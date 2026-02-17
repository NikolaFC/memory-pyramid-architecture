# Troubleshooting Guide

Common issues and solutions for the Memory Pyramid Architecture.

## Installation Issues

### init.py fails with "Permission denied"

**Solution**:
```bash
chmod +x ~/.openclaw/workspace/skills/memory-pyramid-architecture/scripts/init.py
python3 ~/.openclaw/workspace/skills/memory-pyramid-architecture/scripts/init.py
```

### Directories not created

**Check**:
```bash
ls -la ~/.openclaw/workspace/memory/
```

**Manual fix**:
```bash
mkdir -p ~/.openclaw/workspace/memory/{daily_reviews,weekly_distills}
```

### QMD collections not added

**Check**:
```bash
qmd list | grep memory-
```

**Manual fix**:
Edit `~/.openclaw/openclaw.json`, add to `memory.qmd.paths`:
```json
{
  "path": "./memory/daily_reviews",
  "name": "memory-daily-reviews",
  "pattern": "*.md"
},
{
  "path": "./memory/weekly_distills",
  "name": "memory-weekly-distills",
  "pattern": "*.md"
},
{
  "path": "./memory",
  "name": "memory-late-night",
  "pattern": "*-last-night.md"
}
```

Then:
```bash
qmd update
qmd embed
```

## Runtime Issues

### Real-time Sync not capturing conversations

**Symptoms**: `realtime-*.md` files empty or missing

**Check**:
```bash
# Check if cron is running
openclaw cron list | grep "Real-time"

# Check session files exist
ls ~/.openclaw/agents/main/sessions/

# Check log
tail ~/.openclaw/workspace/memory/realtime-sync.log
```

**Solutions**:
1. Ensure `Real-time Chat Sync` cron is enabled
2. Check session directory permissions
3. Verify `realtime-sync.py` exists and is executable

### Micro-Sync never updates

**Symptoms**: `YYYY-MM-DD.md` files empty

**Check**:
```bash
# Look for Micro-Sync updates in file
grep "Micro-Sync Update" ~/.openclaw/workspace/memory/2026-02-17.md
```

**Cause**: Micro-Sync only appends if "meaningful activities" detected

**Solution**: This is normal! It filters out heartbeats and chitchat. Only important activities are logged.

**Force test**:
```bash
# Simulate meaningful activity
echo "## Test Activity" >> ~/.openclaw/workspace/memory/test-activity.md
# Run micro-sync manually
```

### Late Hour Sync missing night activities

**Symptoms**: `*-last-night.md` files empty

**Check time window**:
```bash
# Check current time
date

# Check if night activities exist in realtime file
grep "$(date -d 'yesterday 22:00' '+%Y-%m-%d %H:%M')" ~/.openclaw/workspace/memory/realtime-$(date -d yesterday '+%Y-%m-%d').md
```

**Common causes**:
1. No activity between 22:00-07:00
2. Timezone mismatch
3. Cron job failed

**Check cron status**:
```bash
openclaw cron runs --job-id <late-hour-sync-id>
```

### Daily Review not generating

**Symptoms**: `daily_reviews/` directory empty

**Prerequisites**:
- Must have `YYYY-MM-DD.md` OR `*-last-night.md` files

**Check**:
```bash
ls ~/.openclaw/workspace/memory/2026-02-17*
ls ~/.openclaw/workspace/memory/daily_reviews/
```

**Manual trigger** (for testing):
```bash
# Create test daytime log
cat > ~/.openclaw/workspace/memory/2026-02-17.md << 'EOF'
## Micro-Sync Update (10:00)
- Test activity 1
- Test activity 2
EOF

# Then run Daily Review manually via cron trigger
```

### Weekly Compound not running

**Symptoms**: `weekly_distills/` empty even after Sunday

**Prerequisites**:
- Must have 7 days of `daily_reviews/*.md` files

**Check**:
```bash
ls ~/.openclaw/workspace/memory/daily_reviews/ | wc -l
```

If < 7 files, Weekly Compound may skip or generate partial report.

## QMD and Search Issues

### QMD update fails

**Symptoms**: `qmd update` returns error

**Check**:
```bash
# Check QMD command exists
which qmd

# Check database
cd ~/.openclaw/workspace
qmd status
```

**Common fixes**:
```bash
# Rebuild index
qmd rebuild

# Or delete and recreate
rm -rf ~/.openclaw/qmd
qmd init
qmd update
```

### Can't find memories

**Symptoms**: QMD queries return no results

**Check collections**:
```bash
qmd list
```

**Test query**:
```bash
qmd query "test" --collection memory-daily-reviews
```

**Ensure files are indexed**:
```bash
# Check file exists
ls ~/.openclaw/workspace/memory/daily_reviews/

# Force re-index
qmd update
qmd embed
```

### Wrong retrieval order

**Symptoms**: Getting raw logs when expecting summaries

**Cause**: Retrieval priority not followed

**Correct priority**:
1. `daily_reviews/` - Most distilled
2. `weekly_distills/` - Pattern analysis
3. `topics/` - Long-term knowledge
4. `YYYY-MM-DD.md` - Day logs
5. `*-last-night.md` - Night logs
6. `realtime-*.md` - Raw (last resort)

## Token and Performance Issues

### High token usage in Daily Review

**Normal**: 2000-4000 tokens  
**High**: >8000 tokens

**Cause**: Large input files

**Fix**:
```bash
# Check file size
ls -lh ~/.openclaw/workspace/memory/2026-02-17.md

# If >100KB, consider manual pruning or increasing compression
```

### Context bloat in conversations

**Symptoms**: Session approaching token limit quickly

**Check context composition**:
- Too many code blocks? → Move to files
- Too many tool logs? → They're auto-filtered
- Large pastes? → Summarize before including

**Prevention**:
- Use `/new` to start fresh sessions
- Reference files instead of pasting content
- Rely on MEMORY.md for quick orientation

## Cron Job Failures

### Model not allowed errors

**Error**: `model not allowed: moonshot/kimi`

**Fix**: Update to `moonshot/kimi-k2.5`

```bash
openclaw cron update --job-id <id> --model moonshot/kimi-k2.5
```

### Delivery errors

**Error**: `Delivering to WhatsApp requires target`

**Fix**: Change delivery mode to "none"

```bash
openclaw cron update --job-id <id> --delivery-mode none
```

### Timeout errors

**Error**: Job exceeds timeout

**Check**: 
- Input file sizes
- QMD database size
- Network connectivity

**Fix**: Increase timeout or optimize processing

```bash
openclaw cron update --job-id <id> --timeout 300
```

## Night-Owl Specific Issues

### Night activities appearing in wrong file

**Expected**: 23:00 activity → `2026-02-16-last-night.md`
**Problem**: 23:00 activity → `2026-02-17.md`

**Cause**: Late Hour Sync not running or wrong time window

**Fix**:
1. Check Late Hour Sync schedule: `0 7 * * *`
2. Check timezone in cron config
3. Verify `scripts/config.json` has correct night_owl settings

### Missing early morning activities

**Expected**: 06:00 activity captured in `*-last-night.md`
**Problem**: 06:00 activity missing

**Cause**: Time window calculation error

**Check**:
```python
# Late Hour Sync captures 22:00 yesterday → 07:00 today
# If cron runs at 07:00, it captures up to that moment
```

**Fix**: Ensure activities before 07:00 are complete before cron runs.

## Data Recovery

### Accidentally deleted memory files

**Recovery options**:

1. **From backup** (if exists):
```bash
ls ~/.openclaw/workspace/memory/*.backup
```

2. **From realtime logs**:
```bash
# Reconstruct from raw logs
grep "2026-02-17" ~/.openclaw/workspace/memory/realtime-2026-02-17.md
```

3. **Regenerate via cron**:
- Daily Review can regenerate from structured logs
- Weekly Compound from daily reviews

### Corrupted QMD index

**Symptoms**: Strange search results, missing files

**Fix**:
```bash
# Backup first
cp -r ~/.openclaw/qmd ~/.openclaw/qmd.backup.$(date +%Y%m%d)

# Rebuild
qmd rebuild

# Or full reset
rm -rf ~/.openclaw/qmd
qmd init
qmd update
qmd embed
```

## Getting Help

### Check logs

```bash
# Cron execution logs
ls ~/.openclaw/workspace/skills/cron-activity-tracker/logs/

# Real-time sync log
tail ~/.openclaw/workspace/memory/realtime-sync.log

# Gateway logs
tail ~/.openclaw/gateway.log
```

### Debug mode

Run scripts manually with debug output:

```bash
python3 ~/.openclaw/workspace/skills/memory-pyramid-architecture/scripts/init.py --debug
```

### Community support

- OpenClaw Discord: [link]
- GitHub Issues: [link]
- Ask your AI assistant!

## Prevention Checklist

- [ ] Run `init.py` after any config changes
- [ ] Monitor cron job status weekly
- [ ] Check QMD health monthly
- [ ] Review `daily_reviews/` for quality
- [ ] Archive old `realtime-*.md` files quarterly
- [ ] Backup `topics/` directory regularly
