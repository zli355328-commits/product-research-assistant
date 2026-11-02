# 商品研究助手 / Product Research Assistant

把“我想要那种感觉”变成可核验的商品路线，再交给千问搜索淘宝。

用户表达与判断 → 研究助手查证并提炼 → 千问搜索 → 用户贴回候选 → 研究助手修订。

## 提供的文件

- `skills/product-research/SKILL.md`：核心工作流，可单独作为Agent Skill使用。
- `plugin.json`：便于分发的Agent Plugins清单。
- `.codex-plugin/plugin.json`：Codex兼容清单。
- `通用指令.md`：供普通聊天复制使用，与技能核心正文相同。
- `tests/scenarios.md`：人工行为验收场景；不是已运行的模型评测成绩。

这是无连接器的流程插件：不自带淘宝权限、千问账号、支付或后台运行能力。研究依赖宿主提供的检索工具；没有工具时必须说明关键事实待核验。

## 最简单的使用方式

普通GPT聊天：复制`通用指令.md`全文，然后补一句“我想买……”。不要只上传为参考资料后期待所有聊天自动遵守，也不要假设上传到GitHub便安装到了GPT。

支持本地技能的Codex：把`skills/product-research`文件夹放到工作目录的`.agents/skills/`下，然后在新会话中输入：

> 使用 $product-research。我想买……

要跨项目使用，可按照当前宿主文档配置个人技能目录。这里不自动覆盖用户已有同名技能，不修改全局设置。

插件宿主：按其导入/本地插件或marketplace流程选择包。这里提供清单和技能，不代表已在你的账号安装、通过平台审核或上架；具体入口取决于宿主版本与权限。

## 最终输出约定

需求基本清楚后，研究助手只给不超过500字符的可复制指令。计入中文、英文逐字母、数字、标点和内部换行；去掉文本首尾空白。它应含需求、店铺线索、路线/关键词、核验规则与候选回传格式。

预算未知不当无限；没有证据不直接判差；关键词分组分别搜，不全部叠加。初次澄清最多问少量关键问题，用户不需要先学术语。

长度校验：`python skills/product-research/scripts/check_length.py instruction.txt`

该检查只证明长度，不证明研究正确、关键词有效或模型一定遵守。

## GitHub分享

这个文件夹可作为独立仓库内容；包括隐藏目录`.codex-plugin`。只上传本包，不上传原购物记录、个人文件或整段聊天。公开发布、仓库归属和平台上架需要单独确定，本包尚未发布。

许可：MIT。示例全部是合成验收题，不代表真实商品、搜索或测试结果。不包含参考教材照片或第三方文章复制件。

## 设计依据（核对日期：2026-11-02）

- [技能与本地发现](https://learn.chatgpt.com/docs/build-skills)
- [插件打包与兼容格式](https://developers.openai.com/plugins/build/plugins)
- [插件提交](https://developers.openai.com/plugins/deploy/submission)

本包完成文件结构、YAML/JSON和长度工具检查。模型行为按`tests/scenarios.md`逐项验收；插件宿主导入与商店提交未实测。
