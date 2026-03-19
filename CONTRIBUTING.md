# 贡献指南 🤝

感谢你考虑为 Doc2Book 做贡献！

## 🌟 如何贡献

### 报告 Bug

如果你发现了 bug，请 [创建 Issue](https://github.com/bradenwu/doc2book/issues/new) 并包含：

1. **描述**: 清晰描述问题
2. **复现步骤**: 如何重现这个问题
3. **期望行为**: 你期望发生什么
4. **实际行为**: 实际发生了什么
5. **环境**: Python 版本、操作系统等

### 提交功能请求

欢迎提出新功能建议！请创建 Issue 并说明：

1. **功能描述**: 你希望的功能
2. **使用场景**: 这个功能解决什么问题
3. **可选实现**: 如果有想法，可以描述实现方式

### 提交代码

1. **Fork 仓库**
   ```bash
   git clone https://github.com/your-username/doc2book.git
   cd doc2book
   ```

2. **创建分支**
   ```bash
   git checkout -b feature/amazing-feature
   ```

3. **安装开发依赖**
   ```bash
   python -m venv venv
   source venv/bin/activate
   pip install -e ".[dev]"
   ```

4. **编写代码**
   - 遵循 PEP 8 代码风格
   - 添加必要的注释和文档字符串
   - 为新功能编写测试

5. **运行测试**
   ```bash
   pytest
   ```

6. **提交更改**
   ```bash
   git add .
   git commit -m "feat: 添加某某功能"
   ```

   提交信息格式：
   - `feat:` 新功能
   - `fix:` Bug 修复
   - `docs:` 文档更新
   - `style:` 代码格式（不影响功能）
   - `refactor:` 重构
   - `test:` 测试相关
   - `chore:` 构建/工具相关

7. **推送到 GitHub**
   ```bash
   git push origin feature/amazing-feature
   ```

8. **创建 Pull Request**
   - 描述你的更改
   - 关联相关 Issue
   - 等待代码审查

## 📋 代码规范

- **Python 版本**: 支持 3.10+
- **代码风格**: PEP 8
- **类型提示**: 推荐使用类型注解
- **文档字符串**: 使用 Google 风格

```python
def example_function(arg1: str, arg2: int) -> bool:
    """示例函数说明。
    
    Args:
        arg1: 第一个参数说明
        arg2: 第二个参数说明
        
    Returns:
        返回值说明
        
    Raises:
        ValueError: 异常说明
    """
    pass
```

## 🏗️ 项目结构

```
doc2book/
├── cli/            # 命令行接口
├── core/           # 核心逻辑
├── crawler/        # 爬虫模块
├── builder/        # 内容构建
├── exporter/       # 导出模块
├── models/         # 数据模型
├── config/         # 配置
└── utils/          # 工具函数
```

## 💬 获取帮助

- **GitHub Issues**: 提问或报告问题
- **Pull Requests**: 代码贡献

---

再次感谢你的贡献！🙏
