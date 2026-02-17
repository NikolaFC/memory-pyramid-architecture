# 上传到 GitHub 指南

## 准备工作

### 1. 创建 GitHub 账号

如果还没有 GitHub 账号，先去 [github.com](https://github.com) 注册。

### 2. 创建新仓库

1. 登录 GitHub
2. 点击右上角 `+` → `New repository`
3. 填写信息：
   - **Repository name**: `memory-pyramid-architecture`（或你喜欢的名字）
   - **Description**: `Four-layer memory architecture for OpenClaw with night-owl optimization`
   - **Visibility**: 选择 `Public`（推荐，方便社区贡献）或 `Private`
   - **Initialize**: ❌ 不要勾选 "Add a README"（我们已经有 README 了）
4. 点击 `Create repository`

## 上传步骤

### 方法一：HTTPS（推荐新手）

```bash
# 进入 skill 目录
cd ~/.openclaw/workspace/skills/memory-pyramid-architecture

# 重命名本地 README 为 GitHub 版本
mv README.md README_LOCAL.md
mv README_GITHUB.md README.md

# 添加 GitHub 仓库地址（替换 YOUR_USERNAME 为你的 GitHub 用户名）
git remote add origin https://github.com/YOUR_USERNAME/memory-pyramid-architecture.git

# 推送代码到 GitHub
git push -u origin master

# 输入你的 GitHub 用户名和密码
# 注意：GitHub 现在使用 Personal Access Token 代替密码
```

### 方法二：SSH（如果你配置了 SSH Key）

```bash
# 进入 skill 目录
cd ~/.openclaw/workspace/skills/memory-pyramid-architecture

# 重命名本地 README
mv README.md README_LOCAL.md
mv README_GITHUB.md README.md

# 添加 GitHub 仓库地址（替换 YOUR_USERNAME）
git remote add origin git@github.com:YOUR_USERNAME/memory-pyramid-architecture.git

# 推送代码
git push -u origin master
```

## 获取 GitHub Personal Access Token

GitHub 不再支持密码登录，需要使用 Token：

1. 登录 GitHub
2. 点击头像 → `Settings`
3. 左侧菜单 → `Developer settings`
4. 点击 `Personal access tokens` → `Tokens (classic)`
5. 点击 `Generate new token (classic)`
6. 填写：
   - **Note**: "Memory Pyramid Git Push"
   - **Expiration**: 可选 30 days 或 No expiration
   - **Scopes**: 勾选 `repo`（完整仓库访问）
7. 点击 `Generate token`
8. **立即复制 token**（只显示一次！）

上传时代码密码时，粘贴这个 token 而不是你的 GitHub 密码。

## 验证上传成功

```bash
# 检查远程仓库连接
git remote -v

# 应该显示：
# origin  https://github.com/YOUR_USERNAME/memory-pyramid-architecture.git (fetch)
# origin  https://github.com/YOUR_USERNAME/memory-pyramid-architecture.git (push)
```

然后访问：
```
https://github.com/YOUR_USERNAME/memory-pyramid-architecture
```

你应该能看到所有文件！

## 后续更新

```bash
# 进入目录
cd ~/.openclaw/workspace/skills/memory-pyramid-architecture

# 查看修改状态
git status

# 添加修改的文件
git add .

# 提交修改
git commit -m "描述你的修改"

# 推送到 GitHub
git push
```

## 常见问题

### Q: 提示 "remote origin already exists"
```bash
# 删除已有的 remote
git remote remove origin

# 重新添加
git remote add origin https://github.com/YOUR_USERNAME/memory-pyramid-architecture.git
```

### Q: 提示 "failed to push some refs"
```bash
# 先拉取远程更改
git pull origin master

# 然后再推送
git push -u origin master
```

### Q: 提示 "Permission denied"
- 检查 token 是否有 `repo` 权限
- 检查仓库名是否正确
- 检查是否是仓库所有者

## 分享给社区

上传后，你可以：

1. **分享链接** - 直接把 GitHub 链接发给朋友
2. **提交到 OpenClaw 社区** - 联系 OpenClaw 维护者添加到你的 skills 列表
3. **写博客介绍** - 分享你的设计思路和使用体验

## 示例仓库地址

```
https://github.com/satoshi/memory-pyramid-architecture
```

（记得把 satoshi 换成你的 GitHub 用户名）

---

需要我帮你检查 Git 状态或者生成其他文件吗？🚀
