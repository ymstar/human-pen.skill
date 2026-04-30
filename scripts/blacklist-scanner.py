#!/usr/bin/env python3
"""
黑名单词扫描脚本
功能：扫描markdown文件中的AI高频词黑名单
输出：命中词列表、出现次数、位置（行号）、替换建议
返回：退出码 0=无命中，1=有命中
"""

import sys
import re
from pathlib import Path

# AI高频词黑名单及替换建议
BLACKLIST = {
    # 直接删除类
    "此外": "",
    "希望这对您有帮助": "",
    "让我们": "",
    
    # 软替换类
    "至关重要": "关键、要紧",
    "深入探讨": "仔细看、聊聊",
    "强调": "说、提一嘴",
    "格局": "眼界、视野",
    "无缝": "直接、顺手",
    "直观": "一看就懂、清楚",
    "展示": "看、给你看",
    "证明": "说明、看得出来",
    "充满活力": "活跃、带劲",
    "值得注意的是": "有意思的是、注意",
    "事实上": "其实、实际上",
    "总而言之": "总结下、一句话",
    "旨在": "就是想、目的是",
    "致力于": "在做、专注",
    "亟待": "得赶紧、需要马上",
    "不可或缺": "少不了、必须的",
    "相得益彰": "搭配好、互相配合",
    "显著成效": "效果明显、变化大",
    "深刻变革": "大变、翻天覆地",
    "协同发展": "一起搞、配合着来",
    "远超想象": "比想的厉害、超预期",
    "蓬勃发展": "火了、快速发展",
    "不可忽视": "不能小看、得重视",
    "前所未有": "头一回、从没有过",
    "众所周知": "大家都知道",
    "毋庸置疑": "没得说、肯定的",
    "由此可见": "这说明、看得出来",
    "综上所述": "总结一下",
    
    # 句式简化类
    "唯有...才能...": "只有...才...",
    "不仅...更...": "不光...还...",
    "随着...的发展...": "...越来越...、现在...",
}


def scan_file(file_path: str) -> dict:
    """扫描文件，返回命中结果"""
    results = {
        "file": file_path,
        "total_hits": 0,
        "hits": []
    }
    
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            lines = f.readlines()
    except FileNotFoundError:
        print(f"错误：文件不存在 - {file_path}")
        sys.exit(1)
    except Exception as e:
        print(f"错误：读取文件失败 - {e}")
        sys.exit(1)
    
    # 编译正则模式
    patterns = []
    for word in BLACKLIST.keys():
        # 转义特殊字符，构建词边界匹配
        escaped = re.escape(word)
        # 处理 "..." 占位符模式
        if "..." in word:
            parts = escaped.split(r'\.\.\.')
            pattern = r'\s*'.join(parts)
            try:
                patterns.append((word, re.compile(pattern, re.IGNORECASE)))
            except re.error:
                continue
        else:
            try:
                patterns.append((word, re.compile(escaped, re.IGNORECASE)))
            except re.error:
                continue
    
    # 扫描每一行
    for line_num, line in enumerate(lines, start=1):
        for word, pattern in patterns:
            matches = list(pattern.finditer(line))
            for match in matches:
                replacement = BLACKLIST[word]
                results["hits"].append({
                    "line": line_num,
                    "word": word,
                    "replacement": replacement if replacement else "(直接删除)",
                    "context": line.strip()[:100]  # 截取上下文
                })
                results["total_hits"] += 1
    
    return results


def print_report(results: dict) -> None:
    """打印扫描报告"""
    print("\n" + "=" * 60)
    print(f"📄 文件: {results['file']}")
    print("=" * 60)
    
    if results["total_hits"] == 0:
        print("\n✅ 未检测到AI高频词，文章通过检查！")
        return
    
    print(f"\n⚠️  检测到 {results['total_hits']} 处AI高频词：\n")
    
    # 按行号排序
    results["hits"].sort(key=lambda x: (x["line"], x["word"]))
    
    current_line = -1
    for hit in results["hits"]:
        if hit["line"] != current_line:
            print(f"\n📍 第 {hit['line']} 行:")
            current_line = hit["line"]
        
        print(f"   • \"{hit['word']}\" → {hit['replacement']}")
        print(f"     上下文: {hit['context'][:80]}...")
    
    print("\n" + "-" * 60)
    print("\n📋 替换建议汇总：")
    
    # 汇总统计
    summary = {}
    for hit in results["hits"]:
        key = (hit["word"], hit["replacement"])
        if key not in summary:
            summary[key] = 0
        summary[key] += 1
    
    for (word, replacement), count in sorted(summary.items(), key=lambda x: -x[1]):
        rec = replacement if replacement else "(直接删除)"
        print(f"   [{count}次] \"{word}\" → {rec}")
    
    print("\n" + "=" * 60)


def main():
    if len(sys.argv) < 2:
        print("用法: python blacklist-scanner.py <文件路径>")
        print("示例: python blacklist-scanner.py ./article.md")
        sys.exit(1)
    
    file_path = sys.argv[1]
    results = scan_file(file_path)
    print_report(results)
    
    # 返回退出码
    if results["total_hits"] > 0:
        sys.exit(1)
    else:
        sys.exit(0)


if __name__ == "__main__":
    main()
