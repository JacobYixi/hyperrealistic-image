#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
超真实生图 - 提示词优化器 v8
核心原理：黄金三段式结构
  第一段（置顶）：具体设备 + 拍摄逻辑 + 色彩 + 画质描述
  第二段（中间）：主体内容 + 不完美细节
  第三段（结尾）：反AI否定式描述

v8 更新（2026.06.07 实战验证）：
- 🔑 极端语言法则：说"饱和度低"模型会打折执行，必须用"极低极低""灰扑扑黄乎乎的"等极端重复表达
- 🔑 反精致关键词：人物新增"五官平淡、丢人堆里找不到、头发油乱、不凹造型不摆pose"
- 🔑 环境≠破旧：正常场所（咖啡馆、商场）只需"普通、俗气、不精致"，千万别写成危房
- 00年代参数上调：从"轻微偏黄/轻微褪色"改为"偏黄偏灰/明显褪色/饱和度低"
- 新增验证示例：2000年中国咖啡馆随手拍

v7 更新（2026.06.07 实战验证）：
- 🔑 核心升级：设备名称必须搭配拍摄逻辑！只写设备名不写"用这个设备的人会怎么拍"，AI会忽略年代继续用完美构图
- 新增拍摄逻辑对照表：卡片机→随手按构图歪、照相馆→师傅摆拍闪光灯、老手机→单手歪着拍
- 新增2个验证示例：70年代全家福、2000年杀马特街拍
- 调参指南新增全家福/街拍专项排查
- 修复街拍/全家福构图过于精致的问题

v6 更新（2025.06.06 实战验证）：
- 新增多人场景朝向统一处理：自动检测多人场景，添加强制朝向一致的描述
- 新增第一人称视角增强：检测到第一人称时，添加手部边缘、轻微倾斜等真实感细节
- 优化手机随手拍风格：调整画质描述的度，不太清也不糊，就是普通手机的水平
- 新增光线描述模板：拉窗帘的教室、阴天、夜晚室内等场景的精准光线描述
- 新增常见踩坑记录对应的规避逻辑

v5 更新：
- 新增年代分级（70/90/00年代），不同年代不同程度的褪色/泛黄/画质
- 优化画质描述：用"分辨率不高""细节软软的"代替"模糊"，避免像素风
- 新增建筑/环境反AI元素库
- 强化人物反同质化，加入"眼睛不大"等细节
- 更多验证过的真实感关键词
"""

import random
import re
from typing import List, Dict, Optional


# ==================== 年代分级配置 ====================
# 不同年代对应不同的泛黄、褪色、画质程度
ERA_CONFIG = {
    "1970s": {
        "name": "70年代",
        "yellowing": "严重泛黄",
        "fading": "严重褪色，颜色都快褪完了，接近黑白但还有一点点颜色",
        "quality": "画质很差，分辨率很低，很多细节都看不清，有很多胶卷颗粒和噪点",
        "saturation": "饱和度极低，几乎没有鲜艳的颜色",
        "contrast": "对比度很低，灰蒙蒙的",
        "devices": ["国产胶卷相机", "海鸥相机", "上海牌胶卷相机"],
        "keywords": ["中山装", "军便装", "直筒裤", "自行车", "木招牌", "标语", "砖房", "灰蓝黑军绿"],
    },
    "1980s": {
        "name": "80年代",
        "yellowing": "明显泛黄",
        "fading": "褪色比较严重，颜色发闷发灰",
        "quality": "画质一般，分辨率不高，颗粒感重",
        "saturation": "饱和度很低，颜色不鲜艳，灰蒙蒙的",
        "contrast": "对比度不高",
        "devices": ["海鸥相机", "凤凰相机", "柯达胶卷"],
        "keywords": ["的确良", "喇叭裤", "自行车", "搪瓷缸", "三转一响"],
    },
    "1990s": {
        "name": "90年代",
        "yellowing": "中度泛黄",
        "fading": "明显褪色，颜色偏黄偏暗",
        "quality": "画质一般，颗粒感重，有点模糊但还能看清",
        "saturation": "饱和度很低，色彩灰扑扑的，完全没有鲜艳的颜色",
        "contrast": "对比度低，灰蒙蒙的",
        "devices": ["柯达金胶卷", "富士胶卷", "傻瓜相机"],
        "keywords": ["港风", "大哥大", "BP机", "小霸王", "桑塔纳"],
    },
    "2000s": {
        "name": "00年代",
        "yellowing": "偏黄偏灰",
        "fading": "明显褪色，颜色发灰发闷",
        "quality": "画质一般，分辨率不高，细节软软的，有数码噪点",
        "saturation": "饱和度很低很低，颜色发灰发闷，灰扑扑黄乎乎的，没有任何一个颜色是鲜艳的",
        "contrast": "对比度不高，灰蒙蒙的",
        "devices": ["山寨手机", "杂牌拍照手机", "老式数码相机", "卡片机", "CCD相机"],
        "keywords": ["非主流", "火星文", "MP3", "诺基亚", "摩托罗拉"],
    },
    "2010s": {
        "name": "10年代",
        "yellowing": "基本不黄",
        "fading": "几乎不褪色",
        "quality": "画质较好，比较清晰，但不如现在的手机",
        "saturation": "饱和度中等",
        "contrast": "正常对比度",
        "devices": ["早期智能手机", "数码相机", "iPhone4"],
        "keywords": ["微信", "微博", "小米", "苹果4"],
    },
}


# ==================== 多人场景朝向统一描述 ====================
MULTI_PEOPLE_ORIENTATION = [
    "所有人都朝向同一个方向",
    "每个人的朝向都是一致的",
    "绝对没有面向镜头的人",
    "所有人都背对着镜头",
    "只能看到后脑勺和后背",
    "没有人转过头来",
    "所有人物的朝向都是统一的",
]


# ==================== 第一人称视角增强描述 ====================
FIRST_PERSON_ENHANCEMENT = [
    "画面左下角能看到一点点自己的手指边缘",
    "能看到一点点自己的手的影子",
    "视角略微低头，就是自己举着手机拍的角度",
    "前景有一点点模糊的遮挡，像是自己的胳膊",
    "画面边缘能看到一点点手机边框的影子",
]


# ==================== 光线场景描述 ====================
LIGHTING_SCENARIOS = {
    "curtain_room": {
        "keywords": ["窗帘", "拉着窗帘", "教室", "午睡", "阴天", "昏暗"],
        "descriptions": [
            "窗帘拉着，有柔和的漫射光照进来，整体偏暗但东西都能看清",
            "关着灯拉着窗帘，只有窗外的自然光透进来，光线柔和偏暗",
            "室内光线偏暗，不是开灯的那种亮，就是拉着窗帘的白天的感觉",
        ],
    },
    "cloudy_outdoor": {
        "keywords": ["阴天", "雨天", "下雨", "乌云", "灰蒙蒙"],
        "descriptions": [
            "阴天的自然光，光线柔和不刺眼，整体偏冷调",
            "阴雨天的光线，很柔和，没有明显的影子",
            "灰蒙蒙的天气，光线均匀，没有强烈的阳光",
        ],
    },
    "night_indoor": {
        "keywords": ["晚上", "夜晚", "夜里", "灯光", "台灯", "暖光"],
        "descriptions": [
            "暖黄灯光，只有一盏灯，周围比较暗，有明显的光影对比",
            "夜晚室内，台灯光线，温暖偏黄，周围环境比较暗",
            "室内灯光，色温偏黄，光线不均匀，有明显的明暗对比",
        ],
    },
}


# ==================== 风格预设 ====================
STYLE_PRESETS = {
    "phone_snapshot": {
        "name": "手机随手拍",
        "emoji": "📱",
        "description": "日常记录、生活vlog感、校园生活",
        "opening_templates": [
            "用手机随手拍的照片，单手举起来按的快门，构图很随意画面略微倾斜，画质一般，分辨率不高，细节软软的，有轻微的数码噪点，自动白平衡不准有点偏色，色彩不鲜艳饱和度不高，绝对不是那种鲜艳锐利的高清图，就是普通手机拍的水平",
            "手机抓拍的照片，没对好焦就按了，画面略微有点歪，构图很随意，画质普通，有噪点，颜色有点偏不鲜艳，绝对不是高清大片，不是专业拍的",
            "日常随手拍，随手举起手机按的，画面有点歪，前景有一点点遮挡，画质普通，不是特别清晰也不糊，色彩不是很鲜亮饱和度不高，有一点点噪点，就是正常手机拍的感觉",
            "智能手机拍的照片，单手持机随手一拍，构图没讲究，画面略微倾斜，画质还行，有轻微的数码噪点，白平衡略微不准偏色，色彩自然不艳丽，绝对不是那种精致的高清照片，就是日常记录的水平",
        ],
        "composition": [
            "构图有点歪",
            "画面略微倾斜",
            "主体不在画面中心",
            "上面/旁边有点裁切掉",
            "随手拍的没讲究构图",
            "前景有一点点遮挡",
            "角度有点随意",
        ],
        "quality": [
            "有轻微的数码噪点",
            "画质一般，不是特别清晰",
            "细节软软的，不是锐利的",
            "分辨率不是很高",
            "色彩饱和度不高",
            "白平衡有点不准",
        ],
        "human": [
            "长得很普通，不是网红脸，五官平淡，丢人堆里找不到",
            "眼睛不大，普通大小，不是大眼睛",
            "皮肤有毛孔，不是完美皮肤，脸上有小瑕疵",
            "头发有点油有点乱，有碎发",
            "表情很自然，不是标准微笑",
            "没有看镜头",
            "衣服有点褶皱",
            "不凹造型，不摆pose，整个人很随意不精致",
            "每个人长得都不一样，各有各的特点",
            "所有人朝向一致",
        ],
        "environment": [
            "环境很普通，就是日常的样子，不精致也不豪华",
            "东西有点乱，不是刻意摆的",
            "装修有点俗气，很普通的那种",
        ],
        "negative": [
            "不是精修图",
            "不是AI生成的",
            "不是专业摄影",
            "不是摆拍",
            "不是高清的",
            "就是普通人随手拍的",
            "就是一张很普通的照片",
        ],
    },
    "film": {
        "name": "胶片感",
        "emoji": "🎞️",
        "description": "文艺、复古、氛围感",
        "opening_templates": [
            "柯达金胶卷拍的胶片照片，用胶片机对着取景器拍的，构图有点随意，颗粒感重，色彩偏暖偏黄，对比度不高，有点褪色的感觉，有轻微的暗角，就是胶片机拍的质感",
            "富士C200胶卷拍摄，手动过片拍的，构图不是特别讲究，色彩偏青绿，颗粒感明显，对比度偏低，有复古的感觉，不是数码的锐利感",
            "胶片照片，手动对焦不太准，画面略歪，有明显的胶片颗粒，色彩柔和，有点褪色，暗角明显，氛围感强",
        ],
        "composition": [
            "方形构图",
            "留白比较多",
            "构图有点随意",
            "有一点暗角",
            "边缘画质有点下降",
        ],
        "quality": [
            "胶片颗粒感明显",
            "色彩偏暖/偏青",
            "对比度不高",
            "有点褪色的感觉",
            "不是特别锐利",
            "有轻微的漏光感",
        ],
        "human": [
            "皮肤质感自然，不是磨皮的，脸上有小瑕疵",
            "表情很自然",
            "头发有自然的碎发，有点油有点乱",
            "不是网红脸，五官平淡",
            "普通人的长相，丢人堆里找不到",
            "每个人长得都不一样",
            "所有人朝向一致",
        ],
        "environment": [],
        "negative": [
            "不是精修图",
            "不是AI生成的",
            "不是数码大片",
            "就是普通的胶片抓拍",
        ],
    },
    "documentary": {
        "name": "纪实街拍",
        "emoji": "📷",
        "description": "街头、人文、故事感",
        "opening_templates": [
            "纪实街拍照片，随手举起相机按的快门，构图倾斜画面有真实的杂乱感，高对比度，硬光，胶片颗粒感，有点动态模糊，就是街头抓拍的感觉",
            "理光GR拍的街拍，snap快拍模式不看取景器按的，构图有点歪，画质锐利但有颗粒感，对比度高，抓拍感强",
            "徕卡街拍，盲拍的没看取景器，画面歪了，德味色调，高对比，有颗粒感，画面有故事感，不是摆拍的",
        ],
        "composition": [
            "构图倾斜",
            "有点歪",
            "前景有遮挡",
            "背景有点杂乱",
            "人物动态模糊",
            "抓拍的瞬间感",
        ],
        "quality": [
            "高对比度",
            "硬光",
            "胶片颗粒感",
            "有点动态模糊",
            "暗部比较黑",
            "亮部有点过曝",
        ],
        "human": [
            "表情自然，不是摆拍",
            "普通人的样子，五官平淡",
            "穿着普通的衣服",
            "在做自己的事，没看镜头",
            "每个人长得都不一样",
            "不凹造型，整个人很随意",
            "所有人朝向一致",
        ],
        "environment": [
            "街道有点乱，很真实",
            "路边的东西摆得随意",
            "墙面有张贴的痕迹",
        ],
        "negative": [
            "不是摆拍",
            "不是精修图",
            "不是AI生成的",
            "就是街头抓拍的",
            "不是专业人像摄影",
        ],
    },
    "life_record": {
        "name": "生活记录",
        "emoji": "🏠",
        "description": "居家、日常、温馨感",
        "opening_templates": [
            "在室内用手机拍的，单手举着手机随手一拍，画面有点歪，暖黄灯光，色温偏黄，画质一般有噪点，白平衡不准，桌上有杂物，就是居家随手拍的感觉",
            "家里拍的日常照片，随手举手机按的，构图随意，暖色调，灯光有点黄，手机拍的画质一般，东西摆得有点乱，很生活化的感觉",
            "探店随手拍，手机举起来就按了，没讲究构图，室内暖光，有点噪点，画质一般，不是专业美食摄影",
        ],
        "composition": [
            "构图有点歪",
            "拍得有点随意",
            "桌上有杂物",
            "东西有点乱",
            "不是精心构图的",
        ],
        "quality": [
            "室内暖光，色温偏黄",
            "有点噪点",
            "画质一般",
            "白平衡不太准",
            "色彩偏暖",
        ],
        "human": [
            "穿着家居服",
            "很放松的样子",
            "没化妆或者淡妆",
            "表情很随意",
            "普通人的样子，五官平淡",
            "不凹造型，整个人很随意不精致",
            "所有人朝向一致",
        ],
        "environment": [
            "家里有点乱，很真实",
            "家具是普通的款式",
            "有生活气息",
        ],
        "negative": [
            "不是摆拍",
            "不是精修图",
            "不是专业摄影",
            "就是随手拍的日常",
        ],
    },
    "old_photo": {
        "name": "年代旧照片",
        "emoji": "📼",
        "description": "怀旧、复古、年代感",
        # 注意：old_photo 的开头模板会根据年代动态生成，这里放的是通用模板
        "opening_templates": [
            "90年代的老照片，柯达金胶卷傻瓜机拍的，举起来就按快门没讲究构图，画面有点歪，褪色很严重，颜色整体偏黄偏暗，灰蒙蒙的像蒙了一层雾，没有任何一个颜色是鲜亮的，画质一般颗粒重，有灰尘和细小的划痕，从旧相册扫描的，就是老照片的质感",
            "00年代的老照片，用当年的数码相机拍的，随手按的构图很烂，颜色明显褪色发灰发闷，偏黄偏暗，饱和度很低很低，灰扑扑黄乎乎的，没有任何一个颜色是鲜艳的，画质一般，有颗粒感，有点旧旧的感觉",
            "二十多年前的老照片，柯达胶卷拍的，举起来就按没讲究构图，色彩发黄发闷，对比度不高，灰蒙蒙的，没有任何鲜艳的颜色，画质有点模糊，有岁月的痕迹",
        ],
        "composition": [
            "人物站得很端正",
            "传统的构图",
            "画面有点虚",
            "边角有点磨损的感觉",
            "构图有点正，有点死板",
        ],
        "quality": [
            "褪色严重",
            "偏黄偏暗",
            "对比度低",
            "灰蒙蒙的",
            "画质一般，分辨率不高",
            "颗粒感重",
            "有灰尘和划痕",
            "旧照片扫描的质感",
            "细节软软的，不是锐利的",
        ],
        "human": [
            "每个人长得都不一样，各有各的特点",
            "都是普通长相，不是明星脸，五官平淡丢人堆里找不到",
            "表情有点木讷僵硬",
            "穿着老式的衣服",
            "皮肤有岁月的痕迹，脸上有小瑕疵",
            "不是模板化的网红脸",
            "眼睛不大，普通大小",
            "不凹造型，不摆pose",
            "所有人朝向一致",
        ],
        "environment": [
            "墙面斑驳，有脱落的痕迹",
            "不是规整的砖墙，有点脏有点旧",
            "招牌是木头的，油漆掉了一部分",
            "东西都旧旧的，有岁月感",
            "没有鲜艳的颜色，都是灰灰旧旧的",
            "装修普通，有点俗气，不精致不豪华",
        ],
        "negative": [
            "不是精修图",
            "不是AI生成的",
            "不是高清的",
            "不是画的",
            "不是像素风",
            "就是很旧的老照片",
            "从旧相册里翻出来的",
        ],
    },
}

# ==================== 真实度档位 ====================
REALISM_LEVEL = {
    "low": {
        "description": "轻微真实感",
        "openings": 1,
        "composition": 1,
        "quality": 1,
        "human": 1,
        "environment": 0,
        "negative": 2,
    },
    "medium": {
        "description": "中等真实感",
        "openings": 1,
        "composition": 2,
        "quality": 2,
        "human": 2,
        "environment": 1,
        "negative": 2,
    },
    "high": {
        "description": "高度真实感",
        "openings": 1,
        "composition": 2,
        "quality": 3,
        "human": 3,
        "environment": 2,
        "negative": 3,
    },
    "max": {
        "description": "极致真实感",
        "openings": 1,
        "composition": 3,
        "quality": 3,
        "human": 4,
        "environment": 2,
        "negative": 3,
    },
}


# ==================== 辅助函数 ====================

def detect_era(user_input: str) -> Optional[str]:
    """检测用户输入中的年代，返回 ERA_CONFIG 的key"""
    input_lower = user_input.lower()
    
    # 70年代
    if any(word in input_lower for word in ["70年代", "1970", "七十年代", "70s"]):
        return "1970s"
    # 80年代
    if any(word in input_lower for word in ["80年代", "1980", "八十年代", "80s"]):
        return "1980s"
    # 90年代
    if any(word in input_lower for word in ["90年代", "1990", "九十年代", "90s"]):
        return "1990s"
    # 00年代
    if any(word in input_lower for word in ["00年代", "2000", "2008", "2005", "两千年代", "00s", "08年", "05年"]):
        return "2000s"
    # 10年代
    if any(word in input_lower for word in ["10年代", "2010", "2015", "10s", "15年"]):
        return "2010s"
    
    # 模糊匹配
    if any(word in input_lower for word in ["二十多年前", "20多年前"]):
        return "2000s"
    if any(word in input_lower for word in ["三十多年前", "30多年前"]):
        return "1990s"
    if any(word in input_lower for word in ["四十多年前", "40多年前"]):
        return "1970s"
    
    return None


def detect_style(user_input: str) -> str:
    """根据用户输入检测风格"""
    input_lower = user_input.lower()
    
    # 年代检测（优先匹配，因为最具体）
    if detect_era(user_input) or any(word in input_lower for word in ["老照片", "旧照片", "年代感", "怀旧", "复古"]):
        return "old_photo"
    
    # 胶卷/胶片检测
    if any(word in input_lower for word in ["胶片", "胶卷", "柯达", "富士", "film", "胶片感", "胶片机"]):
        return "film"
    
    # 街拍/纪实检测
    if any(word in input_lower for word in ["街拍", "纪实", "街头", "人文", "抓拍", "扫街", "徕卡", "理光"]):
        return "documentary"
    
    # 生活/居家/室内检测
    if any(word in input_lower for word in ["居家", "家里", "室内", "生活记录", "日常", "家里拍的", "探店", "美食"]):
        return "life_record"
    
    # 默认手机随手拍
    return "phone_snapshot"


def detect_realism_level(user_input: str) -> str:
    """检测真实程度"""
    if any(word in user_input for word in ["拉满", "极致", "超级", "最真实", "非常真实", "以假乱真", "完美"]):
        return "max"
    elif any(word in user_input for word in ["很真实", "比较真实", "明显", "真实感强"]):
        return "high"
    elif any(word in user_input for word in ["稍微", "一点点", "轻", "低", "有点真实感"]):
        return "low"
    else:
        return "medium"


def has_human(user_input: str) -> bool:
    """检测描述中是否有人物"""
    human_keywords = [
        "人", "女孩", "男孩", "女生", "男生", "女人", "男人",
        "人物", "人像", "自拍", "全家福", "一家人", "情侣",
        "朋友", "同学", "同事", "老人", "小孩", "孩子",
        "美女", "帅哥", "小姐姐", "小哥哥", "他", "她",
        "们", "大家", "一群人", "好几个人", "很多人",
    ]
    return any(kw in user_input for kw in human_keywords)


def has_multiple_people(user_input: str) -> bool:
    """检测描述中是否有多个/一群人"""
    multi_keywords = [
        "们", "大家", "一群人", "好几个人", "很多人", "两个", "三个",
        "一些人", "人们", "人群", "众人", "全员", "所有人",
        "同学们", "同事们", "朋友们", "家人们", "一家人", "全家福",
        "趴着午睡", "教室午睡", "上课的人",
    ]
    # 先检查是否有人物，再检查是否有多人特征
    if not has_human(user_input):
        return False
    # 有明确的多人关键词
    if any(kw in user_input for kw in multi_keywords):
        return True
    # 检测"背对镜头"、"后脑勺"等暗示多人的词
    if any(word in user_input for word in ["背对", "背对着", "后脑勺", "后背", "朝向一致"]):
        return True
    return False


def is_first_person(user_input: str) -> bool:
    """检测是否为第一人称视角"""
    fp_keywords = [
        "第一人称", "第一视角", "我拍的", "我看到的", "我眼前",
        "我的视角", "从我这个角度", "举着手机拍", "随手拍",
        "偷拍", "偷偷拍", "趴在桌上拍",
    ]
    return any(kw in user_input for kw in fp_keywords)


def detect_lighting_scenario(user_input: str) -> Optional[str]:
    """检测光线场景"""
    input_lower = user_input.lower()
    for scenario_key, scenario in LIGHTING_SCENARIOS.items():
        if any(kw in input_lower for kw in scenario["keywords"]):
            return scenario_key
    return None


def has_environment(user_input: str) -> bool:
    """检测描述中是否有明显的环境/建筑元素"""
    env_keywords = [
        "街景", "街道", "建筑", "房子", "楼", "墙", "店面",
        "商店", "餐厅", "咖啡馆", "公园", "学校", "医院",
        "室内", "客厅", "卧室", "厨房", "背景", "教室",
    ]
    return any(kw in user_input for kw in env_keywords)


# 正常场所关键词（不适用"斑驳脏旧"等描述，改用"普通俗气不精致"）
NORMAL_PLACE_KEYWORDS = [
    "咖啡馆", "咖啡店", "商场", "超市", "办公室", "餐厅", "饭店",
    "奶茶店", "便利店", "书店", "图书馆", "健身房", "理发店",
]


def is_normal_place(user_input: str) -> bool:
    """检测是否为正常档次的场所（不需要写成危房）"""
    return any(kw in user_input for kw in NORMAL_PLACE_KEYWORDS)


def extract_core_description(user_input: str) -> str:
    """提取用户描述中的核心画面内容（去掉风格/程度等修饰词）"""
    core = user_input
    
    # 去掉前缀模式
    prefix_patterns = [
        r"^用.*?风格[：: ]*",
        r"^用.*?生成[：: ]*",
        r"^.*?风格生成[：: ]*",
        r"^.*?风格[：: ]+",
        r"^.*?感生成[：: ]*",
        r"^超真实生成[：: ]*",
        r"^超真实[：: ]+",
        r"^真实感.*?[：: ]+",
        r"^真实感[^，,。.]*?[：: ]+",
        r"^用.*?[：: ]+",
    ]
    
    for pattern in prefix_patterns:
        core = re.sub(pattern, "", core)
    
    # 去掉常见的功能/风格词（保留核心内容）
    remove_words = [
        "超真实", "真实感", "像拍的一样", "照片级", "更真实",
        "胶片感", "胶片", "胶卷", "随手拍", "纪实感", "街拍",
        "生活记录", "旧照片", "老照片", "年代感", "复古",
        "帮我生成", "帮我画", "生成", "画一个", "画一张",
        "做一个", "来一个", "给我", "真实", "以假乱真",
    ]
    
    for word in remove_words:
        core = core.replace(word, "")
    
    # 清理标点和空格
    core = core.lstrip("：:，, 。.")
    core = core.strip()
    
    # 如果清理后为空，返回原输入
    return core if core else user_input


def pick_random_elements(element_list: List[str], count: int) -> List[str]:
    """从列表中随机选取count个不重复的元素"""
    if count <= 0:
        return []
    if count >= len(element_list):
        return element_list.copy()
    return random.sample(element_list, count)


def generate_era_opening(era_key: str) -> str:
    """根据年代生成对应的开头模板（v8：拍摄逻辑+极端语言法则）"""
    era = ERA_CONFIG[era_key]
    device = random.choice(era["devices"])
    
    # 拍摄逻辑对照表：不同年代/设备对应不同的拍摄习惯
    SHOOTING_LOGIC = {
        "1970s": [
            "师傅让站好别动看镜头，正面闪光灯啪一下亮",
            "照相馆师傅摆拍的，表情僵硬不自然像被硬摆的",
            "老相机手动对焦不太准，画面有点歪",
        ],
        "1980s": [
            "举起来就按快门没讲究构图，画面有点歪",
            "傻瓜机拍的，随手按的，对焦不太准",
            "手动过片拍的，构图不太讲究",
        ],
        "1990s": [
            "傻瓜机举起来就按快门，构图没讲究画面有点歪",
            "柯达金胶卷傻瓜机拍的，随手按的没等完美瞬间",
            "照相馆师傅让站好别动，正面闪光灯啪一下",
        ],
        "2000s": [
            "山寨手机单手举起来按的，30万像素分辨率极低，画面歪了，对焦根本对不上",
            "杂牌拍照手机随手拍的，像素很低画质很差，构图烂画面歪，就是那种几十块钱的山寨机",
            "卡片机随手举起按的快门，构图很烂画面略微倾斜",
            "老手机单手举起来按的，没对好焦，画面有点歪，分辨率很低",
            "CCD相机随手拍的，构图随意前景有东西误入",
        ],
        "2010s": [
            "智能手机随手一拍，构图随意画面略微倾斜",
            "手机举起来就按了，没讲究构图",
            "数码相机自动模式拍的，构图一般",
        ],
    }
    
    shooting = random.choice(SHOOTING_LOGIC.get(era_key, SHOOTING_LOGIC["2010s"]))
    
    # 根据年代不同，生成不同的开头描述
    if era_key == "1970s":
        return f"{era['name']}的老照片，{device}拍的，{shooting}。放了四十多年了。{era['fading']}，整体{era['yellowing']}发灰，{era['saturation']}。{era['quality']}。照片上有灰尘和细微的划痕，就是从旧箱子底翻出来的快烂掉的老照片的感觉。"
    elif era_key == "1980s":
        return f"{era['name']}的老照片，{device}拍的，{shooting}。放了三十多年了。颜色{era['fading']}，{era['yellowing']}，{era['saturation']}，没有任何一个颜色是鲜艳的。{era['quality']}。照片有点旧旧的感觉，有轻微的划痕和灰尘。"
    elif era_key == "1990s":
        return f"{era['name']}的老照片，{device}拍的，{shooting}。放了二十多年了。{era['fading']}，整体偏黄偏暗，{era['saturation']}，{era['contrast']}，没有任何一个颜色是鲜亮的。{era['quality']}。有灰尘和细小的划痕，就是旧相册里的老照片的质感。"
    elif era_key == "2000s":
        return f"{era['name']}的老照片，{device}拍的，{shooting}。有年头了。{era['fading']}，颜色{era['yellowing']}，{era['saturation']}。{era['quality']}。就是当年普通相机拍的水平，不是高清图。"
    else:  # 2010s
        return f"{era['name']}的照片，{device}拍的，{shooting}。画质还可以，{era['quality']}。颜色比较正常，{era['saturation']}。就是普通数码照片的感觉。"


# ==================== 核心生成函数 ====================

def generate_prompt(
    user_input: str,
    style: Optional[str] = None,
    realism_level: Optional[str] = None,
) -> Dict:
    """
    使用黄金三段式生成优化后的超真实提示词
    
    Args:
        user_input: 用户原始描述
        style: 风格（phone_snapshot/film/documentary/life_record/old_photo），None则自动检测
        realism_level: 真实程度（low/medium/high/max），None则自动检测
    
    Returns:
        {
            "style": 风格名称,
            "style_emoji": 风格emoji,
            "realism_level": 真实程度,
            "core_description": 核心描述,
            "enhanced_prompt": 优化后的完整提示词,
            "added_elements": 新增的元素列表,
            "has_human": 是否包含人物,
            "has_multiple_people": 是否包含多个人物,
            "is_first_person": 是否为第一人称视角,
            "era": 检测到的年代,
        }
    """
    # 自动检测风格和程度
    if style is None:
        style = detect_style(user_input)
    if realism_level is None:
        realism_level = detect_realism_level(user_input)
    
    # 检测年代（用于 old_photo 风格）
    era = detect_era(user_input)
    
    # 获取风格预设
    preset = STYLE_PRESETS[style]
    level_config = REALISM_LEVEL[realism_level]
    
    # 提取核心描述
    core_desc = extract_core_description(user_input)
    
    # 检测是否有人物、环境、多人、第一人称
    has_human_flag = has_human(user_input) or has_human(core_desc)
    has_multi_flag = has_multiple_people(user_input) or has_multiple_people(core_desc)
    first_person_flag = is_first_person(user_input) or is_first_person(core_desc)
    has_env_flag = has_environment(user_input) or has_environment(core_desc)
    lighting_scenario = detect_lighting_scenario(user_input)
    
    added_elements = []
    
    # ========== 第一段：开头（设备+色彩+画质） ==========
    # 如果是 old_photo 风格且检测到了年代，用年代专属的开头
    if style == "old_photo" and era:
        opening = generate_era_opening(era)
        added_elements.append(f"年代开头：{era}")
    else:
        opening = random.choice(preset["opening_templates"])
        added_elements.append(f"开头：{opening[:30]}...")
    
    # ========== 第二段：不完美元素 ==========
    extra_elements = []
    
    # 光线场景（如果检测到特定光线场景，添加）
    if lighting_scenario:
        light_desc = random.choice(LIGHTING_SCENARIOS[lighting_scenario]["descriptions"])
        extra_elements.append(light_desc)
        added_elements.append(f"光线：{light_desc[:20]}...")
    
    # 构图元素
    comp_elements = pick_random_elements(preset["composition"], level_config["composition"])
    extra_elements.extend(comp_elements)
    added_elements.extend([f"构图：{e}" for e in comp_elements])
    
    # 画质元素
    qual_elements = pick_random_elements(preset["quality"], level_config["quality"])
    extra_elements.extend(qual_elements)
    added_elements.extend([f"画质：{e}" for e in qual_elements])
    
    # 人物元素（如果有人物）
    if has_human_flag and "human" in preset:
        human_count = level_config["human"]
        human_elements = pick_random_elements(preset["human"], human_count)
        extra_elements.extend(human_elements)
        added_elements.extend([f"人物：{e}" for e in human_elements])
    
    # 多人场景特殊处理：添加强制朝向一致的描述
    if has_multi_flag:
        # 添加2-3个朝向统一的描述，越强调效果越好
        orientation_count = 2 if realism_level in ["medium", "low"] else 3
        orientation_elements = pick_random_elements(MULTI_PEOPLE_ORIENTATION, orientation_count)
        extra_elements.extend(orientation_elements)
        added_elements.extend([f"多人朝向：{e}" for e in orientation_elements])
    
    # 第一人称视角增强
    if first_person_flag:
        fp_elements = pick_random_elements(FIRST_PERSON_ENHANCEMENT, 2)
        extra_elements.extend(fp_elements)
        added_elements.extend([f"第一人称：{e}" for e in fp_elements])
    
    # 环境元素（如果有明显的环境/建筑）
    if has_env_flag and "environment" in preset:
        env_count = level_config.get("environment", 1)
        # v8：正常场所（咖啡馆、商场等）不用"斑驳脏旧"，用"普通俗气不精致"
        if is_normal_place(user_input) or is_normal_place(core_desc):
            normal_env = [
                "装修普通，有点俗气，不精致也不豪华",
                "环境很一般，就是普通档次的场所",
                "不豪华不精致，很普通的装修",
                "东西摆得有点随意，不是精心布置的",
            ]
            env_elements = pick_random_elements(normal_env, env_count)
        else:
            env_elements = pick_random_elements(preset["environment"], env_count)
        extra_elements.extend(env_elements)
        added_elements.extend([f"环境：{e}" for e in env_elements])
    
    # ========== 第三段：否定后缀 ==========
    neg_elements = pick_random_elements(preset["negative"], level_config["negative"])
    added_elements.extend([f"否定：{e}" for e in neg_elements])
    
    # ========== 组合成完整提示词 ==========
    parts = []
    parts.append(opening)
    parts.append(core_desc)
    if extra_elements:
        parts.append("，".join(extra_elements))
    if neg_elements:
        parts.append("，".join(neg_elements))
    
    enhanced_prompt = "。".join([p for p in parts if p]) + "。"
    
    # 替换掉可能出现的连续标点
    enhanced_prompt = re.sub(r"[。，]{2,}", "，", enhanced_prompt)
    enhanced_prompt = enhanced_prompt.replace("。。", "。")
    
    return {
        "style": preset["name"],
        "style_emoji": preset["emoji"],
        "realism_level": realism_level,
        "realism_desc": level_config["description"],
        "core_description": core_desc,
        "enhanced_prompt": enhanced_prompt,
        "added_elements": added_elements,
        "has_human": has_human_flag,
        "has_multiple_people": has_multi_flag,
        "is_first_person": first_person_flag,
        "lighting_scenario": lighting_scenario,
        "era": era,
    }


def list_styles() -> List[Dict]:
    """列出所有可用风格"""
    return [
        {
            "key": key,
            "name": value["name"],
            "emoji": value["emoji"],
            "description": value["description"],
        }
        for key, value in STYLE_PRESETS.items()
    ]


def list_eras() -> List[Dict]:
    """列出所有支持的年代"""
    return [
        {
            "key": key,
            "name": value["name"],
            "description": f"{value['yellowing']}，{value['fading']}",
        }
        for key, value in ERA_CONFIG.items()
    ]


# ==================== 测试 ====================
if __name__ == "__main__":
    test_inputs = [
        "一个女孩在咖啡馆看书",
        "用胶片感生成：雨天的街道",
        "真实感拉满：90年代的全家福",
        "街拍：一个男生走在路边",
        "2008年的街景",
        "70年代的城市街道",
        "居家日常：一个人在沙发上玩手机",
        "08年全家福",
        "在教室中午趴桌午睡无聊拍的照片，第一人称视角",
        "上课随手拿起手机偷偷拍照，第一视角",
        "同学们都在教室里午睡，我拍的照片",
    ]
    
    for test in test_inputs:
        result = generate_prompt(test)
        print(f"\n{'='*60}")
        print(f"输入：{test}")
        print(f"风格：{result['style_emoji']} {result['style']}")
        print(f"年代：{result.get('era', '未检测到')}")
        print(f"真实度：{result['realism_level']} ({result['realism_desc']})")
        print(f"有人物：{result['has_human']}")
        print(f"多人场景：{result['has_multiple_people']}")
        print(f"第一人称：{result['is_first_person']}")
        print(f"光线场景：{result.get('lighting_scenario', '未检测到')}")
        print(f"核心描述：{result['core_description']}")
        print(f"优化后：\n{result['enhanced_prompt']}")
        print(f"新增元素：{len(result['added_elements'])} 个")
