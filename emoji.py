from scene import *
import random
import math

class EmojiSpamScene(Scene):
    def setup(self):
        self.background_color = 'black'
        self.emoji_list = []  # 存储所有表情
        self.spawn_interval = 1.0  # 初始生成间隔(秒)
        self.timer = 0
        
    def update(self):
        self.timer += 1/60  # 假设60fps
        
        # 指数加速生成
        if self.timer >= self.spawn_interval:
            self.timer = 0
            self.spawn_interval *= 0.8  # 每次缩短20%间隔
            
            # 在随机位置生成表情
            x = random.randint(0, int(self.size.w))
            y = random.randint(0, int(self.size.h))
            emoji = LabelNode('😅', position=(x, y))
            self.add_child(emoji)
            self.emoji_list.append(emoji)

run(EmojiSpamScene())