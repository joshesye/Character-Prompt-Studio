# 07 · 词表（AI 绘画提示词库）

> 本文件由 `scripts/render_lexicon.py` 从唯一真源 `lexicon/*.md` 自动生成，**不要手改**。
> 改词请改 `lexicon/` 下的源文件，然后重跑 `python scripts/render_lexicon.py`。

**用法**：用 `scripts/lookup.py` 检索，**不要整份读完** —— 本文件只为检索而生。

共 **3397 条**，21 域 / 49 维度 / 175 要素。

**状态**：常用 1562 · 可用 1801 · 少见 13 · 慎用 21　——「慎用」= 有副作用，备注列写明原因，别当普通词用。

---

# ==== 通用层 ====

## 通用-风格

> A · 材料与形式

### 媒介与画种（31）

- 油画 → oil painting〔常用〕
- 丙烯 → acrylic〔常用〕　— 旧译别名：Acrylics
- 水彩 → watercolor〔常用〕　— 颜色靠纸白透出来，叠色会变深
- 水粉 → gouache〔常用〕　— 不透明水彩，覆盖力强，可与水彩叠用，但不是一回事 旧译别名：Gouache
- 粉彩 → pastel〔常用〕　— 干性色粉笔直接画，画面偏粉质 旧译别名：Pastel
- 炭笔 → charcoal〔常用〕　— 比铅笔黑得多、可擦揉，适合铺大关系 旧译别名：Charcoal
- 铅笔 → pencil〔常用〕　— 石墨铅笔，黑白灰，靠笔压出明暗 旧译别名：pencils
- 彩色铅笔 → colored pencil〔常用〕　— 不溶于水，靠叠加出层次 旧译别名：Colored pencil
- 马克笔 → marker〔常用〕　— 酒精性马克笔，颜色透明、干得快 旧译别名：Marker
- 数码绘画 → digital painting〔常用〕　— 笔刷边缘干净 旧译别名：Digital painting
- 数字插画 → digital illustration〔常用〕
- 插画 → illustration〔常用〕
- 儿童插画 → children's illustration〔常用〕　— 旧译别名：Children's Illustration
- 纸上彩墨 → color ink on paper〔常用〕　— 颜色透进纸里
- 素描 → sketch〔常用〕　— 快速抓形，不追求完成度 旧译别名：Sketching
- 水溶彩铅 → watercolor pencil〔可用〕　— 遇水会化开，能画出半水彩的效果
- 蛋彩 → tempera〔可用〕　— 旧译别名：Tempera
- 钢笔和墨 → pen and ink〔可用〕　— 蘸水笔或针管笔加墨水，线条锐利 旧译别名：Pen and ink
- 墨 → ink〔可用〕　— 旧译别名：Ink
- 喷漆 → spray paint〔可用〕　— 旧译别名：Spray Paint; Spray paint
- 滴漆 → dripping paint〔可用〕　— 颜料直接滴、甩在画布上
- 热蜡 → encaustic〔可用〕　— 加热蜡液作画，表面半透明有厚度 旧译别名：Encaustic
- 中国插图 → Chinese illustration〔可用〕
- 平面插图 → flat illustration〔可用〕
- 写实插画 → realistic illustration〔可用〕　— 写实取向的插画，不是照片
- 混合媒介 → mixed media〔可用〕　— 同时用两种以上材料（如彩铅加水彩、拼贴加丙烯） 旧译别名：Mixed media
- 传统媒介 → traditional media〔可用〕　— 手绘的总称，用来对冲数字感
- 壁画 → fresco〔可用〕　— 画在墙上的画，尺度大、带墙面肌理 旧译别名：Fresco
- 手稿 → manuscript〔可用〕　— 纸张发黄、有手写痕迹的书页
- 填色本 → coloring book page〔可用〕　— 只有黑线框等着上色 旧译别名：Coloring book
- 线描水彩 → line and wash〔可用〕　— 先勾线再上淡彩 旧译别名：Line and wash

### 东方水墨（21）

- 水墨画 → sumi-e〔常用〕　— 用墨的浓淡干湿表现，不依赖颜色 旧译别名：Ink wash painting; Sumi-e
- 书法 → calligraphy〔常用〕　— 旧译别名：Calligraphy
- 晕染 → ink gradient〔常用〕　— 墨色由浓到淡自然过渡
- 飞白 → dry brush〔常用〕　— 笔速快、墨少，纸上留出一道道白丝
- 淡墨 → light ink wash〔常用〕　— 颜色浅而层次多
- 浓墨 → dense glossy black ink〔常用〕　— 黑得发亮
- 湿笔 → wet brush〔常用〕　— 水分饱满，边缘自然晕开
- 白描 → pure outline〔常用〕　— 只用线画轮廓，不上墨色
- 写意 → abbreviated strokes〔常用〕　— 笔简而意在，不求形似求神似
- 工笔 → fine even lines〔常用〕　— 线条细匀、层层罩染，画得极精细
- 墨色层次 → tonal gradation of ink〔常用〕
- 焦墨 → dense black ink〔可用〕　— 极浓的墨，黑得发亮
- 泼墨 → splashed ink〔可用〕　— 把墨泼在纸上再顺势成画，随机、气势大
- 破墨 → broken ink〔可用〕　— 后一笔破开前一笔，墨色自然渗化
- 积墨 → layered ink〔可用〕　— 一层层叠加，越叠越厚越沉
- 皴法 → texture stroke〔可用〕　— 国画里表现山石纹理的笔法
- 没骨 → no outline〔可用〕　— 不用墨线勾轮廓，直接用色块塑形
- 楷书 → regular script〔可用〕　— 笔画端正
- 行书 → running script〔可用〕　— 笔画之间有牵丝
- 草书 → cursive script〔可用〕　— 连绵不断
- 禅意笔触 → zen brushwork〔可用〕　— 比写意更少，一笔到底、留大量气口

### 版画与印刷（8）

- 木刻 → woodcut〔常用〕　— 在木板上刻出凸版再印，线条有刀味 旧译别名：Woodcut
- 版画 → printmaking〔可用〕　— 旧译别名：Linocut
- 蚀刻 → etching〔可用〕　— 用酸腐蚀金属版，线条细而匀 旧译别名：Etching
- 石版画 → lithography〔可用〕　— 在石板上画再印，能画出很丰富的调子 旧译别名：Lithography
- 丝网印刷 → screen printing〔可用〕　— 刮板把墨从网孔挤过去，颜色厚、边界硬 旧译别名：Screen printing
- 凹版印刷 → intaglio〔可用〕　— 墨在凹槽里，压印后线条微微凸起 旧译别名：Intaglio
- 利诺剪裁 → linocut〔可用〕　— 在油毡上刻再印，风格像木刻但更软 旧译别名：Lino cut
- riso 印刷 → risograph〔可用〕　— 孔版印刷，颜色错位、有颗粒、只能叠出有限的几种色

### 立体与工艺（18）

- 雕塑 → sculpture〔常用〕　— 旧译别名：ink painting
- 浮雕 → relief〔常用〕　— 图案从底面上凸起来，有厚度和投影 旧译别名：Relief
- 马赛克 → mosaic〔常用〕　— 用小色片拼出画面，远看成型、近看是格子 旧译别名：Mosaic
- 纸雕 → paper cut〔常用〕　— 剪出来的图形，边缘利落、有镂空
- 折纸 → origami〔常用〕　— 旧译别名：Origami
- 瓷器 → porcelain〔常用〕　— 高温烧的瓷，白、硬、薄处透光 旧译别名：Porcelain
- 玉 → jade〔常用〕　— 半透明、温润，光进去会散开 旧译别名：Jade
- 刺绣 → embroidery〔常用〕　— 用线在布上绣出图案，有丝线的光泽和厚度 旧译别名：Embroidered
- 数字拼贴 → digital collage〔可用〕　— 旧译别名：Digital collage
- 拼布拼贴 → patchwork collage〔可用〕　— 布料缝在一起，有接缝和厚度
- 卷纸艺术 → paper quilling〔可用〕　— 把纸条卷起来拼成图案
- 彩色玻璃窗 → stained glass〔可用〕　— 铅条把彩色玻璃拼起来，背光透亮 旧译别名：Stained glass window
- 挂毯 → tapestry〔可用〕　— 织出来的厚布面，有经纬和绒面 旧译别名：Tapestry
- 金银丝细工 → filigree〔可用〕　— 用极细的金属丝盘成纹样
- 绗缝 → quilted〔可用〕　— 夹层布料缝出线条，表面有起伏
- 纹身图案 → tattoo art〔可用〕　— 皮肤上的图案设计
- 景泰蓝 → cloisonné〔可用〕　— 铜胎掐丝再填珐琅彩，颜色鲜明、有金属边 旧译别名：Cloisonne
- 朱红印章 → vermilion seal〔可用〕　— 方形红印，常压在角落

> B · 风格与流派

### 写实程度（11）

- 照片级写实 → photoreal〔常用〕　— 细节密度和真实照片一样
- 超写实 → hyperreal〔常用〕　— 细节比真实照片更多，刻意强化
- 写实 → realistic〔常用〕　— 比例、光影、材质都符合现实，但不必像素级还原
- 半写实 → semi-realistic〔常用〕　— 结构是真的，但能看出是画出来的
- 风格化写实 → stylized realism〔常用〕　— 基底写实，但比例和特征被有意放大
- 卡通化 → cartoonified〔常用〕　— 细节被去掉，只剩大块颜色和明确轮廓
- 高度风格化 → heavily stylized〔常用〕　— 只留最能识别的几个特征，其余全简化
- 极简 → minimal〔常用〕　— 只留最少的信息量
- 抽象化 → abstracted〔可用〕　— 形体被抽掉，只剩轮廓或色块
- 稚拙 → naive〔可用〕　— 比例「错」、线条不规整，但要错得有味道
- 刻意失真 → deliberately off〔可用〕　— 故意画歪比例和透视，制造不安

### 艺术流派（38）

- 文艺复兴 → renaissance〔常用〕　— 旧译别名：Renaissance
- 巴洛克 → baroque〔常用〕
- 古典主义 → neoclassicism〔常用〕　— 旧译别名：Neoclassicism
- 现实主义 → realism〔常用〕
- 印象派 → impressionism〔常用〕
- 野兽派 → fauvism〔常用〕
- 表现主义 → expressionism〔常用〕
- 立体主义 → cubism〔常用〕
- 超现实主义 → surrealism〔常用〕　— 旧译别名：Surrealism
- 波普艺术 → pop art〔常用〕　— 旧译别名：POP art
- 新艺术 → art nouveau〔常用〕　— 藤蔓般的曲线、花卉纹样、边框装饰 旧译别名：Rococo
- 装饰性 → ornamental〔常用〕　— 以纹样和重复为主
- 民间艺术 → folk art〔常用〕　— 配色大胆、造型朴素、对称构图
- 蒸汽朋克 → steampunk〔常用〕　— 黄铜、齿轮、皮革、维多利亚
- 赛博朋克 → cyberpunk〔常用〕　— 霓虹、雨夜、高科技低生活 旧译别名：Cyberpunk
- 合成波 → synthwave〔常用〕　— 八十年代的紫粉荧光、网格地平线 旧译别名：Synth-wave
- 复古黑暗 → retro dark vintage〔常用〕　— 七十年代的暗调印刷
- 黑暗幻想 → dark fantasy〔常用〕　— 阴郁、宏大、带哥特与宗教感 旧译别名：Dark fantasy
- 恐怖 → horror〔常用〕　— 压抑、不安、有威胁感 旧译别名：Horror
- 黑色电影 → film noir〔常用〕　— 高对比黑白、百叶窗影、烟与雨
- 涂鸦 → graffiti〔常用〕　— 街头喷绘，字体夸张、颜色冲撞 旧译别名：Graffiti
- 概念艺术 → concept art〔常用〕　— 以交代设定为目的，重结构和设计 旧译别名：Concept art
- 学院派 → academic art〔可用〕　— 讲究构图、解剖和明暗的古典学院训练
- 浪漫主义 → romanticism〔可用〕　— 旧译别名：Romanticism
- 点彩派 → pointillism〔可用〕　— 用密集的小色点拼出画面，远看颜色自然混合
- 抽象表现主义 → abstract expressionism〔可用〕
- 未来主义 → futurism〔可用〕　— 用速度线和重复形体表现动感 旧译别名：Futurism
- 魔幻现实主义 → magic realism〔可用〕　— 旧译别名：Magic Realism
- 批判现实主义 → critical realism〔可用〕　— 旧译别名：Critical Realism
- 欧普艺术 → op art〔可用〕　— 用几何图形制造视觉错觉，画面像在动 旧译别名：Op art
- 光色主义 → luminism〔可用〕　— 以光本身为主角，画面通透、发光 旧译别名：Luminism
- 唯美主义 → aestheticism〔可用〕　— 只为好看，不承担叙事
- 粗野主义 → brutalism〔可用〕　— 暴露混凝土原始质感，粗重、不加修饰
- 建构主义 → constructivism〔可用〕　— 苏联时期海报风格，斜线构图＋红黑配色 旧译别名：Constructivism
- 超现代 → ultra modern〔可用〕　— 极简加金属与玻璃 旧译别名：Ultra Modern
- 童话风格 → fairy tale style〔可用〕　— 旧译别名：Fairy Tale Style
- 缝隙艺术 → glitch art〔可用〕　— 像素错位与信号故障 旧译别名：Glitchart
- 复古 → vintage〔可用〕　— 十八到十九世纪的旧物感

### 东方风格（5）

- 中国风 → Chinese style〔常用〕
- 国风 → guofeng style〔常用〕　— 当代流行的国潮审美，非严格古风 旧译别名：Traditional Chinese Ink Painting style
- 浮世绘 → ukiyo-e〔常用〕　— 日本江户时代的木版画，平涂、勾线、构图奇巧 旧译别名：Japanese Ukiyo-e
- 日式风格 → japonism〔可用〕　— 西方视角下的日本趣味，平面、装饰、留白 旧译别名：Japonism
- 唐卡 → thangka〔可用〕　— 藏传佛教的卷轴画，色彩浓、构图对称、画工极细 旧译别名：Thangka

### 东方题材（6）

- 武侠 → wuxia〔常用〕　— 侠客、刀剑、江湖气 旧译别名：Wuxia
- 京剧 → Beijing opera〔可用〕　— 脸谱、水袖、靠旗 旧译别名：Beijing Opera
- 昆曲 → kunqu opera〔可用〕　— 更柔、更素，多用于古典仕女 旧译别名：Kunqu opera
- 茶艺 → tea ceremony〔可用〕　— 旧译别名：Tea art
- 中国童话 → Chinese fairy tale〔可用〕　— 旧译别名：Chinese fairy tales
- 凤凰 → Chinese phoenix〔可用〕　— 东方瑞兽，尾羽拖长、颜色浓

### 动漫游戏（19）

- 日式动画 → anime〔常用〕　— 旧译别名：Anime
- 日本漫画 → manga〔常用〕　— 黑白网点、分镜格、速度线
- 卡通 → cartoon〔常用〕　— 造型简化、轮廓加粗、表情夸张
- 二次元 → ACGN〔常用〕　— 用中文说就是「动漫感」，不必写英文缩写
- Q版 → chibi〔常用〕　— 头大身小的二三头身比例，可爱
- 像素艺术 → pixel art〔常用〕　— 用一个个像素点画出来，边缘是阶梯状的 旧译别名：Pixel art
- 8 比特 → 8-bit〔常用〕　— 八位机画面，色数极少、马赛克大
- 赛璐璐风格 → cel shading〔常用〕　— 颜色分成几个明确的色阶，不渐变 旧译别名：cel-shaded style
- 卡通渲染 → toon shading〔常用〕　— 3D 模型渲染成 2D 动画的样子，颜色分块、勾黑边
- 三渲二 → 3D cel-shaded〔常用〕　— 用 3D 模型和渲染，做出 2D 手绘动画的观感
- 3D 动画电影 → 3D animated feature〔常用〕　— 造型圆润、材质细腻、光影柔和
- 游戏 CG → game CG〔常用〕　— 高精度的游戏宣传画
- 卡哇伊 → kawaii〔可用〕　— 圆润、甜、无害
- 16 比特 → 16-bit〔可用〕　— 十六位机画面，颜色和分辨率略高
- 90 年代电视游戏 → 90s video game〔可用〕
- 等距卡通渲染 → isometric cel shading〔可用〕　— 等距视角＋卡通渲染，常见于休闲游戏
- 图形小说 → graphic novel〔可用〕　— 成人向的漫画叙事，色调更沉 旧译别名：Graphic Novel
- 等距动画 → isometric anime〔可用〕　— 旧译别名：Isometric anime
- 魂系 → souls-like〔可用〕　— 灰暗、苍凉、破败的奇幻

### 视觉效果（17）

- 平铺罗列 → knolling〔常用〕　— 物品整齐排列、俯拍
- 拟人化 → anthropomorphic〔常用〕　— 把动物或物体画成人的样子
- 视错觉 → optical illusion〔常用〕
- 扫描线 → scanlines〔常用〕　— 老 CRT 屏幕的横向细线
- 全息投影 → hologram〔常用〕　— 半透明的绿色图像，带扫描线
- X 光透视 → x-ray〔常用〕
- 双重曝光 → double exposure〔常用〕　— 两张画面叠在一张上，互相透出来 旧译别名：Double exposure
- 闪耀效果 → sparkle〔可用〕
- 压缩失真 → jpeg artifacts〔可用〕　— 反复压缩后的方块和马赛克，刻意保留当成风格
- 半调风格 → halftone〔可用〕　— 用大小不同的点模拟连续的明暗，老报纸印刷的做法
- 抖动 → dithering〔可用〕　— 用规律排列的点模拟出中间色，老电脑的渐变做法
- 立体画 → stereogram〔可用〕　— 要眯着眼才看得出
- ASCII 码效果 → ascii art〔可用〕
- 飞溅效果 → splash〔可用〕
- 彩虹反光 → iridescent〔可用〕　— 表面泛出像肥皂泡、油膜那样的多色渐变反光
- 彩色分离 → chromatic separation〔可用〕　— 红蓝通道没能重合，边缘出现红蓝色的重影
- 星闪 → star flash〔可用〕　— 画面里出现十字或四角的星状亮芒，常用来表现高光 旧译别名：Star Flash

### 3D 与渲染（11）

- 3D → 3D render〔常用〕　— 旧译别名：3D Style
- 写实 3D 渲染 → photoreal 3D render〔常用〕　— 材质像照片
- 低多边形 → low-poly〔常用〕　— 刻意保留多边形面数，能看见一个个平面
- 黏土渲染 → clay render〔常用〕　— 没有贴图只有形，表面像哑光黏土
- 白模渲染 → white model〔常用〕　— 整体白灰、没有贴图，只看形体和光影
- 全局光照 → global illumination〔常用〕　— 光线在环境里反复弹跳，阴影柔和 旧译别名：Global Illumination
- 虚幻引擎 → unreal engine〔常用〕　— 实时渲染，材质厚、辉光强 旧译别名：Unreal engine; Unreal Engine
- 线框渲染 → wireframe render〔可用〕　— 只画模型的网格线，不填面
- 辛烷渲染 → octane render〔可用〕　— GPU 渲染器，干净、光真切、材质准
- 光线追踪 → ray tracing〔可用〕　— 逐条光线计算反射折射，反光和阴影物理正确 旧译别名：Ray Tracing
- 立体等距 → isometric 3D〔可用〕　— 没有透视的立体，像游戏里的地图

### 平面设计（11）

- 极简主义 → minimalist style〔常用〕　— 旧译别名：Minimalist
- 扁平化 → flat design〔常用〕　— 无渐变、无阴影、纯色块
- 包豪斯 → bauhaus〔常用〕　— 基本几何形、红黄蓝、无衬线
- 日本海报设计 → Japanese graphic design〔常用〕　— 大量的留白与细字
- 80 年代风格 → 80s style〔常用〕
- 90 年代风格 → 90s style〔常用〕
- 海报排版 → poster layout〔可用〕
- 杂志封面 → magazine cover〔可用〕
- 杂志内页 → magazine spread〔可用〕　— 旧译别名：magazine scan
- 专辑封面 → album cover〔可用〕
- 街头艺术 → street art〔可用〕　— 喷绘、贴纸、模板印刷 旧译别名：Street Art

### 摄影风格（18）

- 电影感 → cinematic〔常用〕　— 像电影镜头：明确的方向光、有层次的暗部、克制的色彩
- 电影摄影 → cinematic photography〔常用〕
- 商业棚拍 → commercial studio photography〔常用〕　— 可控布光、纯色或渐变背景
- 人像摄影 → portrait photography〔常用〕　— 背景干净、光比克制
- 时尚摄影 → fashion photography〔常用〕　— 强烈的造型与布光
- 纪实摄影 → documentary photography〔常用〕　— 自然光、不摆拍
- 街拍摄影 → street photography〔常用〕　— 抓拍瞬间
- 静物摄影 → still life photography〔常用〕
- 商品摄影 → product photography〔常用〕　— 白底或浅灰底
- 胶片摄影 → film photography〔常用〕　— 颗粒与微微的偏色
- 胶片颗粒 → film grain〔常用〕
- 剪影照片 → silhouette shot〔常用〕　— 旧译别名：Silhouette shot
- 逆光照片 → backlit shot〔常用〕　— 旧译别名：Backlit shot
- 商业摄影 → commercial photography〔可用〕　— 干净、准确、有质感 旧译别名：Commercial Photography
- 富士色彩 → fujicolor〔可用〕　— 绿青浓郁、肤色偏暖 旧译别名：Fujicolor
- 微缩模型电影 → miniature model film〔可用〕　— 布景是模型，景深极浅
- 黑色胶片时期 → pulp noir〔可用〕　— 老黑白印刷的粗颗粒
- 柔焦 → soft focus〔可用〕　— 整张轻微发虚，像雾里看

### 线条（23）

- 线描 → line drawing〔常用〕　— 旧译别名：Line drawing
- 轮廓线画 → contour drawing〔常用〕　— 只画外轮廓，不画内部结构 旧译别名：Contour drawing
- 手势画 → gestural drawing〔常用〕　— 寥寥几笔抓动作，不求准 旧译别名：Gestural drawing
- 动态速写 → gesture drawing〔常用〕　— 旧译别名：Gesture drawing
- 交叉排线 → cross-hatching〔常用〕　— 两组斜线交叉，靠疏密出明暗
- 排线 → hatching〔常用〕
- 剪影画 → silhouette drawing〔常用〕　— 旧译别名：Silhouette drawing
- 连续线画 → continuous line drawing〔常用〕　— 一笔到底不断线 旧译别名：Continuous line drawing
- 单线画 → single line drawing〔常用〕　— 旧译别名：Single line drawing
- 书法线画 → calligraphic line drawing〔常用〕　— 线条有提按粗细 旧译别名：Calligraphic line drawing
- 点描 → stippling〔常用〕　— 用密集的小点堆出明暗 旧译别名：Stippling
- 松散线画 → loose line drawing〔常用〕　— 线不闭合、有重复笔 旧译别名：Loose line drawing
- 平面线描 → flat line drawing〔常用〕　— 线宽均匀、不表现体积 旧译别名：Flat line drawing
- 勾勒 → outlining〔可用〕　— 旧译别名：Outlining
- 断线画 → broken line drawing〔可用〕　— 线条一段一段断开 旧译别名：Broken line drawing
- 双线画 → double line drawing〔可用〕　— 每根线都描两遍 旧译别名：Double line drawing
- 负空间画 → negative space drawing〔可用〕　— 画的是物体周围的空间 旧译别名：Negative space drawing
- 紧密线画 → tight line drawing〔可用〕　— 线密到几乎填满 旧译别名：Tight line drawing
- 角度线描 → angular line drawing〔可用〕　— 全用直线折出形 旧译别名：Angular line drawing
- 等距线描 → isometric line drawing〔可用〕　— 旧译别名：Isometric line drawing
- 禅绕画 → zentangle〔可用〕　— 用重复的图案填满一个形状 旧译别名：Zentangle
- 乱画 → scribbling〔可用〕　— 快速、无序、有情绪 旧译别名：Scribbling
- 盲画轮廓 → blind contour drawing〔少见〕　— 只看对象不看纸，形会跑但很有生气

> C · 参照物

### 艺术家（36）

- 达芬奇 → Leonardo da Vinci〔常用〕　— 旧译别名：Leonardo Da Vinci
- 伦勃朗 → Rembrandt〔常用〕
- 克劳德·莫奈 → Claude Monet〔常用〕
- 梵高 → Van Gogh〔常用〕　— 旧译别名：Vincent Van Gogh
- 齐白石 → Qi Baishi〔常用〕
- 伊戈尔·莫尔斯基 → Igor Morski〔常用〕
- 吉卜力 → Studio Ghibli〔常用〕　— 手绘平涂、细节密集、自然光
- 皮克斯 → Pixar〔常用〕　— 圆润造型、明亮材质
- 京都动画 → Kyoto Animation〔常用〕　— 日常系作画、光斑与水的处理精细
- 米开朗基罗 → Michelangelo〔可用〕
- 桑德罗·波提切利 → Sandro Botticelli〔可用〕
- 保罗·塞尚 → Paul Cezanne〔可用〕
- 皮埃尔·奥古斯特·雷诺阿 → Pierre Auguste Renoir〔可用〕
- 瓦西里·康定斯基 → Wassily Kandinsky〔可用〕
- 皮特·蒙德里安 → Piet Mondrian〔可用〕
- 保罗·克利 → Paul Klee〔可用〕
- 吴道子 → Wu Daozi〔可用〕　— 旧译别名：wu daozi
- 宋徽宗赵佶 → Song Huizong〔可用〕　— 旧译别名：Song Huizong Zhao Ji
- 徐悲鸿 → Xu Beihong〔可用〕　— 旧译别名：xu beihong
- 杰里·平克尼 → Jerry Pinkney〔可用〕
- 梦工厂 → DreamWorks〔可用〕
- 巴勃罗·毕加索 → Pablo Picasso〔慎用〕　— 艺术家参照；需要精确控制时，补充具体色彩、构图和笔触特征。
- 马克·罗斯科 → Mark Rothko〔慎用〕　— 艺术家参照；需要精确控制时，补充具体色彩、构图和笔触特征。
- 萨尔瓦多·达利 → Salvador Dali〔慎用〕　— 艺术家参照；需要精确控制时，补充具体色彩、构图和笔触特征。
- 雷内·马格里特 → Rene Magritte〔慎用〕　— 艺术家参照；需要精确控制时，补充具体色彩、构图和笔触特征。
- 罗伊·利希滕斯坦 → Roy Lichtenstein〔慎用〕　— 艺术家参照；需要精确控制时，补充具体色彩、构图和笔触特征。
- 安迪·沃霍尔 → Andy Warhol〔慎用〕　— 艺术家参照；需要精确控制时，补充具体色彩、构图和笔触特征。
- 草间弥生 → Yayoi Kusama〔慎用〕　— 艺术家参照；需要精确控制时，补充具体色彩、构图和笔触特征。
- 村上隆 → Takashi Murakami〔慎用〕　— 艺术家参照；需要精确控制时，补充具体色彩、构图和笔触特征。
- 岳敏君 → Yue Minjun〔慎用〕　— 艺术家参照；需要精确控制时，补充具体色彩、构图和笔触特征。
- 吴冠中 → Wu Guanzhong〔慎用〕　— 艺术家参照；需要精确控制时，补充具体色彩、构图和笔触特征。
- 张大千 → Zhang Daqian〔慎用〕　— 艺术家参照；需要精确控制时，补充具体色彩、构图和笔触特征。 旧译别名：zhang daqian
- 赵无极 → Zao Wou-Ki〔慎用〕　— 艺术家参照；需要精确控制时，补充具体色彩、构图和笔触特征。
- 马特·科利肖 → Mat Collishaw〔慎用〕　— 艺术家参照；需要精确控制时，补充具体色彩、构图和笔触特征。
- 宫崎骏 → Hayao Miyazaki〔慎用〕　— 艺术家参照；需要精确控制时，补充具体色彩、构图和笔触特征。
- 新海诚 → Makoto Shinkai〔慎用〕　— 艺术家参照；需要精确控制时，补充具体色彩、构图和笔触特征。 旧译别名：Shinkai Makoto

### 锚点（5）

- 一九八二年的东京 → Tokyo, 1982〔常用〕　— 年代锚点：一句话顶五十字，模型会补齐一整套符合那个年代的细节
- 罗杰·迪金斯式的打光 → lighting in the style of Roger Deakins〔常用〕　— 创作者锚点：单光源、剪影、大面积暗部
- 一九五七年的哈瓦那 → Havana, 1957〔可用〕　— 年代锚点
- 苏联构成主义海报 → Soviet constructivist poster〔可用〕　— 文化锚点
- 阿什·索普式的电影级体积光 → cinematic volumetric light, Ash Thorp style〔可用〕　— 风格锚点

### 摄影机与胶片（9）

- 香港电影漂白旁路的低饱和 → Hong Kong bleach-bypass, low saturation〔常用〕　— 港风、武侠
- 柯达 200T 的暖橙怀旧胶片色 → warm orange Kodak Vision3 200T〔常用〕　— 复古、怀旧
- ARRI 的色彩科学 → ARRI REVEAL colour science〔常用〕　— 文艺、诗意
- Log-C 冷调去饱和 → Log-C cool desaturated〔常用〕　— 惊悚、悬疑
- 三十五毫米定焦的古典电影感 → shot on a 35mm prime, classic cinematic〔常用〕　— 焦距比摄影机型号更有效的写法
- 用 IMAX 15/70 胶片拍摄 → shot on IMAX 15/70 film〔可用〕　— 史诗、宏大
- 索尼 Venice 2 的青绿冷调 → shot on Sony Venice 2, teal-cool〔可用〕　— 赛博、硬科幻
- 战地纪录片的自然光加灰调 → documentary Log flatness with natural light〔可用〕　— 纪录、战地
- 超十六毫米的高对比偏绿粗粝感 → Super 16mm high-contrast greenish grain〔可用〕　— 恐怖、粗粝

### 年代（7）

- 古代 → ancient〔常用〕　— 旧译别名：Ancient
- 二十世纪八十年代 → 1980s〔常用〕
- 老照片 → old photograph〔常用〕　— 褪色、四角发黄、有划痕 旧译别名：Old Photograph
- 史前 → prehistoric〔可用〕
- 冰河时代 → ice age〔可用〕　— 旧译别名：Ice Age
- 侏罗纪 → jurassic〔可用〕　— 旧译别名：Jurassic
- 十九世纪 → 1800s〔可用〕

## 通用-光线

> A · 布光

### 光位（13）

- 逆光 → backlighting〔常用〕　— 光源在主体背后、镜头对着光拍；主体偏暗，靠边缘光或补光提亮 旧译别名：Backlight
- 伦勃朗光 → Rembrandt light〔常用〕　— 灯在斜上方 45°，暗侧脸颊上留一个倒三角的光斑，古典人像的经典布光 旧译别名：Rembrandt Light
- 四分之三前光 → three-quarter front light〔常用〕　— 最安全的中性光位
- 侧光 → side light〔常用〕　— 戏剧性、悬疑、黑色电影；最能揭示质感 旧译别名：Raking Light
- 四分之三背光 → three-quarter back light〔常用〕　— 情感场景、深度叙事
- 从后场打光 → light from the back of the set〔常用〕　— 电影布光的首选原则；前场打光会拍成证件照
- 分割光 → split lighting〔常用〕　— 主光从侧面 90° 打，脸正好一半亮一半暗，中间一条直线
- 蝴蝶光 → butterfly lighting〔常用〕　— 灯在正前方偏上，鼻子下面留一个小小的蝴蝶形阴影
- 环形光 → loop lighting〔常用〕　— 影子从鼻侧绕到嘴角，形成一个圈
- 底光 → underlighting〔常用〕　— 从下往上打，反着自然光的方向，不安
- 顶光 → toplighting〔常用〕　— 光从正上方下来，眼窝和下颌陷进阴影，正午户外就是这个效果 旧译别名：Top Light
- 前光 → frontal light〔可用〕　— 多数情况要避免；只有刻意要高调时尚时才用
- 正后方背光 → full back light〔可用〕　— 梦境、回忆、神圣感

### 灯光类型（28）

- 电影灯光 → cinematic lighting〔常用〕　— 像电影镜头那样打光：有明显方向、有明暗层次、暗部不死黑
- 自然光 → natural light〔常用〕　— 太阳或天光，方向随时间变 旧译别名：Natural Light
- 影棚光 → studio lighting〔常用〕　— 灯光被完全控制，背景干净 旧译别名：Studio Light
- 手机屏幕的光 → phone screen light〔常用〕　— 从下往上照脸，冷白
- 钨丝灯 → tungsten〔常用〕　— 暖黄，暗部偏橙
- 闪光灯 → direct flash〔常用〕　— 硬、直接、边缘清晰
- 荧光灯 → fluorescent lighting〔常用〕　— 偏绿偏冷、让人显得疲惫 旧译别名：Fluorescent Lighting
- 霓虹灯 → neon lamp〔常用〕　— 管子的颜色映在墙面和皮肤上 旧译别名：Neon; Neon Lamp
- 聚光灯 → spotlight〔常用〕　— 一束打在主体上，周围压暗 旧译别名：Spotlight
- 舞台灯 → stage spotlight〔常用〕　— 一束追光把主体从黑里拎出来
- 重点照明 → accent lighting〔常用〕　— 在主体上单独打一小束光把它「拎」出来，周围压暗 旧译别名：Accent Lighting
- 三点式照明 → 3-point lighting〔常用〕　— 主光定调＋补光提暗部＋轮廓光勾边，三盏灯各管一件事 旧译别名：3 point lighting
- 柔和照明 → soft lighting〔常用〕　— 反差低、过渡软，人像和生活方式图的默认选择 旧译别名：Soft Lighting
- 低调照明 → low-key lighting〔常用〕　— 画面大部分是暗的，亮部只占一小块，戏剧性最强 旧译别名：Low key lighting
- 高调照明 → high-key lighting〔常用〕　— 画面大部分是亮的，几乎没暗部，干净、轻快、商业感 旧译别名：High key lighting
- 穆迪照明 → moody lighting〔常用〕　— 整体压暗、只留少量亮部，情绪压抑、有故事感 旧译别名：Moody Lighting
- 气氛照明 → atmospheric lighting〔常用〕　— 不为看清主体、只为烘托情绪的辅助光 旧译别名：Atmospheric Lighting
- 环境光 → ambient light〔常用〕　— 没有明确方向、垫底的底光 旧译别名：Ambient Light
- 烛光 → candlelight〔常用〕　— 色温很低，暗部全是暖橙 旧译别名：Candlelight
- 篝火 → firelight〔常用〕　— 光在跳，人物一半亮一半暗
- 月光 → moonlight〔常用〕　— 冷、弱、方向不定
- 阳光直接照射 → direct sunlight〔常用〕　— 影子边缘锐利、方向明确 旧译别名：Direct Sunlight
- 关键照明 → key lighting〔可用〕　— 只靠一盏主光造型，明暗对比强、气氛戏剧化 旧译别名：Key lighting
- 激励照明 → motivated lighting〔可用〕　— 光源在画面里有合理出处（窗、灯、火）
- 双性照明 → bisexual lighting〔可用〕　— 品红＋蓝＋紫三色打光，夜店感的冷艳 旧译别名：Bisexual Lighting
- 音乐会照明 → concert lighting〔可用〕　— 彩色光束从后场扫过 旧译别名：Concert Lighting
- 夜总会照明 → nightclub lighting〔可用〕　— 旧译别名：Nightclub Lighting
- 车灯 → headlights sweeping past〔可用〕　— 一条强光扫过

### 光质（6）

- 硬光 → hard light〔常用〕　— 冷硬、戏剧性、揭示质感与轮廓 旧译别名：Hard Light
- 软光 → soft light〔常用〕　— 柔和、美化、减少瑕疵
- 光比大 → high lighting ratio〔常用〕　— 亮部和暗部的亮度差；光比大＝对比强、戏剧化
- 光比小 → low lighting ratio〔常用〕　— 亮部和暗部的亮度差；光比小＝平、柔和，暗部也留得住细节
- 柔光箱贴着主体 → softbox close in〔常用〕　— 光几乎没有方向
- 反光板补光 → bounce light with a reflector〔可用〕　— 日间外景控光

### 照明风格（5）

- 冷光 → cold light〔常用〕　— 偏蓝青的光，冷静、疏离、科技感 旧译别名：Cold light
- 暖光 → warm light〔常用〕　— 偏橙黄的光，亲密、怀旧、安全 旧译别名：Warm Light
- 色光 → colored light〔常用〕　— 用带颜色的灯打光，一张图里常配两三种互补色 旧译别名：Color Light
- 赛博朋克光 → cyberpunk light〔常用〕　— 霓虹的品红＋青蓝对撞，暗部压深、亮部是彩色光源 旧译别名：Cyberpunk Light
- 均匀平光 → flat even lighting〔常用〕　— 正面均匀打亮、几乎没有阴影，适合角色设定图和产品图

### 影调（5）

- 高反差 → high contrast〔常用〕　— 亮部和暗部都压到极端，中间调很少，硬朗、有力
- 低反差 → low contrast〔常用〕　— 亮暗差别小，整张发灰，柔和但容易显得脏
- 明暗对比 → chiaroscuro〔常用〕　— 靠明暗交界的强烈对比塑造体积 旧译别名：Chiaroscuro
- 暗部留住细节 → shadows holding detail〔常用〕　— 暗的地方还能看出形状和层次，不是一整块黑
- 高光留住细节 → highlights holding detail〔常用〕　— 最亮的地方还能看出纹理，不是一片白

> B · 光效

### 光线效果（22）

- 边缘光 → edge light〔常用〕　— 从侧后方打的一道窄光，只勾出主体的边，用来把主体从背景里「切」出来 旧译别名：Edge light
- 发光边 → glowing rim〔常用〕　— 轮廓外面有一圈柔和的亮光，把主体从背景里拎出来
- 强边缘光 → strong rim light〔常用〕
- 荧光 → glowing light〔常用〕　— 物体自己发出柔和的光 旧译别名：Fluorescence
- 发光 → glowing〔常用〕　— 光源周围有一圈扩散的亮晕 旧译别名：Shine
- 生物发光 → bioluminescent〔常用〕　— 生物自己发光，多为青绿或幽蓝
- 温暖光辉 → warm glow〔常用〕　— 旧译别名：Warm Glow
- 柔和主光配清晰边缘光和自然的接触阴影 → soft key light with a crisp rim light and a natural contact shadow〔常用〕　— 棚拍三件套一起写，缺一个就像渲染图
- 深色底配一个荧光强调色 → a dark ground with one fluorescent accent〔常用〕
- 发光眼睛 → glowing eyes〔可用〕
- 闪闪发光的瞳孔 → sparkling pupils〔可用〕
- 微光 → shimmering light〔可用〕　— 旧译别名：Rays of Shimmering Light
- 明亮高光 → bright highlights〔可用〕　— 旧译别名：Bright Highlights
- 仙气缭绕 → ethereal mist〔可用〕　— 雾状光晕，适合仙侠与神话题材 旧译别名：Ethereal Mist
- 电光闪烁 → electric flash〔可用〕　— 旧译别名：Electric Flash
- 黑光 → blacklight〔可用〕　— 紫外灯下荧光物质发亮 旧译别名：Blacklight
- 紫外线 → ultraviolet〔可用〕　— 旧译别名：Ultraviolet
- 荧光棒 → glow stick〔可用〕　— 旧译别名：Glow-stick
- 频闪灯 → strobe light〔可用〕　— 旧译别名：Strobe light
- 放射性发光 → radioactive glow〔可用〕　— 危险的青绿色自发光
- 熔岩的光芒 → lava glow〔可用〕　— 橙红自下而上的热光 旧译别名：Lava Glow
- 核废料的光芒 → nuclear waste glow〔可用〕　— 诡异的黄绿 旧译别名：Nuclear Waste Glow

### 体积光（6）

- 体积光 → volumetric light〔常用〕　— 光被介质挡住一部分，现出一条条可见的光路 旧译别名：Volumetric light/Volume Method
- 光柱 → light shafts through mist〔常用〕　— 光穿过雾气形成一道道光柱
- 空气里的浮尘 → dust motes in the light〔常用〕　— 光柱里的尘埃颗粒被照亮，画面有颗粒感
- 丁达尔效应 → tyndall effect〔常用〕　— 光穿过雾、烟或胶体时现出光路，就是常说的「耶稣光」
- 逆光下的蒙蒙亮 → backlit haze〔常用〕　— 空气本身被照亮，整片发亮发白
- 细密水雾散光 → fine spray scattering〔可用〕　— 水雾把光打散，没有明确光路，只有一片柔亮

> C · 环境

### 时间（13）

- 黄金时刻 → golden hour〔常用〕　— 日出后、日落前那一小段，太阳很低、光呈金色，人像和风景最常用
- 蓝调时刻 → blue hour〔常用〕　— 太阳刚落或将升的那段，天是深蓝的，和暖色的人造光对比很好看
- 清晨 → early morning〔常用〕　— 天刚亮，空气里有一层薄雾
- 晨光 → morning light〔常用〕　— 太阳刚出来那阵，光偏暖、角度低、影子长 旧译别名：Morning Light
- 正午顶光 → noon light from straight above〔常用〕　— 太阳在正上方，影子几乎踩在脚下、边缘锐利
- 黄昏 → late afternoon〔常用〕　— 太阳压得很低，一切镀上金边
- 日落 → sunset〔常用〕　— 太阳正在落下，光金黄、云被染红
- 夜晚 → night〔常用〕　— 天已全黑，靠人造光源照亮
- 深夜 → deep night〔常用〕　— 环境全暗，只有一盏灯把主体拎出来
- 日出前后的十分钟 → the ten minutes around sunrise〔可用〕　— 太阳在地平线附近，天从粉过渡到紫，色温变化最快的一小段
- 凌晨 → pre-dawn〔可用〕　— 日出前那段，光是冷青灰色，低对比、很安静
- 硬光打出一块明确的影子，像正午 → hard light throwing one definite shadow〔可用〕
- 清晨或傍晚的自然光 → early morning or late afternoon natural light〔可用〕　— 户外场景产品

### 天气（17）

- 晴天 → clear sky〔常用〕　— 通透的蓝天，光有明确方向，影子颜色偏蓝
- 多云 → cloudy〔常用〕　— 云层遮住太阳，光是漫射的、方向不明显
- 阴天 → overcast〔常用〕　— 云把太阳整个盖住，光是漫射的、几乎没有影子
- 雾 → fog〔常用〕　— 空气里悬浮着小水滴，远处的东西变淡、变灰
- 雾天的光被漫射开 → fog diffusing the light〔常用〕　— 雾把光散开，远处的景物一层层变淡
- 细雨 → light rain〔常用〕　— 雨很细，逆光下能看见一丝一丝的雨
- 大雨 → heavy rain〔常用〕　— 雨很大，雨线连成一片、地面溅起水花
- 雨天 → rainy day〔常用〕　— 在下雨，空气湿、地面反光 旧译别名：rain; rainy days
- 雨后初晴 → just after rain〔常用〕　— 雨刚停，空气干净，颜色饱和、锐度高
- 暴风雨 → thunderstorm〔常用〕　— 风雨交加，云很厚很黑 旧译别名：thunderstorms
- 闪电 → lightning〔常用〕　— 天空里一道分叉的强光
- 小雪 → light snow〔常用〕　— 雪很小，只稀疏地飘几片
- 大雪 → heavy snow〔常用〕　— 雪片很大，被光一照像在翻飞
- 雪后反光 → snow bouncing light from below〔常用〕　— 雪地把光反射上来，下巴和眼窝被从下往上补亮
- 沙尘天气 → dust turning the light orange〔常用〕　— 空气里全是沙尘，光被滤成橙黄，太阳变成一个可直视的圆盘
- 梦幻雾气 → dreamy haze〔可用〕　— 比雾更柔、更亮，像做梦 旧译别名：Dreamy Haze
- 暴雨前的闷光 → the flat glare before a storm〔可用〕　— 暴雨将至，云很低很重、光发闷、色温偏绿灰

## 通用-色彩材质

> A · 色彩

### 基础色（16）

- 红 → red〔常用〕　— 旧译别名：Red
- 橙 → orange〔常用〕　— 旧译别名：Orange
- 黄 → yellow〔常用〕　— 旧译别名：Yellow
- 绿 → green〔常用〕　— 旧译别名：Green
- 青 → cyan〔常用〕　— 蓝绿之间的颜色，中文里既可指蓝也可指绿（如「青天」「青草」） 旧译别名：Cyan
- 蓝 → blue〔常用〕　— 旧译别名：Blue
- 紫 → purple〔常用〕　— 旧译别名：Purple
- 粉 → pink〔常用〕　— 介于红和洋红之间，最常见的柔色
- 棕 → brown〔常用〕　— 旧译别名：Brown
- 灰 → grey〔常用〕　— 旧译别名：Gray
- 黑 → black〔常用〕　— 旧译别名：Black
- 白 → white〔常用〕　— 旧译别名：White
- 金 → gold〔常用〕　— 金属感的黄，靠反光和明暗表现
- 银 → silver〔常用〕　— 金属感的灰白，比灰更亮、带反光
- 炭色 → charcoal grey〔常用〕　— 接近黑的深灰，比纯黑柔和、不死板
- 青绿色 → teal〔常用〕　— 蓝绿的中间色，像孔雀石或浅海

### 经典色（11）

- 克莱因蓝 → Klein blue〔常用〕　— 法国艺术家克莱因注册的「国际克莱因蓝」，极高纯度的群青，几乎发光 旧译别名：Klein Blue
- 中国红 → Chinese red〔常用〕　— 带一点橙的正红，传统喜庆色 旧译别名：Chinese Red
- 普鲁士蓝 → Prussian blue〔常用〕　— 十八世纪德国发明的深蓝颜料，偏冷的暗蓝
- 祖母绿 → emerald〔常用〕　— 浓艳的绿，带一点蓝
- 酒红 → burgundy〔常用〕　— 深红带紫，像红酒
- 玫瑰金 → rose gold〔常用〕　— 粉调的金属金，柔和、偏女性化
- 象牙白 → ivory〔常用〕　— 带一点黄的暖白，比纯白柔和
- 奶茶色 → milk tea〔常用〕　— 米白到浅棕的一组暖中性色，温柔、甜而不腻
- 丹宁蓝 → denim blue〔常用〕　— 牛仔布的靛蓝，从浅到深，日常、耐看
- 孔雀绿 → peacock green〔可用〕　— 像孔雀羽毛的蓝绿，深沉华贵 旧译别名：Peacock Green
- 只此青绿 → turquoise green〔可用〕　— 出自舞蹈诗剧《只此青绿》，从《千里江山图》取的青绿 旧译别名：Turquoise color

### 色彩属性（18）

- 灰度 → greyscale〔常用〕　— 只有黑到白的深浅，没有颜色
- 黑白 → black and white〔常用〕　— 只保留明暗，去掉所有颜色 旧译别名：Black and white
- 单色 → monotone〔常用〕　— 整张只有一个色相，靠明度变化 旧译别名：Monotone
- 明亮色 → bright〔常用〕　— 整体偏亮的配色
- 彩色的 → colorful〔常用〕　— 正常上色，不做黑白处理
- 鲜艳的 → vivid colors〔常用〕　— 高饱和、高识别度的颜色
- 甜 → soft pastel〔常用〕　— 高明度低饱和，清透
- 高饱和 → saturated〔常用〕　— 颜色尽量不掺灰，鲜艳、抢眼 旧译别名：High saturation
- 低饱和 → desaturated〔常用〕　— 颜色都掺灰，柔和、耐看、高级
- 淡色调 → tints〔常用〕　— 高明度低饱和，清淡、透气
- 颜色怀旧的 → nostalgia〔常用〕　— 低饱和、偏黄或偏青，像旧照片
- 互补色对撞 → complementary colors〔常用〕　— 色环上正对的两个颜色各占一半，强烈、有张力
- 三色均衡 → three colours at 60/30/10〔常用〕　— 三个颜色按 60/30/10 分配，主色定调、点缀色提神
- 强对比配色 → strong contrasting colours〔常用〕　— 演出／派对海报
- 两色系统 → a two-colour system〔常用〕　— 一深一浅
- 多色彩搭配 → multi color〔可用〕　— 四种以上的颜色同时出现，热闹但要控住比例 旧译别名：Multi color matching
- 高饱和撞色 → high-saturation clash〔可用〕　— 故意用不协调的高饱和颜色对撞，做出冲击或廉价感
- 琥珀色调 → amber tone〔可用〕　— 像琥珀一样的暖黄棕，怀旧、温暖 旧译别名：Amber

### 配色方案（27）

- 莫兰迪色系 → Morandi palette〔常用〕　— 所有颜色都掺了灰，低饱和、安静、高级 旧译别名：Morandi color scheme
- 马卡龙色系 → macaron palette〔常用〕　— 高明度低饱和的甜色（粉、薄荷、鹅黄）
- 糖果色系 → candy palette〔常用〕　— 高饱和高明度的甜色，像水果硬糖 旧译别名：Candy
- 大地色系 → earth tones〔常用〕　— 土黄、赭石、橄榄、砖红这一组，自然、耐看
- 日暮色系 → sunset palette〔常用〕　— 紫、橙、粉的过渡色，像黄昏的天空 旧译别名：Sunset color system
- 秋日棕色系 → autumn brown〔常用〕　— 秋天落叶的棕黄 旧译别名：Autumn Brown
- 柔和粉色系 → soft pink〔常用〕　— 低饱和的粉，温柔 旧译别名：Soft Pink
- 薄荷绿 → mint green〔常用〕　— 浅绿带一点蓝，清凉
- 珊瑚色 → coral〔常用〕　— 粉和橙交界的暖色，活泼但不刺眼
- 紫罗兰 → violet〔常用〕　— 偏蓝的紫
- 土耳其蓝 → turquoise〔常用〕　— 土耳其石那种蓝绿，异域感
- 霓虹色调 → neon accents〔常用〕　— 品红＋青蓝的高饱和霓虹配色，赛博感 旧译别名：Neon Accents
- 黑金色调 → gold and black〔常用〕　— 大面积黑＋金色点缀，奢华感 旧译别名：Gold and black tone
- 红黑色调 → red and black〔常用〕　— 红加黑，强烈、危险、有力量 旧译别名：Red and black tone
- 敦煌色系 → Dunhuang palette〔常用〕　— 敦煌壁画取色：土红、石青、赭石、金，厚重沉稳 旧译别名：Dunhuang color system
- 孟菲斯色系 → Memphis palette〔常用〕　— 八十年代孟菲斯设计小组：高饱和撞色＋几何图形 旧译别名：Memphis color scheme
- 蒙德里安色系 → Mondrian palette〔常用〕　— 红黄蓝三原色＋黑白灰，来自蒙德里安的格子画 旧译别名：Mondrian color scheme
- 韦斯·安德森式的配色 → Wes Anderson palette〔常用〕　— 高饱和的粉黄蓝绿，对称、平面、刻意
- 米白纸底配赤陶橙与墨绿 → cream paper with terracotta and deep green〔常用〕
- 纯黑纯白加一个信号色 → pure black and white with one signal colour〔常用〕
- 低饱和的胶片褪色感 → faded desaturated film look〔常用〕
- 鲜果色系 → fresh fruit palette〔可用〕　— 柑橘、莓果那种鲜亮多汁的颜色，清爽 旧译别名：Fresh fruit color scheme
- 枫叶红 → maple red〔可用〕　— 秋天枫叶的橙红
- 雪山蓝 → snow mountain blue〔可用〕　— 高原天空那种冷而透的蓝
- 马蒂斯色系 → Matisse palette〔可用〕　— 野兽派马蒂斯：高饱和平涂色块，大胆、装饰性强 旧译别名：Matisse color scheme
- 洛可可色系 → rococo palette〔可用〕　— 十八世纪法国宫廷风：粉、薄荷绿、金，甜腻繁复 旧译别名：ROCOCO
- 冷调单色打底 → a cold monochrome base〔可用〕　— 整体冷灰，只在关键处给一点暖

### 配色方法（6）

- 橙蓝分离 → orange and teal〔常用〕　— 暖橙的主体压在冷蓝的环境里；注意别让肤色变橙
- 漂白旁路 → bleach bypass〔常用〕　— 把漂白步骤跳过，饱和度降低但对比保留，画面发灰发狠
- 单色相不同明度 → a single hue separated only by value〔常用〕　— 整张只有一个颜色，靠深浅区分层次，最稳的配色法
- 一点亮色打破整体的灰 → one bright accent in an all-grey field〔常用〕　— 整张低饱和，只留一个鲜艳的颜色当视觉落点
- 大面积留白 → mostly empty〔常用〕　— 只在关键处上色
- 渐变只用在背景 → gradient only in the background〔可用〕　— 前景元素保持单色

> B · 材质

### 材料（44）

- 玻璃 → glass〔常用〕　— 旧译别名：Glass
- 陶瓷 → ceramic〔常用〕　— 高温烧制的陶或瓷，硬、有釉 旧译别名：Ceramic
- 大理石 → marble〔常用〕　— 白色基底带灰或金的纹路，高档、冷感
- 清水混凝土 → fair-faced concrete〔常用〕　— 拆模后不加任何装饰的混凝土，留着模板缝和螺栓孔
- 不锈钢 → stainless steel〔常用〕　— 工业感、现代感，反光清楚
- 黄铜 → brass〔常用〕　— 比金色沉稳，用久了会有包浆
- 古铜 → antique bronze〔常用〕　— 氧化后的铜，暗棕带绿锈
- 铜 → bronze〔常用〕
- 铝合金 → aluminum〔常用〕　— 旧译别名：Aluminum
- 碳纤维 → carbon fiber〔常用〕　— 黑色编织纹理，又轻又硬，运动感、科技感 旧译别名：Carbon Fiber
- 耐候钢 → weathering steel〔常用〕　— Corten 钢：特意让它生锈，锈层反而保护内部，颜色是深锈红
- 石材 → stone〔常用〕
- 砂岩 → sandstone〔常用〕　— 颗粒感明显的沉积岩，粗糙、暖色 旧译别名：Sandstone
- 砖块 → brick〔常用〕　— 旧译别名：Brick
- 钻石 → diamond〔常用〕　— 旧译别名：Diamond
- 松木 → pine〔常用〕　— 浅色、木纹清楚、有节 旧译别名：Pine
- 木制的 → wooden〔常用〕　— 旧译别名：Wooden
- 布料 → fabric〔常用〕　— 旧译别名：Fabric
- 亚麻布 → linen〔常用〕　— 天然纤维，有粗细不匀的横竖纹理 旧译别名：Linen
- 棉质 → cotton〔常用〕　— 旧译别名：Cotton texture
- 天鹅绒 → velvet〔常用〕　— 绒面深、吸光，颜色显得浓 旧译别名：Velvet
- 缎面 → satin〔常用〕　— 像缎子一样，反光柔和、有丝绸的垂感 旧译别名：Satin
- 蕾丝 → lace〔常用〕　— 镂空的花纹网眼 旧译别名：Lace
- 皮革 → leather〔常用〕　— 旧译别名：Leather
- 纸张 → paper〔常用〕　— 旧译别名：Paper
- 宣纸 → xuan paper〔常用〕　— 中国书画用纸，吸水、有纤维感
- 珐琅 → enamel〔常用〕　— 在金属上烧一层玻璃质釉，颜色鲜艳、表面光硬 旧译别名：Enamel
- 塑胶 → plastic〔常用〕　— 旧译别名：Plastic
- 箔 → foil〔常用〕　— 极薄的金属膜，反光刺眼、有折痕 旧译别名：Foil
- 氧化黄铜 → oxidised brass〔可用〕　— 黄铜氧化后的样子，暗金里泛绿，有年头感
- 镍 → nickel〔可用〕　— 冷银色金属，比铬柔
- 竹钢 → densified bamboo〔可用〕　— 把竹条浸胶高压成型，硬度接近钢，色深
- 玄武岩 → basalt〔可用〕　— 深灰近黑、有细密气孔 旧译别名：Basalt
- 石英 → quartz〔可用〕　— 半透明、有冷光 旧译别名：Quartz
- 紫水晶 → amethyst〔可用〕　— 紫色的透明晶体，有内反射 旧译别名：Amethyst
- 乌木 → ebony〔可用〕　— 极黑的硬木，密度大、几乎看不出纹理 旧译别名：Ebony
- 纱线 → yarn〔可用〕　— 纺成的线，能看见纤维的捻向 旧译别名：Yarn
- 尼龙 → nylon〔可用〕　— 旧译别名：Nylon
- 纸板 → cardboard〔可用〕　— 旧译别名：Cardboard
- 薄纸巾 → tissue paper〔可用〕　— 旧译别名：Tissue paper
- 光纤 → fiber optic〔可用〕　— 旧译别名：FiberOptic
- 腐朽衰败的 → decayed〔可用〕　— 长了霉斑、起了皮的材料 旧译别名：Decayed
- 骨骼状 → skeletal〔可用〕　— 旧译别名：Skeletal
- 菌丝 → mycelium〔少见〕　— 菌丝长成的有机材料，浅色、多孔 旧译别名：Mycelium

### 表面质感（41）

- 金属质感 → metallic〔常用〕　— 有金属的反射和明暗对比 旧译别名：Metallic texture
- 拉丝 → brushed〔常用〕　— 表面有平行的方向性纹理，反光被拉长 旧译别名：Brushed
- 抛光 → polished〔常用〕　— 把表面磨到像镜子一样亮 旧译别名：High polished
- 高光洁度 → high polish〔常用〕　— 像镜子一样光滑，能反射出周围环境的形状
- 镜面高光 → specular highlight〔常用〕　— 光滑表面上那一点又小又亮的反光，位置固定、边缘利落
- 磨砂 → frosted〔常用〕　— 表面被打磨成细小颗粒，透光但不透形
- 磨砂玻璃 → frosted glass〔常用〕　— 玻璃被打磨成哑面，光能进来但看不清后面
- 喷砂 → sandblasted〔常用〕　— 高压砂粒打出的均匀哑面 旧译别名：Sandblasted
- 哑光 → matte〔常用〕　— 不反光，表面只有暗淡的反射 旧译别名：Matte
- 绒面 → suede〔常用〕　— 有细密绒毛的表面，反光是散开的
- 毛绒质感 → fluffy〔常用〕　— 表面立着细密的绒毛，反光散开 旧译别名：Fluffy texture
- 皮毛质感 → fur texture〔常用〕　— 动物毛皮，有方向和深浅变化 旧译别名：Fur texture
- 针织质感 → knitted〔常用〕　— 毛线织出来的，有针脚的凹凸
- 绸缎质感 → silk texture〔常用〕　— 反光柔和、有方向和垂感 旧译别名：Silk texture
- 珠光质感 → pearl luster〔常用〕　— 反光柔和且带一点颜色偏移 旧译别名：Pearl luster texture
- 玻璃质感 → glass texture〔常用〕　— 透明、有厚度感，边缘会折射 旧译别名：Glass texture
- 水晶质感 → crystal texture〔常用〕　— 透明且折射强，内部有光路 旧译别名：Crystal texture
- 半透明 → translucent〔常用〕　— 光能透过去，但看不清后面的东西
- 透明质感 → clear transparency〔常用〕　— 边缘清晰
- 玻璃的通透与厚边的绿 → clear glass with the green of a thick edge〔常用〕　— 玻璃透光，但厚的地方会泛出青绿色
- 塑料质感 → plastic texture〔常用〕　— 表面均匀、反光软，没有材质肌理 旧译别名：Plastic texture
- 皮革质感 → leather texture〔常用〕　— 旧译别名：Leather texture
- 皮革的毛孔与压线 → leather grain and stitching〔常用〕
- 镀铬 → chrome〔常用〕　— 表面像镜子一样反光，周围环境被完整映出来
- 金属漆质感 → metallic paint〔常用〕　— 油漆里掺了金属粉，有细密的闪烁颗粒 旧译别名：Metallic paint texture
- 雕刻质感 → carved texture〔常用〕　— 表面有刻出来的凹凸，靠阴影成型 旧译别名：Carved texture
- 竹子质感 → bamboo texture〔常用〕　— 有节、有纵向纤维的浅色硬质 旧译别名：Bamboo texture
- 织物纹理 → warp and weft〔常用〕　— 能看见经纬的交织
- 湿润的表面 → moist〔常用〕　— 表面挂着一层水膜，反光被拉长
- 表面凝结着细密的水珠 → fine beads of condensation〔常用〕　— 低温表面挂的一层细密水珠
- 油光在表面形成亮点 → specular highlights from the oil〔常用〕　— 油膜把光聚成小亮点
- 高光过渡 → highlight rolloff〔常用〕　— 亮部到中调过渡柔和、不过曝
- 真实的反射 → genuine reflections〔常用〕
- 水面倒影 → water reflection〔常用〕
- 露珠 → dew drops〔常用〕
- 皮肤是哑光的 → matte skin〔常用〕　— 只有高光处反光，不是整片油光
- 褶皱质感 → wrinkled〔可用〕　— 表面布满不规则的折痕
- 内部折射 → internal refraction〔可用〕　— 透明物体内部的光线弯折，出现亮线和错位
- 油漆质感 → paint texture〔可用〕　— 刷过漆的表面，有刷痕或厚薄 旧译别名：Paint texture
- 水波纹质感 → water ripple〔可用〕　— 表面像水面一样有同心或平行的波纹 旧译别名：Water wave texture
- 石墨质感 → graphite texture〔可用〕　— 铅笔那种灰黑色带金属反光 旧译别名：Graphite texture

## 通用-镜头构图

> A · 取景

### 景别（28）

- 极限特写 → extreme close-up〔常用〕　— 比特写还近，只留眼睛或嘴这样的局部 旧译别名：Extreme Close-Up
- 脸部特写 → detail shot (ECU)〔常用〕　— 只拍脸，背景几乎看不到，情绪最直接 旧译别名：Face Shot (VCU)
- 头部特写 → headshot〔常用〕　— 从头顶到下巴，比脸部特写略松一点 旧译别名：Headshot
- 头部以上 → big close-up (BCU)〔常用〕　— 头顶到画面上边还留一点空间 旧译别名：Big Close-Up (BCU)
- 胸部以上 → medium close-up (MCU)〔常用〕　— 旧译别名：Chest Shot (MCU)
- 腰部以上 → waist shot〔常用〕　— 旧译别名：Waist Shot(WS)
- 七分身 → three-quarter shot〔常用〕　— 影视里最常用的对话景别，能同时看清表情和手势
- 膝盖以上 → knee shot〔常用〕　— 旧译别名：Knee Shot (KS)
- 全身 → full length shot〔常用〕　— 旧译别名：Full Length Shot(FLS)
- 半身像 → bust〔常用〕　— 旧译别名：Bust Portrait
- 肖像 → portrait〔常用〕
- 中景 → medium shot (MS)〔常用〕　— 旧译别名：Medium Shot(MS)
- 中远景 → medium long shot (MLS)〔常用〕　— 旧译别名：Medium Long Shot(MLS)
- 宽景 → wide view〔常用〕　— 旧译别名：Wide view
- 景观 → an expansive view〔常用〕　— 一片完整的环境，主体在其中 旧译别名：An expansive view of
- 全景照片 → panorama〔常用〕　— 超宽画幅、能看到大片环境 旧译别名：Panorama
- 超广角 → ultra wide shot〔常用〕　— 比广角更极端，画面边缘明显变形，适合拍空间和冲击力 旧译别名：Ultra-wide shot
- 微距 → macro shot〔常用〕　— 凑到极近拍，能看到肉眼看不到的纹理 旧译别名：Macro shot
- 两景 → two shot〔常用〕　— 画面里正好两个人，多用于对话戏
- 群景 → group shot〔常用〕　— 一群人全在画面里，看清谁站哪儿
- 俯拍平铺 → flat-lay from above〔常用〕　— 相机在正上方垂直向下，像把东西摊在桌上拍
- 人占四分之三 → long shot〔可用〕　— 主体占画面约四分之三，留一点空间但不空
- 人在远方 → extra long shot (ELS)〔可用〕　— 人很小，环境为主 旧译别名：Extra Long Shot (ELS)
- 微观 → microscopic view〔可用〕　— 显微镜级别的放大
- 松散景 → loose shot〔可用〕　— 画面留很多余地，主体不占满，呼吸感强
- 近距离景 → tight shot〔可用〕　— 画框卡得很紧
- 三景 → three shot〔可用〕　— 画面里正好三个人
- 横截面图 → cross-section view〔可用〕　— 旧译别名：a cross-section view of (a walnut)

### 视角（30）

- 平视 → eye-level〔常用〕　— 相机与视线等高，最平实、最不带评价
- 正面 → front view〔常用〕　— 正对着主体，最直接、最对称 旧译别名：Front view
- 侧面 → profile〔常用〕　— 从侧面拍，能看清轮廓线 旧译别名：Profile
- 侧视图 → side view〔常用〕
- 背视图 → back view〔常用〕
- 仰视 → look up〔常用〕　— 从下往上看，被拍的人显得强大、有压迫感 旧译别名：Up view
- 俯视 → top view〔常用〕　— 从上往下看，被拍的人显得弱小、被观察 旧译别名：Top view
- 水平视角 → horizontal view angle〔常用〕
- 四十五度斜俯 → a 45-degree downward angle〔常用〕　— 最常用的一档
- 鸟瞰图 → aerial view〔常用〕　— 从很高的地方往下看，能看到大片地面布局 旧译别名：Aerial view
- 等距视角 → isometric〔常用〕　— 没有透视的近失，所有平行线保持平行
- 交错视角 → Dutch angle〔常用〕　— 画面刻意歪斜，制造不安 旧译别名：Dutch Angle
- 肩膀视角 → over the shoulder〔常用〕　— 越过一个人的肩膀拍另一个人，带出两者关系 旧译别名：Over the shoulder
- 第一人称视角 → first-person view〔常用〕　— 镜头就是角色的眼睛，代入感最强
- 第三人称视角 → third-person perspective〔常用〕　— 镜头在角色之外观察，观众是旁观者
- 产品视图 → product view〔常用〕
- 平视（与标签等高） → a level angle at label height〔常用〕　— 产品图常用
- 看向观众 → looking at viewer〔常用〕　— 主体直视镜头，打破第四面墙，有交流感
- 电影角度 → cinematic angle〔常用〕　— 像电影镜头那样取景：有意识的角度、不追求「拍全」
- 摄影机对准人物的视线 → camera on the eyeline〔常用〕　— 视角谱系的高认同端
- 摄影机偏离视线四十五度 → camera 45 degrees off the eyeline〔常用〕　— 最常用的叙事视角
- 卫星视图 → satellite view〔可用〕　— 垂直向下、接近地图的读法
- 底视图 → bottom view〔可用〕　— 旧译别名：Bottom view
- 反转视角 → reverse angle〔可用〕　— 旧译别名：Reverse angle
- 自由视角 → free camera〔可用〕　— 旧译别名：Free camera
- 固定视角 → fixed camera〔可用〕　— 旧译别名：Fixed camera
- 跟随视角 → follow camera〔可用〕　— 旧译别名：Follow camera
- 随意视角 → arbitrary view〔可用〕　— 旧译别名：Arbitrary view
- 摄影机离视线更远 → camera far off the eyeline〔可用〕　— 中立旁观，认同感最低
- 内视镜视角 → endoscopic view〔少见〕　— 旧译别名：Endoscopic view

### 设定图与多视图（8）

- 角色设定图 → character design sheet〔常用〕
- 角色三视图 → character turnaround sheet〔常用〕
- 角色四视图 → character four-view sheet〔常用〕
- 三视图站姿 → three-view neutral stance〔常用〕　— 三个角度都用同一个中性站姿，方便比对
- 前视、侧视、后视图 → front, side, rear view〔常用〕　— 旧译别名：Front, Side, Rear View
- 面部特写格 → face close-up panel〔常用〕　— 多视图里单开一格画头部特写
- 立绘 → character illustration〔常用〕　— 单人、全身、姿态讲究
- 转面图 → character turnaround〔常用〕

> B · 构图

### 构图（28）

- 三分法 → rule of thirds〔常用〕　— 把画面横竖各分三等份，主体放在交叉点或线上，最稳的构图法 旧译别名：Rule of Thirds
- 黄金分割 → golden ratio〔常用〕　— 按 1:1.618 切分画面，比三分法更「自然」的比例 旧译别名：Golden Ratio
- 中心构图 → centered composition〔常用〕　— 旧译别名：Centered composition
- 对称构图 → symmetrical composition〔常用〕　— 旧译别名：Symmetrical composition
- 非对称构图 → asymmetrical composition〔常用〕　— 旧译别名：Asymmetrical composition
- 对角线构图 → diagonal composition〔常用〕　— 旧译别名：Diagonal composition
- 水平线构图 → horizontal line composition〔常用〕　— 旧译别名：Horizontal line composition
- 横向构图 → horizontal composition〔常用〕　— 画面横向展开，适合风景和群像 旧译别名：Horizontal composition
- 三角构图 → triangular composition〔常用〕　— 三点连成三角形，画面最稳；倒三角则制造不稳定
- S 形构图 → S-shaped composition〔常用〕　— 主体或引导线走成 S 形，视线顺着走完全图
- 引导线 → leading lines〔常用〕　— 用画面里的线条（路、栏杆、光）把视线引向主体 旧译别名：Leading Lines
- 消失点构图 → vanishing point composition〔常用〕　— 所有线条朝一个点收拢，纵深和空间感最强 旧译别名：Vanishing point composition
- 框架式构图 → frame composition〔常用〕　— 用门、窗、树枝等在前景框住主体，做出纵深 旧译别名：Frame composition
- 负空间构图 → negative space composition〔常用〕　— 主体周围留大片空白，靠「空」突出主体
- 焦点构图 → focal point composition〔常用〕　— 把最亮或最清楚的一点放在关键位置，视线自然落过去 旧译别名：Focal point composition
- 重复构图 → repetition composition〔常用〕　— 同样的形状反复出现，形成节奏 旧译别名：Repetition composition
- 重叠构图 → overlapping composition〔常用〕　— 前后物体相互遮挡，靠遮挡关系表达层次 旧译别名：Overlapping composition
- 遮挡构图 → blocking composition〔常用〕　— 用前景的物体挡住一部分主体，制造层次和窥视感 旧译别名：Blocking composition
- 对比构图 → contrast composition〔常用〕　— 把两个相反的东西并置（大／小、明／暗、冷／暖） 旧译别名：Contrast composition
- 布景构图 → mise-en-scene〔常用〕　— 场景里的每样东西都为叙事服务 旧译别名：Mise-en-scene composition
- 并列构图 → juxtaposition〔可用〕　— 把两件不相关的东西并排放，靠反差说话 旧译别名：Juxtaposition composition
- 散点构图 → scattered composition〔可用〕　— 旧译别名：Scattered composition
- 剪影构图 → cut out composition〔可用〕　— 主体压成黑色轮廓，形状本身成为主体 旧译别名：Cut out composition
- 径向构图 → radial composition〔可用〕　— 元素从中心向外辐射，视线被拉向圆心 旧译别名：Radial composition
- 动态对称 → dynamic symmetry〔可用〕
- 分割互补构图 → split complementary composition〔可用〕　— 旧译别名：Split complementary composition
- 拼贴构图 → collage composition〔可用〕　— 把不相关的画面拼在一张里，打破单一空间 旧译别名：Collage composition
- 线条构图 → line composition〔可用〕　— 旧译别名：Line composition

### 透视（6）

- 一点透视 → one-point perspective〔常用〕　— 正对着走廊、马路、铁轨拍；最基础也最有力的纵深做法
- 两点透视 → two-point perspective〔常用〕　— 两个消失点，像站在街角看建筑的两个面
- 三点透视 → three-point perspective〔常用〕　— 三个消失点，多加一个垂直方向的，俯仰看高楼用 旧译别名：Three-point perspective
- 立面透视 → elevation perspective〔常用〕　— 正对建筑的一个面拍，透视被压平、线条横平竖直 旧译别名：Elevation perspective
- 空气透视 → aerial perspective〔常用〕　— 远景一层层变淡、变蓝，画远景必备
- 广角变形 → wide-angle distortion〔常用〕　— 24mm 以下明显；靠近画面边角的脸和物体都会变形

> C · 光学

### 焦距（16）

- 鱼眼镜头 → fisheye lens〔常用〕　— 视野接近甚至超过 180°，画面四周拉成圆弧 旧译别名：fish eye lens
- 广角镜头 → wide-angle lens〔常用〕　— 通常指焦距小于 35mm 的镜头，可捕捉更广阔的场景 旧译别名：Wide-angle lens
- 长焦镜头 → telephoto lens〔常用〕　— 通常指焦距大于 70mm 的镜头，可拍摄远距离的主体 旧译别名：Telephoto lens
- 微距镜头 → macro lens〔常用〕　— 可拍摄极其细小的主体，通常有 1:1 的放大倍率 旧译别名：Macro lens
- 定焦镜头 → prime lens〔常用〕　— 旧译别名：Prime lens
- 长焦压缩 → telephoto compression〔常用〕　— 200mm 以上明显；前后景像贴在同一个平面上
- 二十四毫米 → 24mm〔常用〕　— 空间感和冲击力强，靠近边缘的物体会被拉长
- 三十五毫米 → 35mm〔常用〕　— 略广但不夸张，街头和纪实最常用
- 五十毫米 → 50mm〔常用〕　— 最接近人眼看到的比例，不变形、最自然
- 八十五毫米 → 85mm〔常用〕　— 脸不容易变形，背景压缩柔和；对人像最有效
- 一百毫米微距 → 100mm macro〔常用〕　— 退得够远不挡光
- 镜头贴近，浅景深 → shot close with shallow depth of field〔常用〕　— 材质微距
- 移轴镜头 → tilt-shift lens〔可用〕　— 镜头能平移或倾斜，把真实场景拍出「微缩模型」的错觉 旧译别名：Tilt-shift lens
- 变焦镜头 → zoom lens〔可用〕　— 旧译别名：Zoom lens
- 一百三十五毫米 → 135mm〔可用〕　— 背景压得更扁、虚化更浓，主体更突出
- 两百毫米以上 → 200mm and beyond〔可用〕　— 前后景几乎贴在一起，背景化成一片

### 光圈（7）

- f/1.4 → f/1.4〔常用〕　— 景深很浅、焦外光斑很大很圆
- f/1.8 → f/1.8〔常用〕　— 便宜定焦的常见规格，虚化够用、画质比全开好一档
- f/2.8 → f/2.8〔常用〕　— 虚化明显但主体还在焦内，工作和生活照的常用档
- f/5.6 → f/5.6〔常用〕　— 多数镜头收两档后最锐，同时还留一点虚化
- f/8 → f/8〔常用〕　— 从前景到背景基本都清楚，风光和产品的常用档
- f/1.2 → f/1.2〔可用〕　— 只有眼睛那一层清楚，其余全化开
- f/16 → f/16〔可用〕　— 整张都锐，但可能出现衍射导致画质下降

### 焦外（11）

- 背景虚化 → shallow depth of field bokeh〔常用〕　— 旧译别名：Bokeh
- 奶油一样化开的焦外 → creamy, fully dissolved bokeh〔常用〕　— 虚化的背景过渡极其柔和，没有硬边
- 圆形的光斑 → round bokeh balls〔常用〕　— 虚化出来的光点是正圆的
- 前景 → foreground〔常用〕　— 靠近镜头、通常被虚化的一层元素，用来做纵深
- 前后景同时虚化 → foreground and background both soft〔常用〕　— 只有主体实
- 背景完全融成一片色块 → the background melted into flat colour〔常用〕
- 猫眼焦外 → cat's-eye bokeh〔可用〕　— 画面边缘的光点被镜头口径挡住，压成橄榄形
- 旋焦 → swirl bokeh〔可用〕　— 焦外的光斑沿一个方向旋转，画面有眩晕感（老镜头特征）
- 焦外像水彩一样晕开 → bokeh dissolving like watercolour〔可用〕
- 焦外有明显方向性的拖影 → directional smear in the out-of-focus areas〔少见〕　— 像在移动
- 二线性焦外 → busy bokeh〔慎用〕　— 多数情况是缺陷，除非刻意要粗糙感

### 对焦与光学（11）

- 景深 → depth of field〔常用〕　— 画面里「看起来清楚」的那一段前后距离；越浅虚化越强
- 焦点对准 → in focus〔常用〕　— 焦点明确落在主体上，主体锐利
- 专注于脸 → focus on face〔常用〕　— 焦点锁在脸上，其余都化开
- 聚焦在 → focus on〔常用〕
- 前置焦点 → foreground focus〔常用〕　— 焦点落在靠近镜头的前景上，主体反而在后面虚着
- 晕影 → vignetting〔常用〕　— 画面四角比中间暗，像透过一个暗角看进去
- 色差 → chromatic aberration〔常用〕　— 镜头没把不同颜色的光聚到同一点，物体边缘出现红蓝彩边
- 防抖 → image stabilization〔常用〕　— 画面稳、没有手持的抖动感 旧译别名：Image stabilization
- 快门速度 → shutter speed〔常用〕　— 感光的时间长短：越快越能凝固动作，越慢越容易糊 旧译别名：Shutter speed
- 感光度 → ISO〔常用〕　— ISO：对光的敏感程度，越高越亮但噪点越多
- 高动态范围 → HDR〔常用〕　— 亮部和暗部同时保留细节

### 相机类型（9）

- 全画幅相机 → full-frame camera〔常用〕　— 传感器大小等同于 35mm 胶片 旧译别名：Full-frame camera
- 中画幅相机 → medium format camera〔常用〕　— 可拍摄更高分辨率和更细腻的细节 旧译别名：Medium format camera
- 数码单反相机 → DSLR〔常用〕　— 有反光镜和光学取景器，续航好、手感稳
- 无反相机 → mirrorless camera〔常用〕　— 没有反光镜，取景靠电子屏，机身更薄 旧译别名：Mirrorless camera
- 数码相机 → digital camera〔常用〕　— 旧译别名：Digital camera
- 胶片相机 → film camera〔常用〕　— 用胶卷成像，有颗粒和独特的色彩，不能立刻回看 旧译别名：Film camera
- 莱卡相机 → Leica〔常用〕　— 旧译别名：Leica camera
- APS-C 画幅相机 → crop sensor camera〔可用〕　— 传感器小于全画幅 旧译别名：Crop sensor camera
- 傻瓜相机 → point-and-shoot camera〔可用〕　— 小、快、随手拍 旧译别名：Point-and-shoot camera

### 曝光参数（6）

- 曝光不足 → underexposed〔常用〕　— 整体偏暗，暗部细节被压掉，情绪低沉
- 曝光过度 → overexposed〔常用〕　— 整体偏亮，最亮处变成纯白、失去细节
- 低感光度 → low ISO〔常用〕　— 画质最干净，需要足够的光
- 低光照片 → low-light shot〔常用〕　— 旧译别名：Low-light shot
- 向右曝光 → expose to the right〔可用〕　— 在不过曝的前提下尽量往亮曝，后期拉回时暗部更干净
- 高感光度 → high ISO〔可用〕　— 有可见颗粒，常用于暗光和纪实感

### 运动（12）

- 动态模糊 → motion blur〔常用〕　— 物体在曝光期间移动，留下拖影
- 体现运动的线 → motion lines〔常用〕　— 用线条画出运动的轨迹
- 速度线 → speed lines〔常用〕　— 用线条画出运动的方向和速度
- 追随拍摄 → panning〔常用〕　— 相机跟着主体移动拍，主体实、背景拉成横线
- 慢门拖出长长的运动模糊 → a slow shutter trailing long motion blur〔常用〕
- 长曝光把车灯拉成一条条光轨 → a long exposure turning lights into trails〔常用〕
- 慢门拍流水 → a slow shutter turning water into silk〔常用〕　— 水面变成丝绸
- 主体有轻微动态模糊 → slight motion blur on the subject only〔常用〕　— 背景是实的
- 头发和衣角被风带起来 → hair and hems lifted by the wind〔常用〕
- 定格在动作最高点的一瞬 → frozen at the apex of the movement〔常用〕
- 星轨 → star trails〔可用〕　— 超长曝光几十分钟，星星转成一圈圈弧线
- 抖动的画面 → a jittery frame〔可用〕　— 刻意保留手持的抖动，纪录片和抓拍感

## 通用-背景收尾

> A · 背景

### 背景（7）

- 纯色背景 → solid color background〔常用〕
- 白色背景 → white background〔常用〕
- 背景为深色纯色 → a solid dark background that separates the subject cleanly〔常用〕　— 主体干净分离
- 渐变的背景 → gradient background〔常用〕
- 模糊背景 → blurred background〔常用〕
- 简单背景或无背景 → simple or no background〔常用〕　— 旧译别名：background
- 透明背景 → transparent background〔常用〕　— 需要后期合成时用

> B · 收尾

### 收尾（5）

- 画面里只有主体 → only the subject〔常用〕　— 没有别的东西进来
- 画面里只有一个人 → only one person in the frame〔常用〕　— 防「减法错」：不写模型容易自己加人
- 画面里不要出现任何文字 → no text anywhere in the image〔常用〕
- 画面干净 → a clean frame with no background clutter〔常用〕　— 不要有杂乱的背景物件
- 镜面反射里不要出现杂物 → no clutter in reflections〔少见〕

### 排除项（9）

- 不要添加随机文字、乱码或水印 → no random text, gibberish or watermarks〔常用〕　— 几乎所有图都该写
- 不要生成二维码、电话、地址或证书 → do not generate QR codes, phone numbers, addresses or certificates〔常用〕　— 这类细节模型必出错，交给后期
- 不要添加假的标志或假的赞助商 → no fake logos or fake sponsors〔常用〕
- 不要添加不存在的配件 → no accessories that do not exist〔常用〕　— 产品图专项
- 不要过度饱和 → avoid oversaturation〔常用〕　— 食品图尤其
- 不要添加虚假折扣或虚假承诺 → no fake discounts or claims〔可用〕
- 不要出现真实艺人姓名或票务信息 → no real artist names or ticketing details〔可用〕　— 演出海报
- 不要生成标题或按钮文字 → leave out headline and button text so the image can be typeset later〔可用〕　— 官网首屏
- 不要过度锐化 → avoid over-sharpening〔可用〕

# ==== 题材层 ====

## 人像

> A · 人物基础

### 主体类型（29）

- 女性 → female〔常用〕
- 男性 → male〔常用〕
- 女孩 → girl〔常用〕
- 男孩 → boy〔常用〕
- 女仆 → maid〔常用〕
- 修女 → nun〔常用〕　— 天主教女性修行者，穿黑白修道服
- 巫女 → miko〔常用〕　— 日本神道教的女性神职人员，穿白衣红袴
- 魔法少女 → magical girl〔常用〕　— 普通女孩变身成有法力的战士 旧译别名：magical_girl
- 女巫 → witch〔常用〕　— 西方奇幻里的施法女性，常配尖帽与扫帚 旧译别名：Witch
- 法师 → mage〔常用〕
- 忍者 → ninja〔常用〕　— 黑衣、蒙面
- 天使 → angel〔常用〕
- 恶魔 → demon〔常用〕　— 旧译别名：demo
- 吸血鬼 → vampire〔常用〕
- 幽灵 → ghost〔常用〕
- 美人鱼 → mermaid〔常用〕
- 精灵 → elf〔常用〕　— 小体型、尖耳朵的奇幻种族
- 妖精 → fairy〔常用〕　— 带翅膀的小型奇幻生物 旧译别名：elf
- 怪物 → monster〔常用〕
- 人偶 → doll〔常用〕　— 像玩偶一样的人，通常表情空洞、关节可见
- 医生 → doctor〔常用〕
- 护士 → nurse〔常用〕
- 教师 → teacher〔常用〕
- 啦啦队 → cheerleader〔常用〕　— 运动场边加油的队伍
- 兽人 → beastfolk〔可用〕　— 人和兽的混合种族
- 服务员 → waiter〔可用〕
- 伪娘 → crossdressing〔可用〕　— 旧译别名：trap/crossdressing
- 女巨人 → giantess〔少见〕
- 迷你少女 → minigirl〔少见〕

### 年龄段（6）

- 儿童 → a child〔常用〕　— 大约六到十二岁
- 少年 → a teenager〔常用〕　— 大约十三到十七岁
- 青年 → a young adult in their twenties〔常用〕　— 二十多岁
- 中年 → a middle-aged person in their forties〔常用〕　— 四十到五十岁
- 老年 → an elderly person over sixty〔常用〕　— 六十岁以上
- 幼儿 → a toddler〔可用〕　— 大约三到五岁

### 面孔特征（7）

- 东亚面孔 → East Asian features〔常用〕
- 欧美面孔 → Caucasian features〔常用〕
- 混血面孔 → mixed-race features〔常用〕
- 非裔面孔 → African features〔可用〕
- 南亚面孔 → South Asian features〔可用〕
- 中东面孔 → Middle Eastern features〔可用〕
- 拉丁裔面孔 → Latina features〔可用〕

> B · 五官

### 脸型（14）

- 鹅蛋脸 → oval face〔常用〕
- 圆脸 → round face〔常用〕
- 方脸 → square face〔常用〕
- 长脸 → long face〔常用〕
- 心形脸 → heart-shaped face〔常用〕　— 尖下巴、额头宽
- 婴儿肥 → baby fat〔常用〕　— 脸颊有肉
- 颧骨高 → high cheekbones with hollowed cheeks〔常用〕　— 脸颊微凹
- 下颌线清晰 → a sharply defined jawline〔常用〕
- 尖下巴 → a pointed chin〔常用〕
- 面部轮廓柔和 → soft facial contours〔常用〕
- 面部轮廓硬朗 → hard, angular facial contours〔常用〕
- 菱形脸 → diamond face〔可用〕　— 颧骨最宽
- 下颌角明显 → a pronounced jaw angle〔可用〕
- 圆下巴 → a rounded chin〔可用〕

### 眼睛（15）

- 杏眼 → almond eyes〔常用〕　— 圆而略长
- 丹凤眼 → phoenix eyes〔常用〕　— 细长、内眼角往下
- 狐狸眼 → fox eyes〔常用〕　— 眼尾挑得很高
- 圆眼 → round eyes〔常用〕　— 睁得很开
- 细长眼 → narrow eyes〔常用〕
- 吊眼角 → tsurime〔常用〕　— 外眼角往上吊，有攻击性或东方感
- 下垂眼 → tareme〔常用〕　— 外眼角往下走，显得无辜、柔和
- 双眼皮 → double eyelid〔常用〕
- 单眼皮 → single eyelid〔常用〕
- 内双 → hidden double eyelid〔常用〕
- 眼窝深 → deep-set eyes〔常用〕
- 卧蚕 → aegyo-sal〔常用〕　— 眼下那一条微微鼓起的肉
- 水汪汪的眼睛 → watery eyes〔常用〕　— 眼里含着一层水光
- 眼距宽 → wide-set eyes〔可用〕
- 眼距窄 → close-set eyes〔可用〕

### 眼睛颜色（13）

- 棕色眼睛 → brown eyes〔常用〕
- 蓝色眼睛 → blue eyes〔常用〕
- 绿色眼睛 → green eyes〔常用〕
- 灰色眼睛 → grey eyes〔常用〕
- 紫色眼睛 → purple eyes〔常用〕
- 红色眼睛 → red eyes〔常用〕
- 金色眼睛 → golden eyes〔常用〕
- 琥珀色眼睛 → amber eyes〔常用〕
- 橙色眼睛 → orange eyes〔可用〕
- 粉色眼睛 → pink eyes〔可用〕
- 多色眼睛 → multicolored eyes〔可用〕
- 渐变瞳色 → gradient eyes〔可用〕
- 恶魔眼 → devil eyes〔可用〕　— 瞳色发红发光、带异样神采

### 瞳孔（15）

- 爱心瞳 → heart-shaped pupils〔常用〕
- 星形瞳孔 → star-shaped pupils〔常用〕
- X 形瞳孔 → x-shaped pupils〔常用〕
- 符号形瞳孔 → symbol-shaped pupils〔常用〕
- 竖瞳 → slit pupils〔常用〕　— 像猫一样
- 异色瞳 → heterochromia〔常用〕
- 空白瞳孔 → blank pupils〔常用〕　— 没有高光，像空洞
- 瞳孔扩张 → dilated pupils〔常用〕
- 星星眼 → sparkling eyes〔常用〕　— 瞳孔里画着星星，表示极度期待或崇拜
- 钻石形瞳孔 → diamond-shaped pupils〔可用〕
- 一字型瞳孔 → horizontal pupils〔可用〕
- 蛇瞳 → snake pupils〔可用〕
- 恶魔瞳 → devil pupils〔可用〕
- 纽扣眼 → button eyes〔可用〕　— 像布偶
- 瞳孔收缩 → constricted pupils〔可用〕

### 眼睛状态（13）

- 眨眼 → wink〔常用〕　— 旧译别名：eyelid pull
- 睁大眼睛 → wide-eyed〔常用〕
- 眯起眼睛 → narrowed eyes〔常用〕
- 闭上眼睛 → closed eyes〔常用〕
- 一只眼睛闭着 → one eye closed〔常用〕
- 半闭眼睛 → half-closed eyes〔常用〕
- 翻白眼 → rolling eyes〔常用〕　— 旧译别名：rolleyes
- 睁着眼落泪 → crying with eyes open〔常用〕
- 眼下痣 → mole under eye〔常用〕
- 黑眼圈 → dark circles〔常用〕　— 旧译别名：dashed eyes
- 眼圈发红 → ringed eyes〔常用〕　— 刚哭过
- 布满血丝的眼睛 → bloodshot eyes〔可用〕
- 斗鸡眼 → cross-eyed〔少见〕

### 睫毛（7）

- 睫毛 → eyelashes〔常用〕
- 长睫毛 → long eyelashes〔常用〕　— 旧译别名：longeyelashes
- 浓密的睫毛 → thick lashes〔常用〕
- 卷翘的睫毛 → curled lashes〔常用〕
- 睫毛膏 → mascara〔常用〕　— 睫毛根根分明
- 彩色睫毛 → colored eyelashes〔可用〕
- 下睫毛清晰 → lower lashes clearly visible〔可用〕

### 眉毛（19）

- 浓眉 → thick brows〔常用〕
- 细眉 → thin brows〔常用〕
- 柳叶眉 → willow-leaf brows〔常用〕　— 弧度柔和
- 剑眉 → straight brows〔常用〕　— 眉尾上扬有力
- 平眉 → flat brows〔常用〕
- 弓形眉 → arched brows〔常用〕
- 上挑眉 → upswept brows〔常用〕
- 野生眉 → untamed brows〔常用〕　— 没修过、毛流感强
- 修过的眉 → groomed brows〔常用〕　— 边缘干净利落
- 皱眉 → frown〔常用〕
- 挑眉 → raised eyebrows〔常用〕　— 旧译别名：raised eyebrow
- 单边挑眉 → one brow lifted〔常用〕　— 只挑起一边
- 眉头微蹙 → brows slightly drawn together〔常用〕
- V 形眉 → v-shaped brows〔可用〕
- 下垂眉 → downturned brows〔可用〕
- 八字眉 → splayed brows〔可用〕
- 银色眉毛 → silver brows〔可用〕
- 白色眉毛 → white brows〔可用〕
- 无眉 → browless〔少见〕　— 特殊设定

### 鼻型（10）

- 鼻梁挺拔 → a straight, high nose bridge〔常用〕
- 鼻梁低平 → a low, flat nose bridge〔常用〕
- 鼻头圆润 → a rounded nose tip〔常用〕
- 鼻头小巧 → a small, neat nose tip〔常用〕
- 鼻尖微微上翘 → a tip that turns up slightly〔常用〕
- 鼻翼窄 → narrow nostrils〔常用〕
- 侧面看鼻子是一条直线 → a straight nose in profile〔常用〕
- 鼻梁有驼峰 → a bridge with a slight hump〔可用〕
- 鹰钩鼻 → an aquiline nose〔可用〕
- 鼻翼宽 → wide nostrils〔可用〕

### 耳型（16）

- 耳垂明显 → visible earlobes〔常用〕
- 贴面耳 → ears close to the head〔常用〕
- 招风耳 → ears that stick out〔常用〕
- 小巧的耳朵 → small ears〔常用〕
- 耳廓清晰 → a clearly drawn ear shell〔常用〕
- 耳尖微红 → ear tips faintly flushed〔常用〕
- 尖耳 → pointy ears〔常用〕
- 猫耳 → cat ears〔常用〕
- 狐耳 → fox ears〔常用〕
- 犬耳 → dog ears〔常用〕
- 兔耳 → rabbit ears〔常用〕　— 旧译别名：bunny ears
- 狼耳 → wolf ears〔常用〕
- 熊耳 → bear ears〔可用〕
- 鹿耳 → deer ears〔可用〕
- 虎耳 → tiger ears〔可用〕
- 鼠耳 → mouse ears〔可用〕

### 嘴部与牙齿（27）

- 张口 → open mouth〔常用〕
- 闭嘴 → closed mouth〔常用〕
- 嘴唇微张 → parted lips〔常用〕
- 努嘴 → pout〔常用〕
- 撅起的嘴唇 → puckered lips〔常用〕
- 咬牙 → clenched teeth〔常用〕
- 吐舌头 → tongue out〔常用〕
- 舔嘴唇 → licking lips〔常用〕
- 虎牙 → fangs〔常用〕　— 旧译别名：fang
- 露出虎牙 → fang out〔常用〕
- 露出上排牙齿 → upper teeth〔常用〕
- 厚唇 → full lips〔常用〕
- 薄唇 → thin lips〔常用〕
- 上唇薄、下唇厚 → a thin upper lip over a fuller lower〔常用〕
- 唇峰明显 → a defined cupid's bow〔常用〕
- 唇珠饱满 → a full lip bead〔常用〕
- 小巧的唇 → a small mouth〔常用〕
- 嘴角上扬 → corners turning up〔常用〕
- 嘴角下垂 → corners turning down〔常用〕
- 唇色偏红 → lips on the red side〔常用〕
- 唇色偏淡 → lips pale〔常用〕
- 朱唇 → red lips〔常用〕
- 唇釉反光 → glossy lips〔常用〕　— 唇珠有明显亮点
- 挡住嘴巴 → covering mouth〔常用〕
- 手放在嘴边 → hand to mouth〔常用〕
- 宽唇 → a wide mouth〔可用〕
- 嘴唇有干裂的细纹 → fine chapping on the lips〔可用〕

### 皮肤质感（8）

- 皮肤有真实的毛孔和细纹 → real pores and fine lines〔常用〕　— ⭐ 不写容易出塑料脸
- 鼻尖和额头有一点自然的油光 → a little natural oil on nose and forehead〔常用〕
- 颧骨上有几颗雀斑 → a few freckles across the cheekbones〔常用〕
- 皮肤下有淡淡的血色透出来 → a faint flush under the skin〔常用〕
- 颈部和锁骨处的皮肤更薄更亮 → thinner, brighter skin at neck and collarbone〔常用〕
- 细小的绒毛被侧光照亮 → fine down lit by the side light〔可用〕
- 眼下有淡淡的青色与细纹 → faint shadow and fine lines under the eyes〔可用〕
- 出汗后的湿润感 → a slight sheen of sweat〔可用〕

> C · 表情与情绪

### 正面情绪（24）

- 微笑 → smile〔常用〕
- 浅笑 → light smile〔常用〕
- 温柔的微笑 → kind smile〔常用〕
- 露齿而笑 → grin〔常用〕
- 得意地笑 → smirk〔常用〕
- 坏笑 → evil smile〔常用〕
- 苦笑 → sad smile〔常用〕
- 憋笑 → stifled laugh〔常用〕
- 正在笑 → laughing〔常用〕　— 眼睛弯起来
- 对视一笑 → exchanging a smile〔常用〕
- 兴奋 → excited〔常用〕
- 快乐 → happy〔常用〕
- 期待 → hopeful〔常用〕　— 旧译别名：Hopeful
- 欣喜若狂 → elated〔常用〕　— 旧译别名：Elated
- 脸红的 → blush〔常用〕
- 害羞 → shy〔常用〕　— 旧译别名：nose blush
- 尴尬害羞 → embarrassed〔常用〕　— 眼神飘向一边
- 可爱脸 → cute face〔常用〕
- 不安的微笑 → nervous smile〔常用〕
- 强迫笑 → forced smile〔可用〕
- 疯狂的笑 → crazy smile〔可用〕
- 用手指做出笑脸 → finger smile〔可用〕　— 旧译别名：fingersmile
- 得意脸 → doyagao〔可用〕
- 迷人的微笑 → seductive smile〔慎用〕　— 强调诱惑感；中性肖像请改用自然微笑。

### 负面情绪（35）

- 悲伤 → sad〔常用〕
- 忧郁 → gloom〔常用〕　— 整个人往下沉，肩膀塌、视线低
- 沮丧 → frustrated〔常用〕
- 苦恼 → annoyed〔常用〕
- 生气 → angry〔常用〕
- 气愤 → upset〔常用〕
- 一脸不悦 → unamused〔常用〕
- 厌恶 → disgust〔常用〕　— 旧译别名：Disgusted
- 轻蔑 → disdain〔常用〕　— 旧译别名：glaring
- 怒视 → scowl〔常用〕
- 害怕 → fearful〔常用〕　— 旧译别名：Fearful
- 恐惧 → horrified〔常用〕
- 不安 → anxious〔常用〕　— 旧译别名：Anxious
- 恐慌 → panicking〔常用〕
- 绝望 → despair〔常用〕
- 孤独 → lonely〔常用〕
- 嫉妒 → envy〔常用〕
- 邪恶 → evil〔常用〕
- 哭泣 → crying〔常用〕　— 眼眶发红
- 啜泣 → sobbing〔常用〕　— 旧译别名：sobs
- 要哭的表情 → tearing up〔常用〕
- 忍着的表情 → endured face〔常用〕
- 闷闷不乐 → sulking〔常用〕　— 不说话、嘴角往下
- 脸色阴沉 → shaded〔常用〕　— 眼神往下压
- 情绪压着 → depressed〔常用〕　— 嘴角绷紧不说话
- 疲惫 → tired〔常用〕
- 傲娇 → tsundere〔常用〕　— 嘴上凶、心里在意
- 不安地抿嘴 → nervous〔常用〕　— 手指绞在一起
- 烦躁 → fume〔可用〕　— 漫画里头顶冒烟
- 疼痛 → pain〔可用〕
- 尖叫 → screaming〔可用〕
- 叹气 → sigh〔可用〕
- 病娇 → yandere〔可用〕　— 因为爱而走向偏执与危险
- 嚣张 → troll〔可用〕　— 张扬、目中无人
- 厌恶的怪相 → grimace〔可用〕

### 疑问与惊讶（5）

- 惊讶 → surprised〔常用〕
- 疑惑 → confused〔常用〕
- 恍惚 → torogao〔常用〕
- 惊讶到掉色 → color drain〔可用〕　— 极端符号化表达
- 无语 → spit take〔可用〕

### 中性表情（4）

- 面无表情 → expressionless〔常用〕
- 认真 → serious〔常用〕　— 嘴唇抿成一条线
- 思考 → thinking〔常用〕
- 沉思 → pensive〔常用〕

### 眼神（10）

- 凝视 → staring〔常用〕　— 旧译别名：stare
- 眼神坚定 → determined〔常用〕　— 下颌收紧
- 眼神放空 → bored〔常用〕
- 失望地垂眼 → disappointed〔常用〕
- 心虚地移开视线 → guilt〔常用〕
- 轻蔑的眼神 → jitome〔常用〕　— 半垂眼、斜看
- 眼神乱飘 → flustered〔常用〕
- 盯着你 → stare at me〔常用〕　— 直视镜头
- 眼神斜过去 → jealous〔可用〕
- 眼中闪现强烈的情感 → glint〔可用〕

### 哭泣（5）

- 眼泪 → tears〔常用〕
- 流泪 → streaming tears〔常用〕　— 旧译别名：lacrimation
- 开心的眼泪 → happy tears〔常用〕
- 眼眶含着泪没落下来 → eyes brimming〔常用〕
- 泪痕 → tear stains〔常用〕

### 面部反应（7）

- 困倦 → sleepy〔常用〕　— 快睁不开
- 醉酒 → drunk〔常用〕
- 失神 → unconscious〔常用〕
- 瞳孔放大（受惊） → scared〔常用〕
- 憋气 → holding breath〔可用〕
- 喘粗气 → heavy breathing〔可用〕
- 闻 → smelling〔可用〕

### 面部动作（9）

- 以手掩面 → facepalm〔常用〕
- 鼓着腮帮 → cheek bulge〔常用〕
- 捏脸颊 → cheek pinching〔常用〕
- 戳脸颊 → cheek poking〔常用〕
- 抬下巴 → chin grab〔常用〕
- 遮住眼睛 → covering eyes〔常用〕
- 挡住脸 → covering face〔常用〕　— 旧译别名：covering
- 扯脸颊 → cheek pull〔可用〕
- 蒙住眼睛 → covered eyes〔可用〕

> D · 毛发

### 发色（19）

- 黑发 → black hair〔常用〕
- 棕发 → brown hair〔常用〕
- 浅褐发 → light brown hair〔常用〕
- 金发 → blonde hair〔常用〕
- 红发 → red hair〔常用〕
- 银发 → silver hair〔常用〕
- 白发 → white hair〔常用〕
- 灰发 → grey hair〔常用〕
- 粉发 → pink hair〔常用〕
- 蓝发 → blue hair〔常用〕
- 紫发 → purple hair〔常用〕
- 绿发 → green hair〔常用〕
- 渐变发色 → gradient hair〔常用〕
- 挑染 → streaked hair〔常用〕
- 多色头发 → multicolored hair〔常用〕
- 内侧染色 → colored inner hair〔常用〕
- 深蓝发 → dark blue hair〔可用〕
- 浅蓝发 → light blue hair〔可用〕
- 彩虹发 → rainbow hair〔可用〕

### 发长（5）

- 短发 → short hair〔常用〕
- 长发 → long hair〔常用〕
- 中长发 → medium hair〔常用〕
- 超长发 → very long hair〔常用〕
- 长发及腰 → hair past the waist〔常用〕

### 刘海（14）

- 刘海 → bangs〔常用〕
- 齐刘海 → blunt bangs〔常用〕
- 斜刘海 → slanted bangs〔常用〕　— 旧译别名：Slanted bangs
- 中分刘海 → middle-parted bangs〔常用〕　— 旧译别名：middle Fringe
- 分开的刘海 → parted bangs〔常用〕
- 不对称刘海 → asymmetrical bangs〔常用〕
- 交错刘海 → crossed bangs〔常用〕
- 辫子刘海 → braided bangs〔常用〕
- 眼间刘海 → hair between eyes〔常用〕
- 朝一个方向的刘海 → side-swept bangs〔常用〕　— 旧译别名：side swept bangs
- 掀起的刘海 → bangs pinned back〔常用〕
- 头发遮着双眼 → hair over eyes〔常用〕
- 头发遮住一只眼 → hair over one eye〔常用〕
- 美人尖 → widow's peak〔常用〕

### 束发与编发（21）

- 马尾 → ponytail〔常用〕
- 低马尾 → low ponytail〔常用〕
- 高马尾 → high ponytail〔常用〕
- 双马尾 → twintails〔常用〕
- 短双马尾 → short twintails〔常用〕
- 侧马尾 → side ponytail〔常用〕
- 辫子 → braid〔常用〕
- 双辫 → twin braids〔常用〕
- 侧辫 → side braid〔常用〕
- 法式辫 → french braid〔常用〕
- 冠型编发 → crown braid〔常用〕
- 多发辫 → multiple braids〔常用〕
- 脏辫 → dreadlocks〔常用〕
- 发髻 → hair bun〔常用〕
- 丸子头 → topknot〔常用〕
- 双丸子头 → double bun〔常用〕
- 盘发 → updo〔常用〕
- 半扎发 → half updo〔常用〕
- 单侧扎发 → one side up〔常用〕
- 长鬓角 → sidelocks〔常用〕　— 旧译别名：payot
- 扎头发 → tied hair〔常用〕　— 旧译别名：tying hair

### 卷发与直发（7）

- 直发 → straight hair〔常用〕
- 卷发 → curly hair〔常用〕
- 波浪卷 → wavy hair〔常用〕
- 钻发 → drill hair〔常用〕
- 双钻发 → twin drills〔常用〕
- 多钻发 → quad drills〔可用〕
- 外卷发型 → flipped hair〔可用〕

### 发质与状态（13）

- 有光泽的头发 → shiny hair〔常用〕
- 蓬松头发 → big hair〔常用〕
- 湿头发 → wet hair〔常用〕
- 飘动的头发 → floating hair〔常用〕
- 摆动的头发 → hair flaps〔常用〕
- 一缕一缕的发丝 → hair strand〔常用〕
- 散发 → hair spread out〔常用〕
- 披肩发 → hair over shoulder〔常用〕
- 耳后发 → hair behind ear〔常用〕
- 呆毛 → ahoge〔常用〕
- 多根呆毛 → antenna hair〔常用〕
- 云絮状发型 → cloud hair〔可用〕
- 水晶状的头发 → crystal hair〔可用〕

### 短发造型（17）

- 寸头 → buzz cut〔常用〕
- 平头 → crew cut〔常用〕
- 蘑菇头 → bowl cut〔常用〕
- 波波头 → bob cut〔常用〕
- 精灵头 → pixie cut〔常用〕
- 不对称短发 → asymmetrical hair〔常用〕
- 鲻鱼头 → mullet〔常用〕
- 鸟窝头 → afro〔常用〕
- 蜂窝头 → beehive〔常用〕　— 旧译别名：beehive hairdo
- 莫霍克 → mohawk〔常用〕
- 玉米编 → cornrows〔常用〕
- 凌乱发型 → messy hair〔常用〕
- 刺刺的头发 → spiked hair〔常用〕
- 秃头 → bald〔常用〕
- 头发后梳 → hair pulled back〔常用〕
- 平顶 → flattop〔可用〕
- 河童头 → okappa〔可用〕

> E · 体型

### 身形（14）

- 苗条 → slim〔常用〕
- 纤细 → slender〔常用〕
- 匀称 → a balanced build〔常用〕
- 健壮 → a sturdy build〔常用〕
- 肌肉发达 → muscular with visible definition〔常用〕
- 娇小 → petite〔常用〕
- 高挑 → tall and slim〔常用〕
- 丰满 → curvy〔常用〕
- 瘦 → thin〔常用〕
- 高 → tall〔常用〕
- 矮 → short〔常用〕
- 小蛮腰 → a small waist〔常用〕　— 旧译别名：Small waist
- 大长腿 → long legs〔常用〕　— 旧译别名：Long legs
- 胖 → fat〔可用〕

### 肩颈（5）

- 锁骨明显 → prominent collarbones〔常用〕
- 直角肩 → square shoulders〔常用〕
- 颈部修长 → a long neck〔常用〕
- 肩背线条清楚 → a defined shoulder and back line〔常用〕
- 溜肩 → sloping shoulders〔可用〕

### 腰腹（4）

- 腰线明显 → a clear waistline〔常用〕
- 腹肌线条 → abdominal definition〔常用〕
- 腰部曲线 → a curved waistline in profile〔常用〕
- 腰腹紧实 → a flat stomach〔常用〕

### 四肢（4）

- 腿型修长 → slender legs〔常用〕
- 手臂纤细 → slim arms〔常用〕
- 手指细长 → long, slender fingers〔常用〕
- 手部骨感 → bony hands with visible knuckles〔可用〕

> F · 服装

### 上装（27）

- T恤 → T-shirt〔常用〕
- 衬衫 → shirt〔常用〕
- 翻领衬衫 → collared shirt〔常用〕
- 马球衫 → polo shirt〔常用〕
- 毛衣 → sweater〔常用〕
- 连帽毛衣 → hooded sweater〔常用〕
- 露肩毛衣 → off-shoulder sweater〔常用〕
- 卫衣 → hoodie〔常用〕
- 夹克 → jacket〔常用〕
- 连帽夹克 → hooded jacket〔常用〕
- 西装外套 → suit jacket〔常用〕
- 粗呢大衣 → duffel coat〔常用〕
- 外套 → coat〔常用〕
- 背心 → vest〔常用〕
- 无袖紧身背心 → tank top〔常用〕
- 罩衫 → blouse〔常用〕
- 运动衫 → jersey〔常用〕
- 燕尾服 → tailcoat〔常用〕
- 披风 → cape〔常用〕
- 白大褂 → lab coat〔常用〕　— 旧译别名：abcoat
- 细肩带 → spaghetti strap〔常用〕
- 露腰上衣 → midriff〔常用〕
- 袖肩分离装 → detached sleeves〔常用〕
- 短袖 → short sleeves〔常用〕
- 长袖 → long sleeves〔常用〕
- 正装 → formal wear〔常用〕　— 旧译别名：formal
- 袈裟 → kesa〔可用〕　— 旧译别名：Kesa

### 裙装（18）

- 裙子 → skirt〔常用〕
- 迷你裙 → miniskirt〔常用〕
- 短裙 → short skirt〔常用〕　— 旧译别名：short dress
- 长裙 → long skirt〔常用〕　— 旧译别名：long dress
- 百褶裙 → pleated skirt〔常用〕
- 紧身裙 → pencil skirt〔常用〕　— 旧译别名：Pencil Skirt
- 包臀裙 → sheath skirt〔常用〕　— 旧译别名：sheath dress
- 蓬蓬裙 → pettiskirt〔常用〕
- 泡泡裙 → bubble skirt〔常用〕
- 荷叶边裙 → frilled skirt〔常用〕
- 牛仔裙 → denim skirt〔常用〕
- 格子裙 → checkered skirt〔常用〕
- 高腰裙 → high-waist skirt〔常用〕
- 吊带裙 → suspender skirt〔常用〕
- 女仆裙 → maid apron〔常用〕
- 正装短裙 → skirt suit〔常用〕
- 芭蕾短裙 → tutu〔可用〕
- 超短裙 → microskirt〔慎用〕　— 适用于相应服装造型；按角色身份和场景选择。

### 裤装（12）

- 裤子 → pants〔常用〕
- 牛仔裤 → jeans〔常用〕
- 破牛仔裤 → torn jeans〔常用〕
- 牛仔短裤 → denim shorts〔常用〕
- 短裤 → shorts〔常用〕
- 热裤 → hotpants〔常用〕
- 七分裤 → capri pants〔常用〕
- 运动裤 → track pants〔常用〕
- 瑜伽裤 → yoga pants〔常用〕
- 紧身裤 → leggings〔常用〕
- 灯笼裤 → bloomers〔常用〕
- 背带裤 → overalls〔常用〕

### 连身与礼服（13）

- 连衣裙 → dress〔常用〕
- 紧身连衣裙 → bodycon dress〔常用〕　— 旧译别名：taut dress
- 毛衣连衣裙 → sweater dress〔常用〕
- 露肩连衣裙 → off-shoulder dress〔常用〕
- 有领连衣裙 → collared dress〔常用〕
- 无袖连衣裙 → sleeveless dress〔常用〕
- 蕾丝边连衣裙 → lace-trimmed dress〔常用〕
- 百褶连衣裙 → pleated dress〔常用〕
- 晚会礼服 → evening gown〔常用〕
- 婚纱 → wedding dress〔常用〕
- 体操服 → leotard〔常用〕
- 开襟连衣裙 → open dress〔可用〕
- 露背连衣裙 → backless dress〔慎用〕　— 适用于相应服装造型；按角色身份和场景选择。

### 传统服饰（8）

- 汉服 → hanfu〔常用〕　— 旧译别名：Hanfu
- 旗袍 → cheongsam〔常用〕　— 旧译别名：chinadress
- 唐装 → tang suit〔常用〕　— 旧译别名：chinese clothes
- 和服 → kimono〔常用〕　— 旧译别名：japanese clothes
- 浴衣 → yukata〔常用〕
- 水手服 → sailor uniform〔常用〕　— 旧译别名：serafuku
- 学校制服 → school uniform〔常用〕
- 中式礼服 → Chinese formal dress〔可用〕　— 旧译别名：Chinese dress

### 鞋袜（30）

- 运动鞋 → sneakers〔常用〕
- 乐福鞋 → loafers〔常用〕
- 平底鞋 → flat shoes〔常用〕
- 高跟鞋 → high heels〔常用〕
- 细跟高跟鞋 → stiletto heels〔常用〕
- 玛丽珍鞋 → mary janes〔常用〕
- 芭蕾舞鞋 → ballet slippers〔常用〕
- 靴子 → boots〔常用〕
- 马丁靴 → combat boots〔常用〕　— 旧译别名：martin boots
- 及膝靴 → knee boots〔常用〕
- 高跟长靴 → high heel boots〔常用〕
- 拖鞋 → slippers〔常用〕
- 短袜 → socks〔常用〕
- 长袜 → knee-high socks〔常用〕　— 旧译别名：kneehighs
- 过膝袜 → thigh-high socks〔常用〕　— 旧译别名：thighhighs
- 泡泡袜 → loose socks〔常用〕
- 横条袜 → striped socks〔常用〕
- 丝袜 → stockings〔常用〕
- 黑丝 → black stockings〔常用〕
- 白丝 → white pantyhose〔常用〕
- 网袜 → fishnet stockings〔常用〕　— 旧译别名：fishnets
- 损坏的过膝袜 → torn thigh-highs〔常用〕
- 蕾丝裤袜 → lace tights〔常用〕　— 旧译别名：lace legwear
- 条纹连裤袜 → striped tights〔常用〕　— 旧译别名：striped pantyhose
- 女式学生鞋 → uwabaki〔常用〕
- 日式足袋 → tabi〔常用〕
- 腿部系带 → ankle lace-up〔常用〕
- 褶边裤袜 → frilled tights〔可用〕　— 旧译别名：frilled legwear
- 褶边长筒袜 → frilled thigh-highs〔可用〕　— 旧译别名：frilled thighhighs
- 大腿靴 → thigh boots〔慎用〕　— 适用于相应服装造型；按角色身份和场景选择。

### 泳装与内衣（4）

- 泳装 → swimsuit〔常用〕　— 泳装品类；避免人物化呈现
- 连体泳衣 → one-piece swimsuit〔常用〕　— 泳装品类；避免人物化呈现
- 内衣 → underwear〔可用〕　— 电商内衣品类可用；避免人物化呈现
- 比基尼 → bikini〔慎用〕　— 泳装品类，适用于泳池、海滩或泳装展示场景。

> G · 配饰

### 帽子（28）

- 棒球帽 → baseball cap〔常用〕
- 鸭舌帽 → flat cap〔常用〕　— 旧译别名：cap
- 渔夫帽 → bucket hat〔常用〕
- 绒线帽 → beanie〔常用〕
- 礼帽 → top hat〔常用〕
- 软呢帽 → fedora〔常用〕
- 贝雷帽 → beret〔常用〕
- 草帽 → straw hat〔常用〕
- 太阳帽 → sun hat〔常用〕
- 头巾 → turban〔常用〕
- 兜帽（放下） → hood down〔常用〕
- 兜帽（戴上） → hood up〔常用〕
- 水手帽 → sailor hat〔常用〕
- 圣诞帽 → santa hat〔常用〕
- 女巫帽 → witch hat〔常用〕
- 法师帽 → wizard hat〔常用〕
- 护士帽 → nurse cap〔常用〕
- 皇冠 → crown〔常用〕
- 头冠 → tiara〔常用〕
- 头顶光环 → halo〔常用〕
- 兽角 → horns〔常用〕
- 鹿角 → antlers〔常用〕
- 龙角 → dragon horns〔常用〕
- 护额 → forehead protector〔常用〕
- 迷你礼帽 → mini top hat〔可用〕
- 派对帽 → party hat〔可用〕
- 东金帽 → tokin hat〔可用〕
- 带翅膀的头盔 → winged helmet〔可用〕

### 发饰（19）

- 发箍 → headband〔常用〕　— 旧译别名：hair scrunchie
- 发夹 → hairclip〔常用〕
- 发带 → hair ribbon〔常用〕
- 头绳 → hair tie〔常用〕　— 旧译别名：hair bobbles
- 发圈 → hair scrunchie〔常用〕　— 旧译别名：hair rings
- 蝴蝶结发饰 → hair bow〔常用〕
- 簪子 → kanzashi〔常用〕
- 月牙发饰 → crescent hair ornament〔常用〕
- 星星发饰 → star hair ornament〔常用〕
- 心形发饰 → heart hair ornament〔常用〕
- 蝴蝶发饰 → butterfly hair ornament〔常用〕
- 花朵发饰 → flower hair ornament〔常用〕
- 羽毛头饰 → feather hair ornament〔常用〕
- 发珠 → hair beads〔常用〕
- 兽耳头罩 → animal hood〔常用〕
- 女仆头饰 → maid headdress〔常用〕
- 褶边蕾丝发带 → frilled lace headband〔常用〕　— 层叠褶边的蕾丝发带，甜美系
- 猫耳耳机 → cat ear headphones〔常用〕
- 铃铛发饰 → hair bell〔可用〕

### 面部配饰（32）

- 眼镜 → glasses〔常用〕
- 无框眼镜 → rimless eyewear〔常用〕
- 半框眼镜 → over-rim eyewear〔常用〕
- 戴眼镜的 → bespectacled〔常用〕
- 太阳镜 → sunglasses〔常用〕
- 眼罩 → blindfold〔常用〕
- 独眼眼罩 → eyepatch〔常用〕
- 口罩 → face mask〔常用〕　— 旧译别名：antiseptic mask
- 医用口罩 → surgical mask〔常用〕
- 拉着口罩 → mask pull〔常用〕
- 面纱 → veil〔常用〕　— 旧译别名：veils
- 狐狸面具 → fox mask〔常用〕
- 面具（掀到头上） → mask on head〔常用〕
- 摘下的面具 → mask removed〔常用〕
- 护目镜 → goggles〔常用〕
- 头上别着护目镜 → goggles on head〔常用〕
- 无线耳机 → wireless earbuds〔常用〕
- 面纹 → facepaint〔常用〕
- 额前宝石 → forehead jewel〔常用〕
- 额前图案 → forehead mark〔常用〕
- 脸颊上的疤痕 → scar on cheek〔常用〕
- 眼部疤痕 → scar across the eye〔常用〕
- 贴着绷带的脸 → bandage on face〔常用〕　— 旧译别名：bandage on
- 用绷带包扎一只眼 → bandage over one eye〔常用〕
- 美人痣 → beauty mark〔常用〕　— 旧译别名：mole under mouth
- 纹身 → tattoo〔常用〕
- 厚如瓶底的圆眼镜 → coke-bottle glasses〔可用〕
- 心形眼镜 → heart-shaped eyewear〔可用〕
- 天狗面具 → tengu mask〔可用〕
- 防毒面具 → gas mask〔可用〕
- 头戴显示设备 → head-mounted display〔可用〕　— 旧译别名：head mounted display
- 从后脑戴的耳机 → behind-the-head headphones〔可用〕

### 耳饰（6）

- 耳环 → earrings〔常用〕
- 耳钉 → stud earrings〔常用〕
- 环状耳环 → hoop earrings〔常用〕
- 心形耳环 → heart earrings〔常用〕
- 水晶耳环 → crystal earrings〔常用〕
- 长坠耳饰 → long drop earrings〔常用〕

### 颈饰（13）

- 项链 → necklace〔常用〕
- 贴颈项圈 → choker〔常用〕　— 贴颈的窄项圈
- 颈带 → ribbon choker〔常用〕
- 项圈 → collar〔常用〕
- 领带 → necktie〔常用〕　— 旧译别名：necktie/tie
- 领结 → bow tie〔常用〕
- 水手领 → sailor collar〔常用〕
- 围巾 → scarf〔常用〕
- 丝带 → ribbon〔常用〕
- 珠链 → bead necklace〔常用〕
- 首饰 → jewelry〔常用〕
- 锚形项圈 → anchor choker〔可用〕
- 项链挂口哨 → whistle around neck〔可用〕

### 手饰（8）

- 手链 → bracelet〔常用〕
- 手镯 → bangle〔常用〕
- 手表 → wristwatch〔常用〕
- 手套 → gloves〔常用〕
- 长手套 → elbow gloves〔常用〕
- 露指手套 → fingerless gloves〔常用〕
- 蕾丝手套 → lace gloves〔常用〕　— 旧译别名：wears a pair of white lace gloves
- 绷带缠手臂 → bandaged arm〔常用〕

### 腰部与包（8）

- 腰带 → belt〔常用〕
- 腰包 → fanny pack〔常用〕
- 围腰毛衣 → sweater around waist〔常用〕
- 双肩包 → backpack〔常用〕
- 手提包 → handbag〔常用〕
- 斜挎包 → cross-body bag〔常用〕
- 单肩包 → one-shoulder bag〔常用〕　— 旧译别名：One shoulder bag
- 帆布包 → canvas bag〔常用〕　— 旧译别名：Canvas bag

### 手持道具（9）

- 雨伞 → umbrella〔常用〕
- 手杖 → cane〔常用〕
- 魔杖 → staff〔常用〕
- 金权杖 → golden staff〔常用〕　— 旧译别名：holding a golden staff
- 扇子 → folding fan〔常用〕
- 书 → book〔常用〕
- 花束 → bouquet〔常用〕
- 酒杯 → wine glass〔常用〕
- 左轮手枪 → revolver〔可用〕

> H · 动作与姿态

### 手部动作（37）

- 招手 → waving〔常用〕
- 牵手 → holding hands〔常用〕
- 拥抱 → hug〔常用〕
- 张开双臂 → spread arms〔常用〕
- 双抬臂 → arms up〔常用〕
- 双手叉腰 → hands on hips〔常用〕
- 单手插腰 → hand on hip〔常用〕
- 手交叉于胸前 → arms crossed〔常用〕
- 手放身后 → arms behind back〔常用〕
- 手臂放头后 → arms behind head〔常用〕
- 手插在口袋里 → hands in pockets〔常用〕
- 手自然垂着 → hands hanging naturally〔常用〕
- 手撑着头 → chin rest〔常用〕
- 一手托腮 → one hand propping the chin〔常用〕
- 双手交叠放在膝上 → both hands folded on the lap〔常用〕
- 双手相扣 → hands clasped〔常用〕　— 旧译别名：own hands clasped
- 双手捧住一样东西 → both hands cupping something〔常用〕
- 手指捏着一个小物件 → fingers pinching a small object〔常用〕
- 一只手撩头发 → one hand sweeping the hair〔常用〕
- 双手拨头发 → hands in hair〔常用〕
- 手放脸上 → hand on face〔常用〕　— 旧译别名：hand on own face
- 手放胸前 → hand on chest〔常用〕
- 翘大拇指 → thumbs up〔常用〕
- 剪刀手 → peace sign〔常用〕　— 食指和中指比 V，最常见的拍照手势
- 攥拳 → clenched fist〔常用〕　— 旧译别名：clenched hand
- 摸头 → headpat〔常用〕　— 把手放在自己头上，表示困扰或撒娇
- 自拍 → selfie〔常用〕
- 扶正眼镜 → adjusting eyewear〔常用〕　— 用手指把眼镜往上推，常见于斯文形象
- 拳打 → punching〔可用〕
- 敬礼 → salute〔可用〕
- 手枪手势 → finger gun〔可用〕
- 猫爪手势 → cat pose〔可用〕
- 抬起食指 → index finger raised〔可用〕
- 拉头发 → hair pull〔可用〕
- 手腕内侧朝上 → the inner wrist turned up〔可用〕
- 五指张开贴在玻璃上 → a hand splayed flat against glass〔可用〕
- 手指绕着杯沿划圈 → a finger tracing the rim of a cup〔可用〕

### 腿部与站姿（22）

- 站立 → standing〔常用〕
- 坐着 → sitting〔常用〕
- 蹲下 → squatting〔常用〕
- 下跪 → kneeling〔常用〕
- 正坐 → seiza〔常用〕
- 侧身坐 → yokozuwari〔常用〕
- 盘腿 → cross-legged〔常用〕　— 旧译别名：indian style
- 抱腿坐 → knees up〔常用〕
- 双腿并拢 → legs together〔常用〕
- 双腿交叉 → crossed legs〔常用〕
- 双腿分开 → legs apart〔常用〕
- 单腿站立 → standing on one leg〔常用〕
- A 字站姿 → A-pose〔常用〕
- T 字站姿 → T-pose〔常用〕
- 中性站姿 → neutral stance〔常用〕
- 光腿 → bare legs〔常用〕
- 战斗姿态 → fighting stance〔常用〕
- 跨坐 → straddle〔可用〕
- 抬腿 → leg up〔可用〕
- 脚踢 → kicking〔可用〕
- 膝到胸 → knees to chest〔可用〕
- 屈膝礼 → curtsy〔可用〕

### 全身动作（24）

- 身体前倾 → leaning forward〔常用〕
- 躺着 → lying〔常用〕
- 侧躺 → on side〔常用〕
- 趴着 → on stomach〔常用〕
- 仰面躺 → on back〔常用〕
- 睡觉 → sleeping〔常用〕
- 颤抖 → trembling〔常用〕
- 弓起身体 → arched back〔常用〕
- 唱歌 → singing〔常用〕
- 跳舞 → dancing〔常用〕
- 拉伸 → limbering up〔常用〕　— 压腿、扩胸一类准备活动 旧译别名：stretching
- 伸懒腰 → a waking stretch〔常用〕　— 双臂上举、身体后仰，刚醒或放松时 旧译别名：stretch
- 靠墙 → against wall〔常用〕
- 回头 → looking back〔常用〕
- 抬头 → head tilt〔常用〕
- 背对背 → back-to-back〔常用〕
- 玩水 → wading〔常用〕
- 浸在水中 → partially submerged〔常用〕　— 旧译别名：partially submerged,
- 动态姿势 → dynamic pose〔常用〕
- 正面站姿 → front-facing neutral pose〔常用〕
- 浮在水上 → afloat〔可用〕
- 脚在水里 → soaking feet〔可用〕
- 身体颠倒 → upside-down〔可用〕
- 四肢着地 → all fours〔可用〕

> I · 关系互动

### 关系互动（29）

- 脸贴脸 → cheek-to-cheek〔常用〕
- 额头贴额头 → forehead-to-forehead〔常用〕
- 两个人贴得很近 → two people standing very close〔常用〕　— 肩膀几乎靠在一起
- 二人面对面 → facing another〔常用〕
- 两人对望 → the two looking at each other〔常用〕　— 视线交叉
- 两人朝同一方向看 → both looking the same way〔常用〕
- 共同望向远方 → both looking off to the distance〔常用〕　— 不看对方
- 手牵手 → holding hands with fingers interlaced〔常用〕　— 手指交扣
- 挽着手臂 → arm in arm〔常用〕　— 一个人靠着另一个人
- 一只手搭在对方肩上 → one hand resting on the other's shoulder〔常用〕
- 搂着腰 → an arm around the waist〔常用〕
- 一方从背后环抱另一方 → one embracing the other from behind〔常用〕
- 正面拥抱 → a frontal embrace〔常用〕　— 手臂环住对方
- 摸对方的头 → one hand patting the other's head〔常用〕
- 亲吻额头 → a kiss on the forehead〔常用〕
- 亲吻脸颊 → a kiss on the cheek〔常用〕
- 耳语 → whispering close to the ear〔常用〕　— 凑到耳边说话
- 额头抵着对方的肩膀 → forehead against the other's shoulder〔常用〕
- 母亲低头看孩子 → a mother looking down at her child〔常用〕
- 大人牵着小孩的手 → an adult holding a child's hand〔常用〕
- 背靠背坐着 → sitting back to back〔常用〕
- 并肩走 → walking side by side in step〔常用〕　— 步幅一致
- 一个坐着、一个站在旁边 → one seated, the other standing beside〔常用〕
- 一个人回头 → one turning back〔常用〕　— 另一个在前方
- 高矮差明显 → a clear height difference〔常用〕　— 一高一矮并肩
- 一人前景一人背景 → one figure in the foreground〔常用〕　— 前后错开
- 递给对方一样东西 → handing something over〔常用〕
- 家人围坐 → family seated in a loose circle〔常用〕　— 构成一个圈
- 两人平行站位 → two figures in parallel〔可用〕　— 构图对称

> J · 妆容

### 妆容（6）

- 化妆 → makeup〔常用〕
- 素颜 → bare-faced〔常用〕　— 几乎没有妆感
- 淡妆 → light natural makeup〔常用〕　— 只提气色
- 浓妆 → heavy makeup〔常用〕　— 眼影与唇色都重
- 泪痣 → a beauty mark under the eye〔常用〕
- 晒伤妆 → sunburn blush〔可用〕　— 颧骨横过一道红

## 风景自然

> A · 地貌

### 地形（21）

- 山 → a mountain〔常用〕　— 旧译别名：mountain
- 山谷 → a valley〔常用〕　— 旧译别名：valley
- 山顶 → a summit〔常用〕　— 旧译别名：the top of the hill
- 悬崖 → a sheer cliff dropping straight down〔常用〕　— 垂直的岩壁直插下去
- 高原 → a plateau〔常用〕　— 旧译别名：plateau
- 平原 → flat plains with a horizon stretched far〔常用〕　— 地平线拉得很平很远
- 草原 → a meadow〔常用〕　— 旧译别名：in a meadow
- 沙漠 → a desert〔常用〕　— 旧译别名：on a desert
- 红土荒漠 → red desert rock eroded into pillars〔常用〕　— 风把红色砂岩蚀成一根根柱子
- 盐湖 → an endless salt flat with a mirror surface〔常用〕　— 水面极平，能完整倒映天空（天空之镜）
- 火山 → a volcano〔常用〕
- 火山口边缘 → the rim of a crater with smoke beyond〔常用〕　— 远处有烟
- 洞穴 → a cave narrowing then opening out〔常用〕　— 岩壁往里收窄然后豁然开阔
- 冰洞穴 → an ice cave〔常用〕　— 旧译别名：Ice cave
- 冰川裂隙 → a glacier crevasse glowing blue〔常用〕　— 冰层深处的蓝最亮
- 冰原 → an ice sheet〔常用〕　— 一望无际的冰盖，只有风刻出的纹路
- 陡峭的峡谷 → a steep canyon with near-vertical walls〔常用〕　— 两壁几乎垂直
- 陨石坑 → a crater with a raised rim and sunken center〔常用〕
- 外星地貌 → an extraterrestrial landscape〔常用〕　— 不像地球的岩层与颜色，可能是紫或绿的天空 旧译别名：Extraterrestrial landscape
- 地外世界 → an extraterrestrial world〔常用〕　— 旧译别名：Extraterrestrial
- 潮间带滩涂 → tidal flats with ripples left by the ebb〔可用〕　— 退潮后留下一条条纹路

### 水体（10）

- 大海 → the ocean〔常用〕　— 旧译别名：ocean
- 海面波光 → sunlight shattered across the wave tops〔常用〕　— 阳光在浪尖上碎成一片
- 礁石与浪花 → waves breaking white against rocks〔常用〕　— 浪撞上石头炸开
- 湖 → a lake〔常用〕
- 冰封的湖面 → a frozen lake with bubbles and cracks beneath〔常用〕　— 底下有气泡和裂纹
- 江河 → a broad slow river〔常用〕　— 水面宽而流速慢
- 溪流 → a stream splitting around stones〔常用〕　— 水在石头间分成几股
- 瀑布 → a waterfall with mist at the base〔常用〕　— 水从高处砸下来，底下有水雾
- 沼泽 → still marsh water with duckweed floating〔常用〕　— 水是静的，漂着浮萍
- 水下世界 → an underwater world〔常用〕　— 镜头在水面以下，能看到光柱和水泡 旧译别名：Underwater world

### 植被（15）

- 森林 → a forest〔常用〕　— 旧译别名：forest
- 针叶林 → a conifer forest〔常用〕　— 松杉类树林，颜色很深、树形是尖塔
- 竹林 → a bamboo grove〔常用〕　— 竿子笔直、叶片细碎
- 白桦林 → birches with black scars on white trunks〔常用〕　— 白树皮上有黑色横疤的树林，北方特征
- 枫树林 → a maple grove turned solid red〔常用〕　— 叶子红成一片
- 高山草甸 → an alpine meadow in sheets of wildflowers〔常用〕　— 高海拔的草地，夏天开满小野花
- 花田 → a flower meadow〔常用〕　— 旧译别名：flowers meadows
- 樱花 → cherry blossoms〔常用〕
- 落花 → falling petals〔常用〕
- 苔藓 → moss wrapping stones and roots in green〔常用〕　— 苔藓长满石头和树根，把一切染绿
- 藤蔓 → vines hanging down and taking over〔常用〕　— 从上面垂下来缠住一切
- 芦苇 → reeds leaning as one when the wind passes〔常用〕　— 芦苇丛被风吹得整片倾斜
- 仙人掌 → columnar cacti standing with spines〔常用〕　— 柱子一样立着、带刺
- 树 → trees〔常用〕　— 旧译别名：tree
- 花草 → flowers and grass〔常用〕

> B · 天时

### 天象（17）

- 天空 → sky〔常用〕
- 夜空 → night sky〔常用〕　— 天是深的蓝黑色，有层次、不是纯黑
- 星空 → starry sky〔常用〕　— 能看到星星，天很干净、没有光污染
- 月亮 → moon〔常用〕
- 太阳 → sun〔常用〕
- 流星 → shooting star〔常用〕
- 银河 → the Milky Way〔常用〕　— 旧译别名：galaxy
- 星云 → nebula〔常用〕
- 极光 → aurora borealis〔常用〕
- 梦幻云彩 → dreamy clouds〔常用〕　— 旧译别名：Dreamy clouds
- 火烧云 → a sky burned orange at sunset〔常用〕　— 整片天被烧成橘红
- 厚重的积雨云 → heavy cumulonimbus pressing low〔常用〕
- 平流雾 → advection fog creeping along the ground〔可用〕　— 雾像水一样贴着地面流动，把低处淹掉
- 双层彩虹 → a double rainbow〔可用〕
- 雨幡 → virga trailing from the cloud base〔少见〕　— 雨还没落地就在空中蒸发，云底垂下一缕缕丝
- 乳状云 → mammatus bulging under the cloud〔少见〕　— 云底垂下一个个袋状鼓包，暴风雨前后出现
- 日晕 → a solar halo ringing the sun〔少见〕　— 冰晶折射阳光形成的一圈光环

### 季节（10）

- 春 → spring〔常用〕　— 旧译别名：in spring
- 初春 → early spring〔常用〕　— 枝头刚冒出一点嫩绿
- 夏 → summer〔常用〕　— 旧译别名：in summer
- 盛夏 → high summer〔常用〕　— 叶子浓绿到发黑
- 秋 → autumn〔常用〕　— 旧译别名：in autumn
- 深秋 → late autumn〔常用〕　— 落叶铺满地面
- 冬 → winter〔常用〕　— 旧译别名：in winter
- 初冬 → early winter〔常用〕　— 树枝光秃，地面有薄霜
- 隆冬 → deep winter〔常用〕　— 大雪把一切轮廓都抹平
- 梅雨 → the rainy season〔常用〕　— 初夏连续阴雨，一切湿透、绿色浓

> C · 场景

### 自然场景（5）

- 海边日落 → a purple sunset at the beach〔常用〕　— 旧译别名：beautiful purple sunset at beach
- 火山喷发 → volcanic eruption〔常用〕　— 岩浆和火山灰从火山口喷出，天空被染红 旧译别名：Volcanic Eruption
- 沙漠绿洲 → a desert oasis〔常用〕　— 沙漠里的一小片水与植物，四周全是沙 旧译别名：Desert oasis
- 浮岛群 → a cluster of floating islands〔常用〕　— 几块陆地悬在空中
- 杂草丛生的自然 → overgrown nature〔常用〕　— 植物把人工结构吃掉 旧译别名：Overgrown nature

### 奇幻场景（30）

- 魔法森林 → a magical forest〔常用〕　— 旧译别名：Magical forest
- 黑暗森林 → a dark forest〔常用〕　— 旧译别名：Dark Forest
- 鬼屋森林 → a haunted forest〔常用〕　— 旧译别名：Haunted forest
- 蘑菇森林 → a mushroom forest〔常用〕　— 旧译别名：Mushroom Forest
- 魔法花园 → an enchanted garden〔常用〕　— 旧译别名：Enchanted garden
- 神秘山脉 → mystic mountains〔常用〕　— 旧译别名：Mystic mountain
- 仙人掌沙漠 → a cactus desert〔常用〕　— 旧译别名：Cactus Desert
- 水晶洞穴 → a crystal cave〔常用〕　— 旧译别名：Crystal cave
- 天空岛屿 → a sky island〔常用〕　— 旧译别名：Sky island
- 浮空城市 → a floating city〔常用〕　— 旧译别名：Floating city
- 巴比伦空中花园 → the Hanging Gardens of Babylon〔常用〕　— 旧译别名：Hanging Gardens of Babylon
- 未来公园 → a futuristic park〔常用〕　— 旧译别名：Futuristic park
- 冰雪王国 → an ice kingdom〔常用〕　— 旧译别名：Ice kingdom
- 热带天堂 → a tropical paradise〔常用〕　— 旧译别名：Tropical paradise
- 外星球 → an alien planet〔常用〕　— 旧译别名：Alien planet
- 月球地貌 → a lunar landscape〔常用〕　— 旧译别名：Lunar landscape
- 月球殖民地 → a lunar colony〔常用〕　— 旧译别名：Lunar colony
- 在外太空 → outer space〔常用〕
- 虫洞 → a wormhole〔常用〕　— 旧译别名：Wormhole
- 反乌托邦未来 → a dystopian future〔常用〕　— 旧译别名：Dystopian future
- 后启示录荒野 → a post-apocalyptic wasteland〔常用〕　— 旧译别名：Post-apocalyptic wasteland
- 蒸汽朋克工厂 → a steampunk factory〔常用〕　— 旧译别名：Steampunk Factory
- 机器人工厂 → a robot factory〔常用〕　— 旧译别名：Robot factory
- 巨大机器 → giant machines〔常用〕　— 旧译别名：Giant Machines
- 宇宙飞船 → a spaceship〔常用〕　— 旧译别名：Spaceship
- 废弃宇宙飞船 → an abandoned spaceship〔常用〕　— 旧译别名：Abandoned spaceship
- 赛博朋克小巷 → a cyberpunk alley〔常用〕
- 神话世界 → a mythical world〔常用〕
- 超现实梦境 → a surreal dreamscape〔常用〕　— 旧译别名：Surreal Dreamland
- 数字宇宙 → a digital universe〔常用〕　— 旧译别名：Digital Universe

## 建筑空间

> A · 城市与建筑

### 城市景观（26）

- 城市 → city〔常用〕
- 街道 → street〔常用〕
- 老城区 → an old quarter with worn walls and tangled wires〔常用〕　— 墙面旧、电线乱拉
- 商业街 → a shopping street lined with signs〔常用〕　— 招牌一路铺过去
- 夜市 → a night market〔常用〕　— 摊位的灯把地面照成暖色
- 广场 → a plaza〔常用〕　— 空旷、铺装是几何的
- 小镇 → a small town〔常用〕　— 屋顶连成一片、街道很窄
- 浪漫小镇 → a romantic town〔常用〕　— 旧译别名：Romantic Town
- 奇幻村庄 → a fantasy village〔常用〕　— 旧译别名：Fantasy village
- 古罗马街道 → an ancient Roman street〔常用〕
- 港口 → a port with containers and cranes in rows〔常用〕　— 集装箱和吊机排成阵
- 近未来都市 → a near-future city〔常用〕　— 旧译别名：near future city
- 未来都市 → a futuristic metropolis〔常用〕　— 旧译别名：Futuristic metropolis
- 工业城市 → an industrial cityscape〔常用〕
- 霓虹城市 → a neon city〔常用〕　— 旧译别名：Neon city
- 雨天城市 → a rainy city〔常用〕　— 旧译别名：Rainy City
- 赛博朋克城市 → a cyberpunk city〔常用〕
- 蒸汽朋克城市 → a steampunk cityscape〔常用〕
- 世界末日城市 → an apocalyptic city〔常用〕　— 旧译别名：Apocalyptic city
- 废墟 → ruins〔常用〕
- 废弃城市建筑群 → deserted city buildings〔常用〕
- 古代遗迹 → ancient ruins〔常用〕　— 旧译别名：Ancient ruins
- 沉船遗迹 → a sunken shipwreck〔常用〕　— 旧译别名：Sunken Shipwreck
- 冥界 → an underworld of dark structures and mist〔常用〕　— 成片的暗色建筑与雾 旧译别名：Underworld
- 紫禁城 → the Forbidden City〔常用〕　— 旧译别名：Forbidden city
- 赛博朋克丛林 → a cyber jungle〔可用〕　— 旧译别名：Cyber jungle

### 建筑类型（14）

- 摩天楼 → a skyscraper with a glass facade rising〔常用〕　— 玻璃的立面一直往上
- 塔 → a tower tapering as it rises〔常用〕　— 越往上越细
- 桥 → a bridge〔常用〕　— 墩子立在水中、拉索张开
- 图书馆 → a library〔常用〕　— 方正、开窗很少
- 灯塔 → a lighthouse〔常用〕　— 旧译别名：at the lighthouse
- 民居 → a vernacular house with a pitched roof and plain walls〔常用〕　— 坡屋顶、墙是素的
- 寺庙 → a temple〔常用〕
- 古代神庙 → an ancient temple〔常用〕　— 旧译别名：Ancient Temple
- 神秘古墓 → a mysterious tomb〔常用〕　— 旧译别名：Mysterious Tomb
- 水晶宫殿 → a crystal palace〔常用〕　— 旧译别名：Crystal palace
- 魔法城堡 → a magical castle〔常用〕　— 旧译别名：Magical castle
- 中世纪城堡 → a medieval castle〔常用〕　— 旧译别名：Medieval castle
- 童话城堡 → a fairy-tale castle〔常用〕　— 旧译别名：Fairy Tale Castle
- 魔法王国 → a magical kingdom〔常用〕　— 旧译别名：Magical Kingdom

> B · 室内

### 室内空间（23）

- 室内 → indoors〔常用〕
- 宫廷 → a palace interior〔常用〕　— 旧译别名：palace
- 教堂 → a church〔常用〕　— 旧译别名：church
- 哥特式大教堂 → a Gothic cathedral〔常用〕　— 旧译别名：Gothic cathedral
- 寺庙内 → a temple interior〔常用〕
- 温泉 → an onsen〔常用〕　— 旧译别名：onsen
- 酒吧 → a bar〔常用〕　— 旧译别名：in a bar
- 居酒屋 → an izakaya〔常用〕　— 旧译别名：in a tavern
- 咖啡厅 → a cafe〔常用〕　— 旧译别名：cafe
- 教室 → a classroom〔常用〕　— 旧译别名：classroom
- 餐厅 → a restaurant〔常用〕　— 旧译别名：restaurant
- 商店 → a shop〔常用〕　— 旧译别名：shop
- 卧室 → a bedroom〔常用〕　— 旧译别名：bedroom
- 厨房 → a kitchen〔常用〕　— 台面干净、器具有序
- 书房 → a study with books stacked to the ceiling〔常用〕　— 书一直堆到天花板
- 画廊 → a gallery〔常用〕　— 白墙、射灯只打作品
- 地铁车厢 → a subway car〔常用〕　— 扶手和吊环排成一列
- 体育馆 → an arena with tiers of seating rising〔常用〕　— 看台一圈圈围上去
- 舞台 → a stage〔常用〕　— 旧译别名：stage
- 舞台灯光穿过烟雾 → stage beams cutting through haze〔常用〕　— 舞台烟机配聚光灯，光路明显，演出感
- 炼金室 → an alchemy laboratory〔常用〕　— 旧译别名：Alchemy Laboratory
- 未来实验室 → a futuristic laboratory〔常用〕　— 旧译别名：Futuristic laboratory
- 黑暗地牢 → a dungeon〔常用〕　— 旧译别名：dungeon

> C · 构件与做法

### 结构构件（28）

- 柱廊 → a colonnade of evenly spaced columns〔常用〕　— 等距排列的柱子撑起一条廊，古典建筑的常见做法
- 连续的拱券 → a run of arches receding one after another〔常用〕　— 罗马式与伊斯兰建筑
- 肋架拱顶 → ribbed vaulting with ribs crossing overhead〔常用〕　— 哥特式
- 外露的钢桁架 → exposed steel trusses with diagonal bracing〔常用〕　— 工业风
- 大跨度悬挑 → a long cantilever with nothing under it〔常用〕　— 结构只有一端固定，另一端凭空悬出
- 玻璃幕墙 → a full glass curtain wall〔常用〕　— 现代高层的外墙整面用玻璃，会反射天空和对面楼
- 天窗 → a skylight dropping light from the ridge〔常用〕　— 屋顶开的洞，把光从正上方引进来
- 老虎窗 → a dormer poking out of the pitched roof〔常用〕　— 斜屋顶上凸出的小窗，为阁楼采光
- 旋转楼梯 → a spiral stair winding around a central column〔常用〕　— 台阶围绕中心柱螺旋上升
- 女儿墙 → a low parapet along the roof edge〔常用〕　— 屋顶四周的安全矮墙
- 木格栅 → a timber louvre slicing light into stripes〔常用〕　— 细木条排成一排，光透过来变成一条条
- 飞檐翘角 → upturned eaves sweeping outward and up〔常用〕　— 中式与东亚建筑
- 斗拱层叠 → stacked dougong brackets stepping out〔常用〕　— 中式木构的承重构件
- 悬山顶 → an overhanging gable roof〔常用〕　— 中国古建筑屋顶等级最低的一种 旧译别名：overhanging gable roof
- 歇山顶 → a hip-and-gable roof〔常用〕　— 一条正脊、四条垂脊、四条戗脊，共九脊 旧译别名：hip-and-gable roof
- 马头墙 → stepped gable walls rising above the roof〔常用〕　— 徽派建筑的山墙做成阶梯状高出屋顶（也叫封火墙） 旧译别名：horse-head gable wall
- 月洞门 → a moon gate〔常用〕　— 中式园林的圆形门洞，本身就是一个取景框 旧译别名：moon gate
- 影壁 → a free-standing screen wall facing the entrance〔常用〕　— 进门正对的一堵墙，挡住视线 旧译别名：spirit screen wall
- 美人靠 → a curved wooden bench along the veranda〔常用〕　— 江南园林里带靠背弧度的长凳 旧译别名：waterside bench railing
- 夯土墙 → rammed earth with horizontal lift lines〔常用〕　— 把土一层层夯实成墙，横向的层纹是施工痕迹
- 木模板木纹印在混凝土上 → timber grain left in the concrete〔常用〕　— 木纹被印在混凝土上
- 石材干挂 → dry-hung stone with straight joints〔常用〕　— 石板用金属件挂在墙上，板缝笔直且深
- 拉毛墙面 → a rough stucco wall like sandpaper〔常用〕　— 表面故意做成粗糙颗粒
- 老砖墙 → old brickwork with moss in the joints〔常用〕　— 旧砖墙，砖缝积了土长出青苔
- 水磨石 → terrazzo with chips set into cement〔常用〕　— 石子拌进水泥再磨平抛光
- 陶土砖 → terracotta brick〔常用〕　— 烧制时温度不匀，颜色深浅不一、有斑点
- 青瓷 → celadon〔常用〕　— 中国青瓷的釉色，粉青或梅子青，温润有玉感 旧译别名：Celadon
- 悬索结构 → a cable-net roof〔少见〕　— 用钢索把屋顶吊起来，像吊桥一样

## 产品静物

> A · 构图与摆放

### 摆放方式（24）

- 产品居中 → product centred and fully visible〔常用〕　— 棚拍底盘写法
- 产品只占一角 → the product in one corner〔常用〕　— 大面积留白给文案
- 产品放在画面右侧 → the product on the right〔常用〕　— 官网首屏，留白给后期排版
- 产品占画面约六成 → the product fills about 60% of the frame〔常用〕　— 社媒方形图
- 产品斜靠 → the product leaning into a diagonal〔常用〕　— 形成一条对角线
- 产品悬浮在简洁背景中 → product floating in a clean background〔常用〕　— 科技／美妆／饮品广告
- 产品和包装同框 → the product in front of its packaging〔常用〕　— 层次清楚，适合礼盒与套装
- 产品与倒影同框 → the product with its reflection filling the lower half〔常用〕　— 倒影占下半格
- 产品被手拿着 → the product held in hand〔常用〕　— 只露手指
- 多个产品堆叠成塔 → products stacked into a tower〔常用〕
- 同系列产品排成一行 → the rest of the range blurred behind〔常用〕　— 虚化在后面
- 周围有少量相关道具 → a few relevant props that do not steal focus〔常用〕　— 但不抢主体
- 与产品同色的道具 → a prop in the same colour as the product〔常用〕　— 颜色呼应
- 一块有纹理的石板当台面 → a textured stone slab as the surface〔常用〕
- 一块垂落的丝绸 → silk falling in flowing folds〔常用〕　— 做出流动的褶
- 亚麻布做底 → a linen base with natural creases〔常用〕　— 有自然的褶
- 几何石膏块垫出层次 → geometric plaster blocks for depth〔常用〕
- 亚克力透明支架把产品垫高 → a clear acrylic riser lifting the product〔常用〕
- 一片干净的玻璃板做反射 → a clean glass sheet for reflection〔常用〕
- 细砂或小石子铺一层 → a bed of fine sand or pebbles〔常用〕
- 飘在空中的水花或粉末 → water or powder suspended in the air〔常用〕　— 悬浮感
- 干花或枝叶从边缘露进来 → dried leaves peeking in at the edge〔常用〕　— 只从边缘露进来
- 香水瓶 → a perfume bottle〔常用〕　— 旧译别名：perfume bottle
- 化妆品瓶 → a cosmetic bottle〔常用〕　— 旧译别名：cosmetic bottle

> B · 背景与台面

### 台面背景（10）

- 浅色台面 → a light-colored surface〔常用〕
- 浅灰棚拍背景 → light grey studio backdrop〔常用〕　— 影棚里用的浅灰背景纸，干净、不抢主体
- 无缝背景纸 → a seamless backdrop〔常用〕　— 背景纸从底部的浅灰渐变到顶部的白
- 纯白无缝背景（白底图） → seamless pure white, a cutout-ready backdrop〔常用〕
- 纯黑背景 → pure black with only the product edge lit〔常用〕　— 只留产品边缘的光
- 渐变背景 → a gradient darkening outward from the center〔常用〕　— 从中心往外变暗
- 几何色块背景 → geometric color blocks contrasting with the product〔常用〕　— 与产品形成对比
- 水波纹台面 → a rippled surface breaking up the reflection〔常用〕　— 倒影被拉碎
- 大理石台面，冷色调 → a cool-toned marble counter〔常用〕
- 与水同色的亚克力缸 → an acrylic tank〔常用〕　— 产品半浸

> C · 光效

### 光效（10）

- 大面积柔光箱在正上方，光很匀 → a large softbox directly overhead, very even〔常用〕
- 两侧各一块柔光板 → soft panels both sides leaving a vertical highlight〔常用〕　— 圆柱形产品用
- 顶部条光 → a strip light pulling one long highlight〔常用〕　— 在瓶身上拉出一条长高光
- 底光从亚克力台面透上来 → light coming up through an acrylic base〔常用〕
- 柔光加一块反光板补暗部 → soft key with a bounce filling the shadows〔常用〕
- 硬光加黑卡挡出明确的明暗交界 → hard light with black cards cutting the edge〔常用〕
- 聚光灯打出一小块圆斑 → a spotlight throwing one small pool〔常用〕
- 侧逆光勾出产品轮廓 → a rim of backlight tracing the silhouette〔常用〕
- 背光加柔和反射 → backlight with soft reflections to bring out transparency〔常用〕　— 玻璃杯／香水／护肤瓶／亚克力
- 高质感商业灯光配清晰阴影 → high-end commercial lighting with defined shadows〔常用〕

> D · 保真要求

### 保真要求（14）

- 保持产品的真实形状和材质 → keep the product's true shape and material〔常用〕　— ⭐ 产品图必写：不写模型会改形
- 保持产品原有形状、颜色和标签不变 → keep the product's original shape, colour and label unchanged〔常用〕
- 不要改变产品的结构、颜色和材质 → do not change the product's structure, colour or material〔常用〕
- 不要改变产品的比例和体积感 → do not change the proportions or volume〔常用〕
- 不要让产品弯曲或变形 → do not bend or distort the product〔常用〕
- 不要添加原产品没有的部件 → do not add parts the product does not have〔常用〕
- 材质要符合实物（哑光不要拍成亮面） → the finish must match reality〔常用〕
- 产品标签朝前 → the label faces the camera and stays readable〔常用〕　— 清晰可读
- 标志的位置与朝向保持不变 → keep the logo position and orientation〔常用〕
- 包装上的文字保持原样 → keep the packaging text exactly as it is〔常用〕　— 不要改写
- 颜色以参考图为准 → match the colour to the reference〔常用〕　— 不要偏色
- 保持参考图里的配色不变 → keep the reference palette〔常用〕
- 背景与产品同色系 → same hue behind〔常用〕　— 只靠明度拉开
- 主色取自品牌色 → primary colour taken from the brand palette〔常用〕

## 食物饮品

> A · 摆盘与餐具

### 摆盘（13）

- 主菜在中心 → the main centered〔常用〕　— 配菜围着摆一圈
- 用负空间把食物挤到一边 → negative space pushing the food to one side〔常用〕
- 桌面上留大片空白 → lots of empty table〔常用〕　— 食物只占一角
- 俯拍（餐具围成一圈） → top-down with cutlery circling the frame edge〔常用〕　— 餐具沿画面边缘排成圈
- 四十五度角或正俯拍 → a 45-degree or straight top-down angle〔常用〕　— 两个习惯角度，选一个
- 酱汁在盘底画一道弧 → a single arc of sauce across the plate〔常用〕　— 用勺背在盘底拖出一道弧线
- 只在食物上撒几粒盐和一点香草 → a few salt flakes and a sprig of herbs〔常用〕
- 少量配菜道具 → a few garnish props that do not steal focus〔常用〕　— 不抢主体
- 刀叉斜放在盘子外侧 → cutlery set at an angle outside the plate〔常用〕
- 掰开一半露出内里 → one half broken open to show the inside〔常用〕　— 展示切面和内馅
- 饮品杯壁上有冷凝水 → condensation on the glass〔常用〕　— 旁边散几块冰
- 冰镇过的杯壁起雾 → a chilled glass fogged with condensation〔常用〕
- 手正伸进画面 → a hand just entering the frame〔常用〕

### 食物质感（9）

- 食物新鲜真实 → food that looks fresh and real〔常用〕　— 有自然的油光
- 面包外壳脆硬 → a hard crust with strands pulling apart〔常用〕　— 欧包的外壳硬脆，掰开时内部有拉丝
- 焦褐色的边 → charred at the edges〔常用〕　— 表面煎到焦褐（美拉德反应），切开中间还是嫩的
- 焦糖化表面 → a caramelized top with a glossy crust〔常用〕　— 脆壳反光
- 酱汁浓稠 → a thick sauce coating the back of a spoon〔常用〕　— 挂得住勺背
- 汤汁表面有一层油光 → a sheen of fat on the surface of the broth〔常用〕
- 拉丝的奶酪 → melted cheese still strung〔常用〕　— 丝还连着
- 冰激凌边缘开始化 → ice cream just starting to melt〔常用〕　— 挂着水珠
- 切面清晰 → the cut surface is crisp〔常用〕　— 汉堡／蛋糕／水果类

### 餐具（11）

- 素白瓷盘 → a plain white porcelain plate〔常用〕　— 没有花纹
- 粗陶碗 → a rustic bowl with uneven glaze〔常用〕　— 釉面不均匀
- 原木托盘 → a raw wood tray with visible grain〔常用〕　— 木纹清楚
- 亚麻餐巾 → a linen napkin draped beside the plate〔常用〕　— 随意搭在盘子边上
- 铜锅 → a copper pot catching warm light on its walls〔常用〕　— 锅壁反着暖光
- 薄玻璃杯 → thin glass showing the colour behind it〔常用〕　— 杯壁透出对面的颜色
- 深色石板当盘子用 → a dark slate slab used as a plate〔常用〕
- 竹蒸笼 → a bamboo steamer just opened〔常用〕　— 盖子掀开还在冒气
- 旧砧板 → a worn board covered in knife marks〔常用〕　— 刀痕累累
- 一双漆筷 → lacquered chopsticks resting on a holder〔常用〕　— 架在筷托上
- 银质刀叉 → polished silver cutlery〔常用〕　— 反光很亮

> B · 光线与氛围

### 光线（7）

- 侧逆光 → back-side light glowing through the edges〔常用〕　— 食物的边缘被照透
- 顶部柔光加一块反光板补暗部 → a soft top light with a bounce card〔常用〕
- 窗边的自然光 → window light raking in from the front left〔常用〕　— 从左前方斜进来
- 深色背景配单侧光 → a dark ground with single-side light〔常用〕　— 主体像浮在暗处
- 逆光穿过半透明的食物 → backlight passing through translucent food〔常用〕
- 蒸汽被逆光照亮成一条条白线 → steam lit from behind into white threads〔常用〕
- 冷光加冰霜感 → cold light with condensation beading the glass〔常用〕　— 杯壁结着水珠

### 氛围（6）

- 干净的餐桌 → a clean dining table with natural light〔常用〕　— 光线自然
- 桌布有自然的褶皱 → a creased tablecloth with a fork beside〔常用〕　— 旁边放着一把叉子
- 木质桌面 → a wooden table with a dulled sheen〔常用〕　— 有一层用旧的暗哑光泽
- 背景是虚化的厨房 → a blurred kitchen behind〔常用〕　— 能看见一点热气
- 晨光从百叶窗斜切进来 → morning light cut into strips by blinds〔常用〕　— 一道一道
- 深色亚麻布 → dark linen with one pool of light on the food〔常用〕　— 只留一束光在食物上

## 抽象概念

> A · 形态

### 抽象形态（27）

- 流动的色块 → flowing color fields with soft edges〔常用〕　— 大片颜色互相渗透，没有明确边界
- 大面积渐变色域 → a large gradient field with no hard edge〔常用〕　— 整片区域是渐变，没有硬边
- 流体渐变 → an iridescent fluid gradient〔常用〕　— 颜色像油膜一样流动，带虹彩
- 液态金属 → liquid metal with a moving surface〔常用〕　— 像水银一样，表面一直在缓慢流动
- 粒子云 → a particle cloud thinning outward from the center〔常用〕　— 一堆粒子聚成云，中心最密、往外越稀
- 烟雾缠绕 → coiling smoke that never holds a shape〔常用〕　— 烟在空气里缠绕变形，没有固定形状
- 光的碎片 → shards of light scattering like broken glass〔常用〕　— 光被切成一块块碎片向外飞散
- 破碎的镜面 → a shattered mirror〔常用〕　— 镜子碎成很多块，每一块反射的角度都不同
- 水晶棱镜 → a crystal prism splitting light into bands〔常用〕　— 光穿过棱镜被分成几条不同颜色的光
- 线条相互交织成网 → lines interlacing into a mesh〔常用〕　— 很多线互相穿插，织成一张网
- 涟漪从中心一圈圈扩散 → ripples spreading ring by ring from the center〔常用〕　— 水面被打一下，波纹一圈圈往外推
- 同心圆扩散 → concentric circles radiating out〔常用〕　— 从中心一圈圈往外放的圆，视线被拉向圆心
- 一道贯穿画面的斜线 → a single diagonal cutting across the frame〔常用〕
- 细密噪点与颗粒覆盖整张图 → fine noise and grain over the whole frame〔常用〕　— 细小的噪点铺满画面，像胶片颗粒
- 分形 → fractal〔常用〕　— 旧译别名：Fractal
- 分形结构，自相似 → a self-similar fractal structure〔常用〕　— 放大后每一小块都和整体长得一样
- 斐波那契数列 → Fibonacci〔常用〕
- 黄金螺旋 → a golden spiral〔常用〕　— 按黄金比例一圈圈放大的螺旋
- 等距立方体堆叠 → stacked isometric cubes〔常用〕　— 等距视角下把立方体叠起来
- 圆形与六边形网格叠加 → overlapping circles over a hexagonal grid〔常用〕　— 两种网格叠在一起，产生干涉感
- 立方体堆叠成不规则的山 → cubes stacked into an irregular mass〔常用〕　— 大小不一的立方体堆出一座不规则的体块山
- 电子电路 → electronic circuitry〔常用〕　— 旧译别名：Electronic Circuitry
- 坐标网格与刻度线 → a coordinate grid with tick marks〔常用〕　— 带刻度的网格，像坐标纸
- 单向箭头 → a single directional arrow〔常用〕
- 无限循环的箭头 → a looping infinity arrow〔常用〕　— 首尾相接的箭头，表示循环
- 十字准星 → a crosshair〔常用〕　— 交叉的细线，像瞄准镜
- 三个同心圆组成的靶心 → a bullseye of three concentric rings〔常用〕

### 几何（12）

- 球体 → a sphere with an even matte surface〔常用〕　— 表面是均匀的哑光
- 多面体 → a polyhedron with every face catching light〔常用〕　— 由多个平面组成的立体，每个面反光方向都不同
- 四棱锥 → a pyramid with hard edges〔常用〕　— 底面是四边形的锥体，棱线锐利
- 球面网格 → a sphere wrapped in a latitude-longitude grid〔常用〕　— 像地球仪那样用经纬线包住球
- 莫比乌斯环 → a Möbius strip with a single surface〔常用〕　— 把纸带拧半圈接上，只有一个面、一条边
- 剪影 → silhouette〔常用〕　— 背景亮、主体全黑，只剩一个轮廓，看不出五官
- 印刷网点 → halftone dots〔常用〕　— 网点从大到小排列，远看是一个渐变
- 圆点阵列 → a dot field fading from dense to sparse〔常用〕　— 点阵从密到疏渐变，形成方向的暗示
- 虚线框 → a dashed box marking out a region〔常用〕　— 用虚线画出范围，提示这块是要强调的
- 编号标签 → numbered callout tags〔常用〕　— 带数字的小标签加引线，像工程图纸上的标注
- 一个对勾 → a check mark〔常用〕　— 明确表示肯定
- 一个叉号 → a cross mark〔常用〕　— 明确表示否定

> B · 纹样

### 纹样（15）

- 曼陀罗 → mandala〔常用〕　— 从中心向外对称展开的圆形图案，源自佛教坛城 旧译别名：Mandala
- 祥云纹 → auspicious cloud pattern〔常用〕　— 中国传统吉祥纹样，云头卷曲成套
- 回纹边框 → meander border pattern〔常用〕　— 由连续方形回折组成的边框纹
- 鱼鳞纹 → a fish-scale pattern〔常用〕　— 像鱼鳞一样层层叠压的半圆排列
- 碎裂纹 → crackle glaze〔常用〕　— 不规则的裂纹遍布表面，像冰裂或瓷器开片
- 花卉纹样 → floral pattern〔常用〕
- 宽条纹 → wide vertical stripes at even spacing〔常用〕　— 等宽等距的竖条
- 细格纹 → a fine check〔常用〕　— 细密的方格，像衬衫布
- 千鸟格 → houndstooth〔常用〕　— 由小方块拼成的锯齿状格纹
- 波尔卡圆点 → polka dots〔常用〕　— 均匀排布的小圆点
- 豹纹 → leopard spots〔常用〕
- 斑马纹 → zebra stripes〔常用〕　— 黑白相间
- 大理石纹 → marble veining that forks naturally〔常用〕　— 石头的纹路自然分叉延伸，没有规律
- 水磨石纹 → terrazzo with stones of mixed size〔常用〕　— 满地小石子嵌在底色里，大小颜色都不同
- 洛阳花石纹 → Luoyang flower-and-stone pattern〔可用〕　— 旧译别名：Luo Yang Flower Stone Pattern

## 文字平面

> A · 图表与信息元件

### 信息图元件（23）

- 技术画 → a technical drawing with annotations〔常用〕　— 像工程图纸一样标注 旧译别名：Technical drawing
- 蓝图 → blueprint〔常用〕　— 蓝底白线的制图 旧译别名：Blueprint
- 线框图 → a wireframe drawing〔常用〕　— 旧译别名：Wireframe drawing
- 剖面图 → a cutaway〔常用〕　— 旧译别名：cutaway
- 爆炸图 → an exploded view〔常用〕　— 零件沿轴线拉开
- 户型图 → a floor plan seen from directly above〔常用〕　— 从正上方看平面布局
- 细线图表 → a thin-line chart with the data line only〔常用〕　— 只留数据线，去掉网格与边框
- 柱状图 → a bar chart with a shared baseline〔常用〕　— 柱子底部对齐
- 饼图 → a pie chart labeling only the largest slice〔常用〕　— 只标最大的一块
- 趋势图 → a trend illustration〔常用〕　— 旧译别名：trend illustration
- 时间轴 → a timeline with nodes on a single line〔常用〕　— 节点串在一条横线上
- 流程图 → a flowchart of boxes and arrows〔常用〕　— 方框加箭头
- 对比表格 → a two-column comparison table〔常用〕　— 两列并排
- 图标组 → an icon set with a consistent stroke width〔常用〕　— 统一线宽
- 进度条 → a progress bar with a clear filled remainder〔常用〕　— 填充与未填充对比清楚
- 圆角矩形标注框 → a rounded callout box with a leader line pointing to the subject〔常用〕　— 一条引线指向主体
- 三到五个彩色圆点当图例 → three to five coloured dots as a legend〔常用〕
- 一条粗横线当分区标题 → a thick horizontal rule acting as a section heading〔常用〕
- 数字用超大字号单独占一块 → the number set very large in its own block〔常用〕
- 关键数字放大到正文的三倍 → key figures set at triple body size〔常用〕
- 箭头连接前后两步 → an arrow connecting two steps〔常用〕
- 地图标注点 → a map pin with a leader line〔常用〕　— 带一条引线
- 半调网点做的明暗过渡 → a halftone dot gradient〔常用〕

> B · 排版与字体

### 版式（12）

- 正文只用宋体、黑体、楷体三种 → body text in serif〔常用〕　— 其他字体整段排会累
- 一页里最多两个中文字体家族 → at most two Chinese type families per page〔常用〕　— 加载与统一性双重考虑
- 字号档位不超过六档 → no more than six type sizes〔常用〕　— 档位多了层级贬值
- 字重从细到粗拉开档次 → full weight range from light to heavy〔常用〕　— 只有两档时层级全靠字号撑
- 大标题的字距收紧 → tight letter-spacing on large headings〔常用〕　— 大字号下空隙会被放大
- 正文行长收住 → line length capped around 30 characters〔常用〕　— 行长失控是可读性问题里排第一的
- 数字用等宽数位对齐 → tabular figures for numbers〔常用〕　— 数字宽度不等会让列左右抖动
- 竖排文字 → vertical writing〔常用〕　— 适合书脊式标题、诗词、目录
- 标题压在图上 → the title over the image on a darkened band〔常用〕　— 底下垫一层压暗
- 网格对齐 → everything snapped to one grid〔常用〕　— 所有元素贴同一条基线
- 信息密度低 → low density〔常用〕　— 留出大块呼吸空间
- 中英文混排 → mixed Chinese and Latin〔常用〕　— 英文用小一号的字重

### 字体（10）

- 思源黑体 → Noto Sans SC〔常用〕　— 免费商用(OFL)；当默认正文不会错
- 思源宋体 → Noto Serif SC〔常用〕　— 免费商用(OFL)；Heavy 字重可当大标题
- 霞鹜文楷 → LXGW WenKai〔常用〕　— 免费商用(OFL)；适合文艺、教育、引言
- 霞鹜新晰黑 → LXGW Neo XiHei〔常用〕　— 免费商用
- 汇文明朝体 → Huiwen Mingchao〔常用〕　— 免费商用；适合书封、文化类
- 京华老宋体 → Jinghua Old Song〔常用〕　— 免费商用；标题专用
- 源流明体 → GenRyuMin〔常用〕　— 免费商用(OFL)；繁体内容首选
- 未来荧黑 → Glow Sans〔常用〕　— 免费商用(OFL)；压缩宽度可做窄长大标题
- MiSans → MiSans〔常用〕　— 免费商用；界面原型合适
- 得意黑 → Smiley Sans〔常用〕　— 免费商用(OFL)；标题专用，正文用会晕

> C · 海报与规格

### 海报元素（6）

- 顶部标题、中心主体、底部信息区 → title on top, subject in the centre, information block at the bottom〔常用〕　— ⭐ 最稳的海报层级配方
- 大标题加一行副标题 → a large headline with one line of subheading〔常用〕
- 三个卖点标签 → three selling-point tags〔常用〕　— 课程／产品海报
- 底部保留价格和按钮区域 → leave room for price and button〔常用〕　— 电商促销；具体数字交给后期
- 主体占画面约五成半 → the subject fills about 55% of the frame〔常用〕　— 信息流广告
- 画面里只出现引号内的文字 → only the text inside the quotation marks appears in the image〔常用〕　— ⭐ 控制图中文字最有效的一句

### 平台规格（5）

- 竖版图文笔记 → vertical image post〔常用〕　— 1080×1440，三比四
- 图文笔记一套 → a set of 1 cover + 4-8 content pages + 1 summary page〔常用〕
- 自媒体封面主图 → article cover〔常用〕　— 标题放在中偏左的清晰安全带里，避免中间发空
- 自媒体方形封面 → square cover〔常用〕　— 默认只放短标题、大字居中，不放图
- 方图里的短标题压到四到十个字 → keep the square-cover title to 4-10 characters〔常用〕　— 不要把横版长标题硬塞进方图

## 旧库补充-主体

> 原有分类

### 眼睛（46）

- 细节的美丽的眼睛 → detailed beautiful eyes〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 发光的眼睛 → glowing eyes〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 一只眼睛被覆盖 → one eye covered〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 用绷带包扎一只眼睛 → bandage over one eye〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 睁着眼睛哭 → crying with eyes open〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 疯狂的眼睛 → crazy eyes〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 下眉毛 → furrowed brow〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 多色的眼睛 → multicolored eyes〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 一字型瞳孔/挖眼 → horizontal pupils〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 钻石型瞳孔 → diamond-shaped pupils〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 没有眼睛 → no pupils〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 空洞眼睛 → empty eyes〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 白眼球 → blank eyes〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 漆黑的眼睛 → hollow eyes〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 收缩的瞳孔 → constricted pupils〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 符号眼 → symbol-shaped pupils〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 星形眼睛 → star-shaped pupils〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- X形眼睛 → x-shaped pupils〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 眼镜反射 → eye reflection〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 闭上一只眼 → one eye closed〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 闭眼 → eyes closed〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 闭一只眼 → wince〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 盯着看 → eyeball〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 水汪汪大眼睛 → aqua eyes〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 半闭的眼睛 → half-closed eye〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 挡在头发下的眉毛 → eyebrows behind hair〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 渐变眼 → gradient_eyes〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 竖瞳孔/猫眼 → slit pupils〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 下垂的眼睛 → tareme〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 恶魔的瞳孔 → devil pupils〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 蛇瞳孔 → snake pupils〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 异色瞳孔 → heterochromia〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 紫眼 → purple eyes〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 红眼 → red eyes〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 白眼 → white eyes〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 金眼 → yellow eyes〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 橙色的眼睛 → orange eyes〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 上翘的眼睛 → upturned eyes〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 睁开的眼睛 → wide-eyed〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 眼圈 → ringed eyes〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 闪闪发光瞳 → pupils sparkling〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 花型瞳孔 → flower-shaped pupils〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 美瞳 → color contact lenses〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 实心圆眼睛 → solid circle eyes〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 心形眼 → heart-shaped eyes〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 粉红色的眼睛 → pink eyes〔可用〕　— 旧库保留；按目标模型与具体场景选择。

### 耳朵（24）

- 动物耳朵 → animal ears〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 仿制的动物耳朵 → fake animal ears〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 狐狸耳朵 → fox ears〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 狗耳 → dog ears〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 老鼠耳 → mouse ears〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 熊耳朵 → bear ears〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 牛耳朵 → cow ears〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 鹿耳朵 → deer ears〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 浣熊耳朵 → raccoon ears〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 山羊耳朵 → goat ears〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 马耳 → horse ears〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 兔子耳朵 → rabbit ears〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 狮子耳朵 → lion ears〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 猴耳朵 → monkey ears〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 熊猫耳朵 → panda ears〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 皮卡丘耳朵 → pikachu ears〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 猪耳朵 → pig ears〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 羊耳朵 → sheep ears〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 松鼠耳朵 → squirrel ears〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 狼耳朵 → wolf ears〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 蝙蝠耳朵 → bat ears〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 尖尖的长耳朵 → long pointy ears〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 遮住耳朵 → covering ears〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 月牙耳环 → crescent earrings〔可用〕　— 旧库保留；按目标模型与具体场景选择。

### 身材、人物部位（5）

- 肌肉 → muscle〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 强壮 → strong〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 颈部以上 → Close-Up(CU)〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 人占 3/4 → Long Shot(LS)〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 特写 → Close-up〔可用〕　— 旧库保留；按目标模型与具体场景选择。

### 发型（85）

- 刘海遮眼 → hair over eyes〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 刘海遮单眼 → hair over one eye〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 刘海分开 → parted bangs〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 很长的头发 → very long hair〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 波浪 → wavy hair〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 公主卷 → drill hair〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 自然卷 → wavy hair〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 翘发 → flipped hair〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 短马尾 → short ponytail〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 前马尾 → front ponytail〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 四马尾 → quad tails〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 编织马尾辫 → braided ponytail〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 折叠马尾辫 → folded ponytail〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 单辫 → single braid〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 低双辫 → low twin braids〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 侧编辫 → side braid〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 冠型织辫 → crown braid〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 法式辫子 → french braid〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 辫子髻 → braided bun〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 单发髻 → single hair bun〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 双发髻 → double bun〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 锥形发髻 → cone hair bun〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 甜甜圈发髻 → doughnut hair bun〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 心型发髻 → heart hair bun〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 侧绑发 → one side up〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 双侧绑发 → two side up〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 多绑头发 → multi-tied hair〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 顶绑发 → topknot〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 包子头 → hair bun〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 包子头(两个) → double bun〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 湿发 → wet hair〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 非对称发型 → asymmetrical hair〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 窗帘/瀑布发型 → curtained hair〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 双团子头 → double bun〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 双钻头卷 → twin drills〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 多钻头卷 → quad drills〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 单侧钻头卷 → side drill〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 带着尖角的发型 → pointy hair〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 团子头 → hair bun〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 双辫子 → twin braids〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 折叠马尾 → folded ponytail〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 圆环发髻 → doughnut hair bun〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 心形发髻 → heart hair bun〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 遮盖头发稀少的部分 → comb over〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 富有表现力的头发 → expressive hair〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 大呆毛 → huge ahoge〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 秃头女孩 → bald girl〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 锅盖头 → bowl cut〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 心形呆毛 → heart ahoge〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 帽盔式发型 → undercut〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 玉米垄发型 → cornrows〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 弓型头发 → bow-shaped hair〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 前辫 → front braid〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 多股麻花辫 → multiple braids〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 三股辫 → tri braids〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 四股辫 → quad braids〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 三发髻 → triple bun〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 单发圈 → single hair ring〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 只扎了一边头发 → one side up〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 低辫长发 → low-braided long hair〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 角发 → mizura〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 多扎头发 → multi-tied hair〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 日本发 → nihongami〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 两股辫子大小不一样 → uneven twintails〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 三股辫子 → tri tails〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 五股辫子 → quin tails〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 超大鸟窝头 → huge afro〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 莫霍克发型 → mohawk〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 蓬松感油头 → quiff〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 头发遮住了一只眼 → hair over one eye〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 垂下的长鬈发 → hair slicked back〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 披在两侧的两条辫子 → high ponytail〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 中等长发 → medium hair〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 披在两侧的发髻 → side bun〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 尾部散开的单马尾发型 → split ponytail〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 小型双股辫 → two side up〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 超长的头发 → absurdly long hair〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 触手头发 → tentacle hair〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 很短的头发 → very short hair〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 耳前发 → sidelocks〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 单耳前发 → single sidelock〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 侧发后梳 → half updo〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 一侧绑发 → hair one side up〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 漂浮的头发 → floating hair〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 头发很多的 → big hair〔可用〕　— 旧库保留；按目标模型与具体场景选择。

### 发色（5）

- 棕色头发 → brown hair〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 茶发 → brown hair〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 粉色头发 → pink hair〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 蓝色头发 → blue hair〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 多彩头发 → multicolored hair〔可用〕　— 旧库保留；按目标模型与具体场景选择。

### 主体、角色（16）

- 男人 → man〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 女人 → woman〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 魔术师/魔法师 → mage〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 萝莉 → loli〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 正太 → shota〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 魔幻少女 → multiple_girls〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 男服务员 → waiter〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 女服务员 → waitress〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 忍者/日本武士 → ninja〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 同学 → classmate〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 小精灵 → fairy〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 魅魔 → succubus〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 魔鬼(撒旦) → devil〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 兽人/半兽人 → furry/orc〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 迷你女孩 → minigirl〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 兽耳萝莉模式 → kemonomimi mode〔可用〕　— 旧库保留；按目标模型与具体场景选择。

### 表情、情绪（79）

- 腮红脸红 → blush〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 满脸腮红 → full-face blush〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 可爱的脸 → cute face〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 脸色苍白 → pale〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 叹息 → sigh〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 高潮 → orgasm〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 开心 → Happy〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 黑暗 → Dark〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 残酷 → Brutal〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 讨厌 → Hateful〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 喜怒无常 → Moody〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 食物在脸上 → food on face〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 鼻血 → nosebleed〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 生气的 → angry〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 苦恼的 → annoyed〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 疯狂的 → crazy〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 害羞的 → shy〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 尴尬的 → embarrassed〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 困乏的 → sleepy〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 悲伤的 → sad〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 喝醉的 → drunk〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 尖牙 → fangs〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 舌头 → tongue〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 没有鼻子 → no nose〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 唾液 → saliva〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 胡子 → facial hair〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 嘴咬住 → mouth hold〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 哭 → crying〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 气的冒烟（漫画） → fume〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 整张脸泛红 → full-face blush〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 有决心的 → determined〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 失望的 → disappointed〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 蔑视 → disdain〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 恶心 → disgust〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 有罪的 → guilt〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 孤独的 → lonely〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 扬起的眉毛 → raised eyebrow〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 强硬的表情 → rape face〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 压抑的郁闷的 → depressed〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 担忧的 → worried〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 累 → tired〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 沉思的 → pensive〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 格拉斯哥微笑 → glasgow smile〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 恐惧表情 → horrified〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 伸出舌头 → oral invitation〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 害怕的 → scared〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 怒视、嫌弃、不满 → scowl〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 严肃的 → serious〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 惊讶或无语 → spit take〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 流口水 → drooling〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 诱惑的表情 → torogao〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 牙 → teeth〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 下流的表情 → naughty face〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 忍耐的表情 → endured face〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 在笑的 → laughing〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 唾液拉丝 → saliva trail〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 虎牙状 → skin fang〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 长舌头 → long tongue〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 额头 → forehead〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 淡淡的腮红 → light blush〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 无聊的 → bored〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 悲观情绪 → gloom〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 表达式 → expression〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 嫉妒的 → jealous〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 不安的 → nervous〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 阴沉的 → shaded〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 无口 → expressionless〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 表情 → expressions〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 明亮的瞳孔 → bright pupils〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 耳红 → ear blush〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 诱人的微笑 → seductive smile〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 笑脸 → smiley〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 傻笑/得意的笑 → smirk〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 慌乱的 → flustered〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 眼里冒爱心 → heart in eye〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 呻吟 → moaning〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 青筋 → anger vein〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 表情贴纸 → blush stickers〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- V形眉 → v-shaped eyebrows〔可用〕　— 旧库保留；按目标模型与具体场景选择。

## 旧库补充-场景

> 原有分类

### 天气、灯光、光线（69）

- 黄金时段照明 → golden hour lighting〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 傍晚背对阳光 → against backlight at dusk〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 满月 → full moon〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 晚上 → night〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 强阴影 → intense shadows〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 雨中 → in the rain〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 柔和的雾 → smooth fog〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 暴风雨的海面 → stormy ocean〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 海洋背景 → ocean backdrop〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 白昼的光线 → Crepuscular Rays〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 背景光 → Backlight〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 黄金时段光线 → Golden hour light〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 灰尘 → Dust〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 放射性发光体 → Glow Radioactive〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 量子点 → Quantum Dot〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 自然照明 → Natural Lighting〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 太阳光 → Sun light〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 美丽的照明 → Beautiful Lighting〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 激励的照明 → Motivated lighting〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 轮廓光 → Rim light〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 体积照明 → Volumetric Lighting〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 工作室照明 → Studio lighting〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 明亮的光线 → Bright Light〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 反光 → Reflection Light〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 映射光 → Mapping Light〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 情调光 → Mood Lighting〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 黄金时段光 → Golden Hour Light〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 明亮的 → Bright〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 情绪照明 → Mood Lighting〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 柔软的光线 → Soft Light〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 雾气朦胧 → Misty Foggy〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 残酷的 → Brutal〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 强烈对比的 → Dramatic Contrast〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 忧郁氛围 → Moody Atmosphere〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 强光 → Dramatic Light〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 柔和月光 → Soft Moonlight〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 层次光 → Volumetric Lighting〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- OC渲染效果 → Octane Render〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 黄昏射线 → Crepuscular Rays〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- UE5效果 → Unreal Engine 5〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 外太空观 → Outer Space View〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 电影光 → Cinematic Light〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 强光逆光 → Intense Backlight〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 立体光 → Volumetric Light〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 闪光灯光 → Shimmering Light〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 反射效果 → Reflection Effect〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 柔和的照明 → Soft Illumination〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 柔光 → Soft Lights〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 投影效果 → Projection Effect〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 发光效果 → Glow Effect〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 浪漫烛光 → Romantic Candlelight〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 好看的灯光 → Beautiful Lighting〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 渲染效果 → Raytracing〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 戏剧灯光 → Dramatic Lighting〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 阴影效果 → Shadow Effect〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 戏剧光 → Dramatic Light〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 伦勃朗照明 → Rembrandt Lighting〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 明暗分明 → Stark Shadows〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 分体照明 → Split Lighting〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 黑暗氛围 → Moody Darkness〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 前灯 → Front Lighting〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 鲜艳色彩 → Vibrant Color〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 背光照明 → Backlighting〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 干净的背景趋势 → Clean Background Trending〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 安静恬淡 → Serene Calm〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 边缘灯光 → Rim Lights〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 星密 → Winking Stars〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 全局照明 → Global Illumination〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 柔和烛光 → Soft Candlelight〔可用〕　— 旧库保留；按目标模型与具体场景选择。

### 背景（1）

- 简单花纹背景 → simple patterned background〔可用〕　— 旧库保留；按目标模型与具体场景选择。

### 场景（69）

- 海滩上 → on the beach〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 好天 → beautiful detailed sky,〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 好水 → beautiful detailed water〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 落日 → sunset〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 在大海上 → on the ocean〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 草地 → in a meadow〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 夏威夷 → in hawaii〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 罗马街道 → in the romanesque architecture streets〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 在街上 → in the street〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 建筑 → building〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 星巴克 → starbucks〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 圣诞节 → christmas〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 户外 → outdoors〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 公园 → park〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 远处的建筑 → Buildings in the distance〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 小岛 → islet〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 湖边 → lakeside〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 玫瑰花瓣 → rose petals〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 花瓣 → petals〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 花 → flower〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 在城堡里 → in the castle〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 幻想 → fantasy〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 异想天开 → whimsically〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 街景 → street scenery〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 宇宙 → universe I cosmos〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 在晨露中 → In the morning mist〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 充满阳光 → full of sunlight〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 疯狂麦斯沙地风格 → mad max〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 杂草丛生的 → overgrown nature〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 天空之城 → Castle in the Sky〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 太空 → Space〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 飞溅的油漆 → Splatter Paint〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 徽标 → Logo〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 大理石雕像 → Marble Statue〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 细菌 → Molecular〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 核电 → Nuclear〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 美国国家航空航天局 → NASA〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 轨道 → Orbital〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 工业城市景观 → Industrial cityscape〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 火星 → Red planet〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 时光穿越城市景观 → Time travel cityscape〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 襄博朋克城市 → Cyberpunk city〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 超现实主义风景 → Surreal landscape〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 星空夜景 → Starry night sky〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 蒸汽朋克城市景观 → Steampunk cityscape〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 雨 → Rain〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 在晨雾中 → In the morning mist〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 蹇博朋克街道 → Cyberpunk street〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 神秘寺庙 → Mystic temple〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 蒸汽动力机械 → Steam-powered machinery〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 巨大建筑 → Giant Architecture〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 迷人花园 → Enchanted Garden〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 后启示录世界 → Post-Apocalyptic World〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 反乌托邦景观 → Dystopian Landscape〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 迷失废墟 → Lost ruins〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 极光北极 → Aurora Borealis〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 暴走机甲小巷 → Cyberpunk Alley〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 神秘森林 → Mystical Forest〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 荒漠孤烟 → Desolate Desert〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 后启示录 → Post apocalyptic〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 神活世界 → Mythical world〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 外太空 → Outer Space〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 魔幻森林 → Magical Forest〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 末日废城 → Apocalypse Ruins〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 星球大战 → Star Wars〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 火星深险 → Mars Exploration〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 科技城市 → Technological City〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 飞檐 → upturned eaves〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 斗拱 → bracket set〔可用〕　— 旧库保留；按目标模型与具体场景选择。

## 旧库补充-姿势

> 原有分类

### 腿部动作（6）

- 抱腿 → holding legs〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 抬起腿 → leg up〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 张开双腿 → spread legs〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 双腿之间的手 → hand between legs〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 手放在自己的大腿上 → hands on own thighs〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 手在腿下 → hands under legs〔可用〕　— 旧库保留；按目标模型与具体场景选择。

### 手部动作（17）

- 抬手 → arms up〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 张手 → spread arms〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 张开双手 → open hands〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 张开手指 → spread fingers〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 嘘手势 → shushing〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 比出中指 → middle finger〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 双手紧握 → interlocked fingers〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 手放在身后 → arms behind back〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 将手藏起来 → hidden hands〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 展示腋窝 → presenting armpit〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 用手支撑住 → arm support〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 舔手指 → finger to mouth〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 双手相合 → own hands together〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 双手V手势 → double peace pose〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 手托乳房 → breast lift〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 手伏在乳房上 → breast suppress〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 胜利手势 → victory sign〔可用〕　— 旧库保留；按目标模型与具体场景选择。

### 整体姿势（26）

- 身体前驱 → leaning forward〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 颠倒的 → upside-down〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 弯腰 → squatting〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 拍头 → headpat〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 弓身体 → arched back〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 趴着翘臀 → top-down bottom-up〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 翘臀姿势 → bent over〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 四肢趴地 → all fours〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 猫一样的姿势 → claw pose〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 站立一字马 → standing split, leg up〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 双膝并拢脚分开 → knees together feet apart〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 手夹在腿间 → hand between legs〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 内八 → pigeon-toed〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- M字腿 → m legs〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 眼对眼 → eye contact〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 向后看 → looking back〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 手放在自己的胸前 → hand on own chest〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 手放头旁边 → arm at side〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 手把腿抓着 → leg hold〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 曲腿至胸 → fetal position〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 靠罕墙 → against wall〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 二郎腿 → crossed legs〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 抽烟 → smoking〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 侧 → on side〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- A字站姿 → A-pose〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- T字站姿 → T-pose〔可用〕　— 旧库保留；按目标模型与具体场景选择。

## 旧库补充-服装

> 原有分类

### 袜子（9）

- 日式厚底短袜 → tabi〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 裤袜 → leggings〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 渔网袜 → fishnet stockings〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 损坏了的过膝袜 → torn thighhighs〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 袜带 → garter_straps〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 吊带袜 → garters〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 长筒袜 → thighhighs〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 裹腿 → legwear〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 印花裤袜 → print legwear〔可用〕　— 旧库保留；按目标模型与具体场景选择。

### 套装（22）

- 宽松连衣裙 → dress〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 纳粹军装 → nazi uniform〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 西装夹克 → Piece Suit〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 商务装 → business suit〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 迷彩服 → camouflage uniform〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 警服 → police uniform〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 网球服 → tennis uniform〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 校服 → school uniform〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 赛车服 → racing suit〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 运动服 → gym uniform〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 圣诞装 → santa〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 圣诞老人服装 → santa costume〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 女仆装 → maid〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 逆兔女郎 → reverse bunnysuit〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 美少女战士制服 → sailor senshi uniform〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 裸体的 → nude〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 露背装 → backless outfit〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 军服 → military uniform〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 高开衩的连身衣 → highleg leotard〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 情趣内衣 → Sex underwear〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 华丽繁琐的服装 → Gorgeous and fussy clothes〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 浴巾 → naked towel〔可用〕　— 旧库保留；按目标模型与具体场景选择。

### 鞋子（3）

- 系带靴 → cross-laced footwear〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 高帮靴 → thigh boots〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 长靴 → boots〔可用〕　— 旧库保留；按目标模型与具体场景选择。

### 上衣（8）

- 胸罩 → bra〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 制服 → uniform〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 职场制服 → business suit〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 束身胸衣 → corset〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 小款背心 → cropped vest〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 湿衬衫 → wet shirt〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 肚兜 → dudou〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 比基尼上衣 → bikini top〔可用〕　— 旧库保留；按目标模型与具体场景选择。

### 下裤（11）

- 比基尼裙 → bikini skirt〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 芭蕾舞短裙 → tutu〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 尿布 → diaper〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 内裤 → panties〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 没内裤 → no panties〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 三角裤 → trefoil〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 丁字裤 → thong〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 日式丁字裤 → fundoshi〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 条纹内裤 → striped panties〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 低腰式内裤 → lowleg panties〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 系带式内裤 → side-tie panties〔可用〕　— 旧库保留；按目标模型与具体场景选择。

## 旧库补充-神话

> 原有分类

### 中国神话（66）

- 盘古，世界的创造者 → Pangu〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 女娲，创世和人类之神 → Nüwa〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 伏羲，人类、知识和文化之神 → Fuxi〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 神农，农业和医药之神 → Shennong〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 嫦娥，月亮和长生不老之神 → Chang'e〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 后羿，弓箭和太阳之神 → Houyi〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 哪吒，保护、勇气和力量之神 → Nezha〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 玉皇大帝，天地之尊和天堂的统治者 → Jade Emperor〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 关羽，战争、忠诚和正义之神 → Guan Yu〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 妈祖，海洋和航海者的守护神 → Mazu〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 二郎神，保护、真理和忠诚之神 → Erlang Shen〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 钟馗，驱鬼和护身之神 → Zhong Kui〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 雷公，雷电之神 → Lei Gong〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 西王母，西方的女王和长生不老之神 → Xi Wangmu〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 玉帝妃，慈悲之神 → Yu Di〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 嫘祖，丝绸和蚕丝之神 → Lei Zu〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 东王公，东方的天和日出之神 → Dong Wang Gong〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 西王母四大天仙，侍奉西王母的四位女神 → Xiwangmu's Four Attendants〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 土地公，土地和土壤之神 → Tu Di Gong〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 观音菩萨，慈悲和同情之神 → Guan Yin〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 吕洞宾，文学和文化之神 → Lu Dongbin〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 韦驮菩萨，武术和佛教的守护神 → Wei Tuo〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 财神，财富和繁荣之神 → Cai Shen〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 三清，道教中的三位最高神 → Sanqing〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 玄武，北方和水、土元素之神 → Xuan Wu〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 张果老，长寿和炼丹之神 → Zhang Guo Lao〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 羲和，太阳和温暖之神 → Xihe〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 后土，土地和丰收之神 → Hou Tu〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 轩辕，农业和黄帝之神 → Xuan Yuan〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 白牡丹，花卉和春天之神 → Bai Mudan〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 蚩尤，战争和雨水之神 → Chi You〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 孟婆，遗忘之神 → Meng Po〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 刘海，财富和繁荣之神 → Liu Hai〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 王母娘娘，西方女王和长生不老之神 → Wang Mu Niang Niang〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 精卫，试图用石头填海的鸟神 → Jingwei〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 董永，孝顺和爱情之神 → Dong Yong〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 福禄寿，财富和长寿的三位神 → Fu Lu Shou〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 九天玄女，战争和性的女神 → Jiutian Xuannu〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 胡天保，公正和正义之神 → Hu Tianbao〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 妈祖，海洋和水手之神 → Matsu〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 闻仲，忠诚和正义之神 → Wen Zhong〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 大禹，治水之神 → Da Yu〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 黄帝，中华文明之神 → Huang Di〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 常羲，月亮和命运之神 → Chang Xi〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 土地公，土地和农业之神 → Tudi Gong〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 谢怜，慈悲和宽容之神 → Xie Lian〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 炎帝，火和农业之神 → Yandi〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 玉龙，雨和雷的龙神 → Yulong〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 风伯，风和雷之神 → Feng Bo〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 祝融，火和战争之神 → Zhu Rong〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 东风，东方之神 → Dong Feng〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 济公，慈悲和智慧的僧人之神 → Ji Gong〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 水庸，水和海之神 → Shui Yong〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 崇礼，长寿之神 → Chongli〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 赵公明，财富和武术之神 → Zhao Gongming〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 鲁班，木工和工程之神 → Lu Ban〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 后土，大地和生育之神 → Houtu〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 后羿，射箭和太阳之神 → Hou Yi〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 天后，海洋女神和天后 → Tianhou〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 王母娘娘，西方女王和长寿女神 → Wangmu Niangniang〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 奎星，考试和学习之神 → Kui Xing〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 观音，慈悲和怜悯之神 → Guanyin〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 鸿钧老祖，道教神话中的神灵和宇宙创造者 → Hongjun Laozu〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 灶君，灶神 → Zao Jun〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 真武，武术之神和北方的保护神 → Zhenwu〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 文昌，文学和教育之神 → Wen Chang〔可用〕　— 旧库保留；按目标模型与具体场景选择。

### 西方希腊诸神（78）

- 阿多尼斯，美和欲望之神 → Adonis〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 埃俄洛斯，风之神 → Aeolus〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 阿伊忒耳，上层大气和光的原初神 → Aether〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 安特洛斯，相互爱之神 → Anteros〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 阿佛洛狄忒，爱、美和欲望之神 → Aphrodite〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 阿波罗，音乐、诗歌、预言和医学之神 → Apollo〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 阿瑞斯，战争、暴力和流血之神 → Ares〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 阿尔忒弥斯，狩猎、月亮和分娩之神 → Artemis〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 阿斯克勒庇俄斯，医药和治愈之神 → Asclepius〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 阿斯特莉亚，正义之女神 → Astraea〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 雅典娜，智慧、战争和手艺之女神 → Athena〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 阿特拉斯，天文和航海之泰坦 → Atlas〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 爱神阿罗拉，黎明女神 → Aurora〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 巴库斯，酒、狂欢和疯狂之神 → Bacchus〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 比亚，力量和权力之女神 → Bia〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 卡吕俄佩，史诗诗歌之缪斯 → Calliope〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 谷物女神瑟莱斯，农业、谷物和生育之神 → Ceres〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 混沌，宇宙的原初神 → Chaos〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 西尔凯，魔法和巫术之女神 → Circe〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 克利奥，历史之缪斯 → Clio〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 克洛诺斯，时间和时代之泰坦神 → Cronus〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 丘比特，爱和吸引之神 → Cupid〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 赛伯勒，弗里吉亚母亲女神 → Cybele〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 狄蜜特，农业、生育和收成之女神 → Demeter〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 黛安娜，狩猎、月亮和分娩之神 → Diana〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 狄俄尼索斯，酒、节庆和狂欢之神 → Dionysus〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 埃希德娜，女人头和蛇身之怪物 → Echidna〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 艾拉托，爱情诗之缪斯 → Erato〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 爱神艾洛斯，爱和欲望之神 → Eros〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 法乌努斯，森林、平原和田野之神 → Faunus〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 福图娜，幸运和命运之女神 → Fortuna〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 格拉斯，衰老之神 → Geras〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 冥王哈迪斯，冥界和死亡之神 → Hades〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 哈尔莫尼亚，和谐和一致之女神 → Harmonia〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 黑卡忒，魔法、巫术和幽灵之女神 → Hecate〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 伊利奥斯，太阳之神 → Helios〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 赫菲斯托斯，火、铁匠和手工艺之神 → Hephaestus〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 赫拉，诸神之后，婚姻的守护神 → Hera〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 赫尔墨斯，商业、偷盗和信使之神 → Hermes〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 赫斯提亚，炉灶、家庭和家族之神 → Hestia〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 海吉亚，健康和卫生之女神 → Hygieia〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 雅努斯，开始和转变之神 → Janus〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 朱诺，诸神之后，婚姻和分娩之神 → Juno〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 朱庇特，诸神之王，天空和雷电之神 → Jupiter〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 火星，战争、暴力和农业之神 → Mars〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 梅尔波门，悲剧之缪斯 → Melpomene〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 水星，商业、偷盗和信使之神 → Mercury〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 米涅瓦，智慧、手艺和战略之神 → Minerva〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 莫菲厄斯，梦之神 → Morpheus〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 涅墨西斯，报复和惩罚之女神 → Nemesis〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 海神尼普顿，海洋、地震和马的神 → Neptune〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 胜利女神尼刻 → Nike〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 潘，牧羊人、羊群和荒野之神 → Pan〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 佩尔塞福涅，冥王后和春天女神 → Persephone〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 恐惧之神福波斯 → Phobos〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 冥王普鲁托，冥界和财富之神 → Pluto〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 保利希米娜，赞美诗之缪斯 → Polyhymnia〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 波塞冬，海神，地震和马的神 → Poseidon〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 塞勒涅，月亮女神 → Selene〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 斯堤克斯，冥河斯堤克斯女神和冥界女神 → Styx〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 特尔普西科莱，舞蹈和合唱之缪斯 → Terpsichore〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 萨莉亚，喜剧和田园诗之缪斯 → Thalia〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 死亡之神塔纳托斯 → Thanatos〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 特里东，海神和海的信使 → Triton〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 乌拉尼亚，天文之缪斯 → Urania〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 乌拉诺斯 → Uranus〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 维纳斯，爱、美和生育之神 → Venus〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 维斯塔，炉灶、家庭和家族之神 → Vesta〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 宙斯，诸神之王，天地之父 → Zeus〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 休底厄斯，光和观察之泰坦 → Hyperion〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 克洛诺斯，时间之泰坦 → Kronos〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 奥创纽斯，海洋之泰坦 → Oceanus〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 普罗米修斯，先见之明和狡猾的建议之泰坦 → Prometheus〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 瑞亚，生育和母亲之泰坦 → Rhea〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 塔耳塔洛斯，深渊的原初之神 → Tartarus〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 忒弥斯，法律和秩序之泰坦 → Themis〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 泰凯，幸运和机遇之女神 → Tyche〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 泽菲洛斯，西风之神 → Zephyrus〔可用〕　— 旧库保留；按目标模型与具体场景选择。

### 埃及神话（11）

- 阿蒙，创造和空气之神 → Amun〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 阿努比斯，死亡和木乃伊之神 → Anubis〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 巴斯特，保护、生育和猫之女神 → Bastet〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 哈索尔，爱、音乐和美丽之女神 → Hathor〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 赫鲁士，天空、王权和胜利之神 → Horus〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 伊西丝，魔法、生育和母性之女神 → Isis〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 玛阿特，真理、正义和和谐之女神 → Ma'at〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 奥西里斯，来世和重生之神 → Osiris〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 荷鲁斯，太阳和创造之神 → Ra〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 塞赫梅特，战争、毁灭和治愈之女神 → Sekhmet〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 托特，知识、写作和智慧之神 → Thoth〔可用〕　— 旧库保留；按目标模型与具体场景选择。

## 旧库补充-质量

> 原有分类

### 画质（77）

- 最高质量 → the best quality〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 杰作 → masterpiece〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 极致的细节 → extreme detail〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 超高清 → ultra-high definition〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 8k → 8k〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 惊人的 → amazing〔可用〕　— 旧库保留；按目标模型与具体场景选择。 旧译别名：Breathtaking
- 原创 → original〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 非常详细的壁纸 → extremely detailed wallpaper〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 非常详细的cg → extremely detailed cg〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 超现实图片 → surreal photo〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 极高分辨率 → incredibly absurdres〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 壁纸 → wallpaper〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 高细节 → high detail〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 高品质 → hyper quality〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 高分辨率 → high resolution〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 全高清.1080P,2K,4K,8K → FHD,1080P,2K,4K,8K〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 8k流畅 → 8k smooth〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 1280 x 720 → 720p〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 1920 x 1080 → 1080p〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 2048 x 1080 → 2K〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 4096 x 2160 → 4K〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 5120 x 2880 → 5K〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 7680 x 4320 → 8K〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 10240 x 4320 → 10K〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 1280 x 720 或 1920 x 1080 → HD〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 3840 x 2160 → UHD〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 全高清 → Full HD〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 8k 流畅 → 8k Smooth〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 8K 分辦率 → 8K Resolution〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 16K 分辦率 → 16K Resolution〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 超清晰 → Super Clarity〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 超高分辨率 → Ultra-high Resolution〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 超高清 HDR → Ultra HD HDR〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 超高清晰度 → Ultra-high Clarity〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 超高清画面 → Ultra HD picture〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 摄影感 → Photography〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 徕卡镜头 → Leica Lens〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 详细细节 → Detailed〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 画面渲染品质关键词 → Keywords for Visual Rendering Quality〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- Arnold 渲染器 → Arnold Renderer〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- V-Ray 渲染器 → V-Ray Renderer〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- Redshift 渲染器 → Redshift Renderer〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- Octane 渲染器 → Octane Renderer〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- C4D 渲染器 → C4D Renderer〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- Blender 渲染器 → Blender Renderer〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- Mental Ray 渲染器 → Mental Ray Renderer〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 散蓝渲染器 → Indigo Renderer〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- Octane 渲染 → Octane Render〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- Maxon Cinema 4D → Maxon Cinema 4D〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 建筑渲染 → Architectural Visualization〔可用〕　— 旧库保留；按目标模型与具体场景选择。 旧译别名：Architectural visualisation
- 着色器 → Shader〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 亚像素采样 → Subpixel Sampling〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 室内渣染 → Indoor Rendering〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- Quixel Megascans → Quixel Megascans〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 渲染 → Rendering〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 超真实 → Hyperrealism〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 环境光遮蔽 → Ambient Occlusion〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 物理渲染 → Physically Based Rendering〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- Monte Carlo 渲染 → Monte Carlo Rendering〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 贴图映射 → Texture Mapping〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- FStorm 渲染器 → FStorm Renderer〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- Corona 渲染器 → Corona Renderer〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 抗锯齿 → Anti-aliasing (AA)〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 体积渲染 → Volume Rendering〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 光线投射 → Ray Casting〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 格点光线追踪 → Grid-based Ray Tracing〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 重要性采样 → Importance Sampling〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- Octane渲染 → Octane render〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- V-ray渲染 → V-ray〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- Corona室内渲染 → Corona render〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- QM渲染 → Quixel megascans render〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- C4D渲染 → Maxon cinema 4D〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 硬边阴影 → hard-edged shadow〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 块状高光 → blocky specular highlight〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 描边线 → outline stroke〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 块面头发 → blocky anime hair〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 次表面散射 → subsurface scattering〔可用〕　— 旧库保留；按目标模型与具体场景选择。

### 细节描述词（138）

- 奇妙细节 → Marvelous Details〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 精美细节 → Exquisite Details〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 惊人的细节 → Stunning Details〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 令人印象深刻的细节 → Impressive Details〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 高级细节 → High Details〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 精细细节 → Fine Details〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 加强细节 → Enhanced Details〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 难以置信的细节 → Incredible Details〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 无与伦比的细节 → Unmatched Details〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 令人惊叹的细节 → Mind-blowing Details〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 极致细节 → Extreme Details〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 疯狂细节 → Insane Details〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 令人惊叹的 → breathtaking〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 令人敬畏的 → awe-inspiring〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 混乱的 → chaotic〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 迷人的 → charming〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 引人注目的 → compelling〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 复杂的 → complex〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 显眼的 → conspicuous〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 炫目的 → dazzling〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 令人愉悦的 → delightful〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 细节丰富的 → detailed〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 坚决的 → determined〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 庄重的 → dignified〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 梦幻般的 → dreamy〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 光辉的 → effulgent〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 精细的 → elaborate〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 高尚的 → elevated〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 令人愉快的 → enjoyable〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 诱人的 → enticing〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 优雅的 → ethereal〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 崇高的 → exalted〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 精致的 → exquisite〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 幻想的 → fanciful〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 有趣的 → fun〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 华而不实的 → gaudy〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 闪烁的 → glimmering〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 闪亮的 → glistening〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 闪闪发光的 → glittering〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 宏伟的 → grandiose〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 富有想象力的 → imaginative〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 帝国式的 → imperial〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 令人印象深刻的 → impressive〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 白炽的 → incandescent〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 复杂精细的 → intricate〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 引人入胜的 → intriguing〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 招摇的 → kitschy〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 有光泽的 → lustrous〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 神奇的 → magical〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 壮丽的 → magnificent〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 雄伟的 → majestic〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 令人着迷的 → mesmerizing〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 神秘的 → mystical〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 高贵的 → noble〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 奢华的 → opulent〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 装饰性的 → ornamental〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 华丽的 → ornate〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 炫耀的 → ostentatious〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 超凡的 → otherworldly〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 强大的 → powerful〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 辐射的 → radiant〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 帝王般的 → regal〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 坚定的 → resolute〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 辉煌的 → resplendent〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 闪耀 → scintillating〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 有魅力的，诱人的 → seductive〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 闪烁的，闪耀的 → shimmering〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 炫耀的，张扬的 → showy〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 老练的，有教养的，复杂精密的 → sophisticated〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 闪耀的，活泼的 → sparkling〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 壮观的，引人入胜的 → spectacular〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 迷人的，令人入迷的 → spellbinding〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 庄严的，高贵的 → stately〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 坚定的，不动摇的 → steadfast〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 引人注目的，惊人的 → striking〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 极美的，惊人的 → stunning〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 崇高的，超凡的，壮丽的 → sublime〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 豪华的，奢侈的 → sumptuous〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 旋转的，缭绕的 → swirling〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 坚韧的，顽强的 → tenacious〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 卓越的，超越凡俗的 → transcendent〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 动荡的，骚乱的 → tumultuous〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 动荡的，狂暴的 → turbulent〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 闪烁的，眨眼间的 → twinkling〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 坚定不移的，毫不动摇的 → unwavering〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 坚定的，不屈不挠的 → unyielding〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 异想天开的，古怪的 → whimsical〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 非凡的 → Extraordinary〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 不寻常的 → Phenomenal〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 不可能的 → Improbable〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 难以解释的 → Inexplicable〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 难以理解的 → Unfathomable〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 令人困惑的 → Puzzling〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 魔幻的 → Magical〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 不可思议的 → Marvelous〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 令人震惊的 → Astounding〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 奇迹般的 → Miraculous〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 史诗般的 → Epic〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 传奇的 → Legendary〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 神话般的 → Mythical〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 英雄般的 → Heroic〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 宇宙的 → Cosmic〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 银河的 → Galactic〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 平整的 → Flat〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 精密的 → Precise〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 线条流畅的 → Sleek〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 流线型的 → Streamlined〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 柔和的 → Soft〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 弯曲的 → Curved〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 线条优美的 → Graceful〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 多样化的 → Varied〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 有机的 → Organic〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 光洁的 → Polished〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 细微的 → Subtle〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 纤细的 → Slender〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 线条细致的 → Intricate〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 曲线细腻的 → Delicately Curved〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 线条弯曲但流畅的 → Sinuous〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 线条优美且精细的 → Exquisite〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 有纹理的 → Textured〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 有层次感的 → Layered〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 纹路自然的 → Organic Pattern〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 具有浮雕感的 → Embossed〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 具有雕刻感的 → Carved〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 超细节 → Epic Detail〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 光滑的 → Smooth〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 清晰的 → Clear〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 细腻的 → Delicate〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 线条优美且流畅的 → Elegant〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 线条柔和且平滑的 → Soothing〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 曲线优美的 → Curvaceous〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 粗糙的 → Rough〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 不规则的 → Irregular〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 锋利的 → Sharp〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 粗大的 → Bulky〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 多棱角的 → Angular〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 充满动感的 → Dynamic〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 统一的 → Uniform〔可用〕　— 旧库保留；按目标模型与具体场景选择。

### 材质（19）

- 铜质 → Bronze〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 棉花 → Cotton〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 软糖 → Gummies〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 金色 → Gold〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 金属质地 → Metallic〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 镣 → Nickel〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 包裹 → Wrap〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 象牙 → lvory〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 石质 → Stone texture〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 亚光质感 → Matte texture〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 珍珠质感 → Pearl texture〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 纹理质感 → Texture〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 沙质 → Sandy texture〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 陶瓷质感 → Ceramic texture〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 古铜质感 → Antique bronze texture〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 砖石质感 → Brick texture〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 纱绸质感 → Gauze texture〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 粘土质感 → Clay texture〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 木头 → Wood〔可用〕　— 旧库保留；按目标模型与具体场景选择。

### 色调、渲染（51）

- 高对比 → high contrast〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 金银色调 → Gold and silver tones〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 黑色背景为中心 → Black background centered〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 低纯度色调 → Low purity tone〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 高纯度色调 → High purity tone〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 对比度 → contrast ratio〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 雪山蓝色系 → Snow Mountain Blue Series〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 镭射糖果纸色 → Laser candy paper color〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 马卡龙色 → Macaron〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 钛金属色系 → Titanium metal color system〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 黑白灰色系 → Black and white gray system〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 极简黑白色系 → Minimalist black and white color scheme〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 温暖棕色系 → Warm Brown Series〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 时尚灰色系 → Fashion Grey〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 亮丽橙色系 → Bright Orange Series〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 自然绿色系 → Natural Green Series〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 象牙白色系 → Ivory white series〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 奢华金色系 → Luxury Gold Tones〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 巨无霸色系 → Big Mac color scheme〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 紫罗兰色系 → Violet color scheme〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 柠檬黄色系 → Lemon yellow〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 爱马仕橙 → Hermes Orange〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 蒂芙尼蓝 → tiffany blue〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 提香红 → Tixiang Red〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 马耳他蓝 → Malta Blue〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 马尔斯绿 → Mars Green〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 鲜艳 → Rich color〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 霓虹氛围 → Neon shades〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 粉白色调 → White and pink tone〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 戏剧性对比度 → Dramatic contrast〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 黑色背景居中 → Black background centered〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 白色和绿色调 → White and green tones〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 红色和黑色调 → Red and black tones〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 黄色和黑色调 → Yellow and black tones〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 金色和银色调 → Gold and silver tones〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 稳重蓝色系 → Steady Blue〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 丹宁蓝色系 → Denim Blue〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 经典红黑白色系 → Classic Red Black and White〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 珊瑚橙色系 → Coral Orange〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 紫罗兰紫色系 → Violet Purple〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 水晶藍色系 → Crystal Blue〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 珊瑚色系 → Coral〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 绿野仙踪色系 → Emerald〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 玫瑰金色系 → Rose Gold〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 浅藍色系 → Sky Blue〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 酒紅色系 → Burgundy〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 土耳其藍色系 → Turquoise〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 薄荷绿色系 → Mint Green〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 枫叶红色系 → Maple Red〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 圣光 → Holy Light〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 反射透明彩虹色 → Reflections Transparent Iridescent Colors〔可用〕　— 旧库保留；按目标模型与具体场景选择。

## 旧库补充-镜头构图

> 原有分类

### 镜头（47）

- 男性焦点(女性焦点) → male focus〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 动态角度 → dynamic angle〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 从上面拍 → from above〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 从下面拍 → from below〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 全身拍摄 → full-body shot〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 相机平行 → camera level/Parallel angles〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 背光 → backlighting〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 光线反射 → reflection light〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 光圈 → Aperture〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 曝光 → Exposure〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 广角照片 → Wide-angle shot〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 长焦照片 → Telephoto shot〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 高键照片 → High-key shot〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 低键照片 → Low-key shot〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 高动态范围照片 → HDR〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 超侧角 → super side angle〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 超广角镜头 → ultra wide shot〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 电影镜头 → cinematic shot〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 景深(dof) → depth of field (dof)〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 相机型号 焦段 光圈 → Canon 5D, Fujifilm XT100, Sony Alpha〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 中特写 → Medium Close-Up(MCU)〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 远景 → Long Shot(LS)〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 过肩景 → over the shoulder shot〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 两景(2S) → two shot(2S)〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 三景(3S) → three shot(3S)〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 群景(GS) → group shot(GS)〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 风景照 → scenery shot〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 背景 → background〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 细节镜头(ECU) → Detail Shot(ECU)〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 面部拍摄(VCU) → Face Shot (VCU)〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 俯视视角 → Top-down perspective〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 侧面视角 → Side-scrolling perspective〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 短距离视角 → Close-up view〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 远距离视角 → Long-shot view〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 鱼眼视角 → Fisheye lens〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 微距视角 → Macro lens〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 大特写 → Detail Shot (ECU)〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 全景视角 → Panoramic View〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 逆光摄影风格 → Backlight Style〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 低角度视角 → Low Angle Shot〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 俯拍视角 → Overhead〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 常规视角 → Eye-level〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 鸟瞰视角 → Bird's-Eye〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 运动视角 → Dynamic〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 透视视角 → Perspective〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 极限近景 → Extreme Close-Up〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 模拟摄影机 → Simulated Camera〔可用〕　— 旧库保留；按目标模型与具体场景选择。

### 镜头解析（14）

- 广角镜头，通常指焦距小于35mm的镜头，可捕捉更广阔的场景 → Wide-angle lens〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 标准镜头，通常指焦距约为50mm的镜头，视角与人眼相近 → Standard lens〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 长焦镜头，通常指焦距大于70mm的镜头，可拍摄远距离的主体 → Telephoto lens〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 变焦镜头，可通过调整焦距拍摄不同视角的主体 → Zoom lens〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 微距镜头，可拍摄极其细小的主体，通常有1:1的放大倍率 → Macro lens〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 鱼眼镜头，可拍摄极其宽广的场景，视角通常为180度以上 → Fish-eye lens〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 移轴镜头，可调整透视和景深，常用于建筑和风景摄影 → Tilt-shift lens〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 快速镜头，指最大光圈较大（如f/1.4或f/1.8）的镜头 → Fast lens〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 中画幅相机，可拍摄更高分辨率和更细腻的细节 → Medium format〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 全画幅相机，指传感器大小等同于35mm胶片的相机 → Full frame camera〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- APS-C画幅相机，指传感器大小小于全画幅相机的相机 → Crop sensor camera〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 莱卡相机，指使用徕卡镜头的相机，以高质量和精度著称 → Leica camera〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 好景深，指焦外模糊的效果，常用于强调主体并创造氛围 → Bokeh〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 暗角，指图像四周较暗的效果，常用于增加画面深度和视觉吸引力 → Vignetting〔可用〕　— 旧库保留；按目标模型与具体场景选择。

### 构图（34）

- 仰拍构图 → Upside-down composition〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 俯拍构图 → Perspective composition〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 等距 → isometric〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 等距视图 → isometric view〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 特写视图 → closeup view〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 高角度视图 → high angle view〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 乌瞰图 → A bird's-eye view,aerial view〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 顶视图 → Top view〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 倾斜移位 → tilt-shift〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 前视图、侧视图、后视图 → front, side, rear view〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 极端特写视图 → extreme closeup view〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 对称 → Symmetry〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 不对称 → Asymmetry〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 构框 → Framing〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 孤立 → Isolation〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 深度 → Depth〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 对比 → Contrast〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 纹理 → Texture〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- S形构图 → S-shaped composition〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 对称身体 → Symmetrical body〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 对称面孔 → Symmetrical face〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 三分法构图 → Rule of Thirds composition〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 黄金分割构图 → Golden Ratio composition〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 画框构图 → Framing composition〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 动态对称构图 → Dynamic symmetry composition〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 汇聚线条构图 → Converging lines composition〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 饱和构图 → Saturated composition〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 非线性构图 → Nonlinear composition〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 视角构图 → Point of view composition〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 孤立构图 → Isolation composition〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 负空问构图 → Negative space composition〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 鸟瞰 → Bird's-eye view〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 极端特写 → Extreme close-up〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 留白 → negative space〔可用〕　— 旧库保留；按目标模型与具体场景选择。

## 旧库补充-风格

> 原有分类

### 艺术风格（121）

- 全息色彩风格 → Holographic color style〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 立体等距风格 → Stereoscopic isometric style〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 3D风格 → 3D style〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 辛烷渲染风格 → Octane render style〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 复合式风格 → A made out of "B"〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 极简主义风格 → minimalist style〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- sheet风格 → sheet style〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- Ul扁平风格 → Ul flat style〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 平铺罗列风格 → Knolling〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 复杂设计风格 → complex design style〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 哥特式 → gothic〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 日本浮世绘风格 → Ukiyoe〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 中国国画 → Traditional Chinese painting〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 黑暗风格 → film noir〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 文艺复兴风格 → Renaissance Art〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 写实主义 → hyperrealism〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 巴洛克式 → Baroque〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 古埃及 → ancient Egypt〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 学院主义 → Academicism〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 愁苦主义 → Miserablism〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 古希腊艺术 → Ancient Greek art〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 迪士尼风格 → Disney style〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 皮克斯风格 → Pixar style〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 插画风格 → illustration〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 黑暗幻想风格 → dark fantasy style〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 后印象派 → Neo-impressionism〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 当代艺术 → contemporary art〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 动画风格 → anime style〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 视觉艺术 → visionary art〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 漫画书 → comic book〔可用〕　— 旧库保留；按目标模型与具体场景选择。 旧译别名：Comicbook
- 黑暗主题 → dark theme〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 能生成美漫封面的漫画画面 → DC Comics〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 纯二次元风格人像 → 2D style portrait/pixiv〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 威廉森风格 → style of Al Williamson〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 包豪斯风格 → Bauhaus Style〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 安迪沃霍尔风格 → Warhol〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 当代写实主义 → Contemporary Realism〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 纪实的 → Non-Fiction〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 同步性 → Synchronism〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- ww3风格 → WW3 style〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 适合科幻场景 → Suitable for Sci-Fi〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 科幻的 → Sci-Fi〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 科幻 → Science Fiction〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 科幻风格 → Sci-Fi style〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 黑暗奇幻 → Dark Fantasy〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 飘渺奇幻 → Ethereal Fantasy〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 绗缝艺术 → quilted art〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 立体派 → Cubism〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 欧普艺术/光效应艺术 → OP Art /Optical Art〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 维多利亚时代 → Victorian〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 粗犷主义 → brutalist〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 旷野之息 → botw〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 法国艺术 → french art〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 民族艺术 → Ethnic Art〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 新艺术风格 → Art Nouveau〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 超现实的 → Surreal〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 复古黑暗复古 → retro dark vintage〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 浮世绘艺术 → Ukiyo-e art〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 纹身艺术 → Tattoo art〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 滴漆艺术 → Dripping art〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 官方艺术 → official art〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 游戏CG → game cg〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 高对比度 → high contrast〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 速涂风格 → pastel color sketch〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 80年代风格 → 80s (style)〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 90年代风格 → 90s (style)〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 新艺术(不支持含背景) → art nouveau〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 手绘风格 → hand drawn style〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 街拍 → street photography〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 电影摄影风格 → flm photography〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 日本海报风格 → poster of japanese graphic design〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 分析性绘图 → Analytic drawing〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 着色书 → Coloring book〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 电影风格 → Film style〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 哥特式黑暗 → Gothic gloomy〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 统一创作 → Unity Creations〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 时尚 → Fashion〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 巴洛克时期 → Baroque〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 观赏性 → Ornamental〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- riso 印刷风格 → Risograph〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 现实的 → Realistic〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 静脉 → Veins〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 缝合 → Stitching〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 斯格格勒斯 → Squiggles〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 对称性 → Symmetric〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 技术性 → Technological〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 创世纪 → Tron〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 褶皱的 → Wrinkled〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 火山型 → Volcanic〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 湿漆 → Wet Paint〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 迷你仿制 → Miniature Faking〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 狂野西部 → Wild West〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 包浩斯 → Bauhaus〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 古典风，18-19世纪 → Vintage〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 黑白电影时期 → Pulp Noir〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 乡村风格 → Country style〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 抽象风 → I Abstract〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- riso印刷风 → risograph〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 设计风 → Graphic〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 线粒体 → Mitochondria〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 梅卡巴 → Merkaba〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 多维度 → Multidimensional〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 神秘幻想 → Mystic Fantasy〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 珍珠奶茶风格 → Pearl Milk Tea Style〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 水墨风格 → Ink Wash Painting Style〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 纸本彩色墨水 → Color Ink on Paper〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 传统文化 → Traditional Culture〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 日本动画片 → Anime〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 日本风格 → Japanese Style〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 魔幻现实 → Magic Realism〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 迪士尼风 → Disney-style〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 洛丽塔风格 → Lolita Style〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 像素风 → Pixel Art〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 伏尼契手稿 → Voynich Manuscript〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 微缩模型电影风格 → Miniature Movie Style〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 剪辑 → Film Photography〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 魔幻现实主义风格 → Magic Realism Style〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 游戏风格 → Game Style〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 真实的 → Realistic〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 真实感 → Photorealism〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 电影般的 → Cinematic〔可用〕　— 旧库保留；按目标模型与具体场景选择。

### 动漫/动画/游戏风格（25）

- 星际战甲 → Warframe〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 宝可梦 → Pokémon〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- Apex英雄 → APEX〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 上古卷轴 → The Elder Scrolls〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 魂系游戏 → From Software〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 底特律:变人 → Detroit: Become Human〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 剑与远征 → AFK Arena〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 跑跑姜饼人 → Cookie Run: Kingdom〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 英雄联盟 → League of legends〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- JOJO的奇妙冒险 → jojo's bizarre adventure〔可用〕　— 旧库保留；按目标模型与具体场景选择。 旧译别名：Jojo's Bizarre Adventure
- 宫崎骏风格 → Miyazaki Hayao style〔可用〕　— 旧库保留；按目标模型与具体场景选择。 旧译别名：Miyazaki Hayao Style
- 副岛成记 → Soejima Shigenori〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 山田章博 → Yamada Akihiro〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 六七质 → Munashichi〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 梦工厂动画风格 → DreamWorks Animation style〔可用〕　— 旧库保留；按目标模型与具体场景选择。 旧译别名：Dreamworks Pictures
- 梦工厂影业 → DreamWorks Pictures〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 漫画 → manga〔可用〕　— 旧库保留；按目标模型与具体场景选择。 旧译别名：comic; Manga
- 吉卜力风格 → Ghibli Studio〔可用〕　— 旧库保留；按目标模型与具体场景选择。 旧译别名：Ghibli Studio Style
- 90年代电视游戏 → 90s video game〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 日本漫画风格 → Japanese comics/manga〔可用〕　— 旧库保留；按目标模型与具体场景选择。 旧译别名：Japanese manga style
- 童话故事书插图风格 → stock illustration style〔可用〕　— 旧库保留；按目标模型与具体场景选择。 旧译别名：Stock Illustration Style
- 赛璐璐着色 → cel shading〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 3D 动漫 → 3D anime〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 动漫渲染 → anime-style rendering〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 3D 动画电影风格 → 3D animated feature film style〔可用〕　— 旧库保留；按目标模型与具体场景选择。

### 其他风格（40）

- 可爱的 → cute〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 闪闪发亮 → shiny〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 漩曲的 → swirling〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 法喜充满 → peaceful〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 纠缠的 → entanglement〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 交织的 → intertwined〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 让人喜爱的 → adorable〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 轮廓分明，刀切斧凿 → chiseled〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 巨大的 → Gigantic〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 骨制 → made of bones〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 塑胶包装 → plastic shrink wrap〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 半机械的 → semi-mechanized〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 花俏的 → fancy〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 骷髅状的各种东西 → skull shape〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 雾气的 → foggy〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 被烟雾包围 → surrounded by smoke〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 湿润的 → moist〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 米其林星级 → Michelin star〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 不光滑的/雾面 → matte〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 飘渺的 → scary〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 白色配色 → White color scheme〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 小巧的 → dinky〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 对称的 → symmetrical,〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 错综复杂的 → intricate〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 以花丝作为细节 → filigree detailing〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 光速 → Lightspeed〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 液体 → Liquid〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 电气的 → Electrical〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 未来的 → Futuristic〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 点状 → Dots〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 滴落的油漆 → Dripping Paint〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 沙丘 → Dune〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 原核生物 → Prokaryotic〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 前历史性的 → Pre Historic〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 花卉类的 → Floral〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 水粉画 → Gouache〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 乳胶 → Latex〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 写实的 → Photorealistic〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 针织的 → Knitted〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 波尔卡 → Polka〔可用〕　— 旧库保留；按目标模型与具体场景选择。

### 炫图风格（24）

- 平铺效果 → Knolling〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 集合效果 → a collection of〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 3D平面图 → floorplan〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 雕刻效果 → carving/relief/sculpture〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 拟人效果 → anthropomorphic〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 马赛克拼贴 → Benin art/mosaic style〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 卷纸艺术效果 → quilling paper art〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 电影光效 → cinematic lighting〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 模糊的 → blurry〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 神圣感顶光 → god rays〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 反射光 → reflection light〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 混合 → blending〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 盛开 → bloom〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 色差滥用 → chromatic aberration abuse〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 投影阴影 → drop shadow〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 胶片颗粒感/老电影滤镜 → film grain〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 图像填充 → image fill〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 多重单色 → multiple monochrome〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 互补色 → anaglyph〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 科幻全系图效果 → hologram〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- X光透视效果 → x-ray〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 生物发光效果 → bioluminrscent〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 镀铬效果 → made of chrome〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- ASCII码效果 → ascii art〔可用〕　— 旧库保留；按目标模型与具体场景选择。

### 艺术家（15）

- 莫奈 → Monet〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 保罗-塞尚 → Paul Cezanne〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 马克-罗斯科 → Mark Rothko〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 毕加索 → Picasso〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 皮特-蒙德里安 → Piet Mondrian〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 皮埃尔-奥古斯特-雷诺阿 → Pierre Auguste Renoir〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 马特-科利肖 → Mat Collishaw〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 伊戈尔-莫尔斯基 → Igor Morski〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 京都动漫 → Kyoto Anime〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 杰里-平克尼 → Jerry Pinkney〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 雷内-马格里特 → Rene Magritte〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 萨尔瓦多-达利 → Salvador Dali〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 罗伊-利希滕斯坦 → Roy Lichtenstein〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 瓦西里-康定斯基 → Wassily Kandinsky〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 克劳德莫奈 → Claude Monet〔可用〕　— 旧库保留；按目标模型与具体场景选择。

### 线条（29）

- 交叉线描 → Cross-hatching〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 涂鸦画 → Scribble drawing〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 素描画 → Outline drawing〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 富表现力的线描 → Expressive line drawing〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 建设性的线描 → Constructive line drawing〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 结构性线描 → Structural line drawing〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 波浪线描 → Wavy line drawing〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 草书线描 → Cursive line drawing〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 印象主义的线描 → Impressionistic line drawing〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 现实主义线描 → Realistic line drawing〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 色调线描 → Tonal line drawing〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 线刻 → Hatching〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 交叉线刻 → Crosshatching〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 点刻 → Stippling〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 不看纸画 → Blind contour drawing〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 日本水墨画 → Sumi-e〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 涂色书 → Coloring book〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 干笔画 → Dry brush〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 禅宗画法 → Zen Painting〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 雕塑线条 → Sculpture Line〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 细节线条 → Detail Line〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 手工制作画 → Handmade Painting〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 立体主义线条 → Cubist Line〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 抽象线条 → Abstract Line〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 现代主义线条 → Modernist Line〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 野兽派线条 → Fauvist Line〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 表现主义线条 → Expressionist Line〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 印象派线条 → Impressionist Line〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 点线结合 → Point and Line Combination〔可用〕　— 旧库保留；按目标模型与具体场景选择。

### 国潮插画风格（14）

- 标记绘图 → Marker drawing〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 纸本彩墨 → color ink on paper〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 彩色铅笔绘图 → colored pencil drawing〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 涂鸦艺术 → Doodle Art〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 平线图 → flat line drawing〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 工笔画 → gongbi painting〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 图解说明 → Graphic illustration〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 剪纸工艺 → Paper cut craft〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 衍纸 → Paper quilling〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 矢量图 → vector illustration〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 昆剧 → Kunqu opera〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 川剧 → Sichuan opera〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 中国奇侠 → Chinese Paladin〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 中国武侠 → Chinese wuxia〔可用〕　— 旧库保留；按目标模型与具体场景选择。

### 形式（56）

- 摄影 → photography〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 印刷版画 → Blockprint〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 石墨 → Graphite〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 彩色玻璃 → Stained glass〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 刮画板 → Scratchboard〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 水彩画 → water colour painting〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 透明水彩绘 → watercolor (medium)〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 水彩铅笔 → watercolor pencil〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 墨水涂鸦 → ink doodle〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 炭笔素描 → charcoal sketch〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 素描艺术 → sketch art〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 素描纸 → sketch paper〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 草图 → posing sketch〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 传统媒体风格(蜡笔) → faux traditional media〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 传统媒体 → traditional media〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 平色 → flat color〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 褪色的边界 → fading border〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 浓重的对比(强调颜色) → heavy contrast〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 唯美主义绘画 → Aestheticism Painting〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 现实主义绘画 → realism〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 逼真,仿真 → photorealistic〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 现实的阴影 → realistic shadows〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 照片真实感 → Photorealistic〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 海报/主题聚焦 → poster, caustics〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 动画截图 → anime screenshot〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 封面 → cover〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 专辑 → album〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 信息图画 → Infographic drawing〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 图解式画像 → Diagrammatic portrait〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 虹彩 → Iridescent〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 日本墨水 → Japanese ink〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 单线图 → One-line drawing〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 墨水渲染 → ink render〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 粉笔画 → Pastel drawing〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 水彩儿童插画 → Watercolor children's illustration〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 拼布拼贴画 → Patchwork collage〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 图示性绘图 → Diagrammatic drawing〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 二维插图 → 2D illustration〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 16比特 → 16-Bit〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 8比特 → 8-Bit〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 1800s → 1800s〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 1980s → 1980s〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 纤维素 → Cellulose〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 阿拉伯 → Arabic〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 块状的 → Blocky〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 天人般 → Celestial〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 加勒比 → Caribbean〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 炭色风格 → Charcoal Style〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 衍射分级 → Diffraction Grading〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 堕落的 → Diabolic〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 色度 → Chromatic〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 珊瑚 → Coral〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 水墨插图 → ink illustration〔可用〕　— 旧库保留；按目标模型与具体场景选择。 旧译别名：Ink Illustration
- 东方山水画 → Traditional Chinese Ink Painting〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 素描画法 → Sketch Drawing〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 产品摄影 → product photography〔可用〕　— 旧库保留；按目标模型与具体场景选择。

### 中式元素（6）

- 中式服饰 → Chinese costume〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 功夫 → Kungfu〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 牡丹 → Peony〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 中式亭 → Chinese pavilion〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 梅花 → Plum flower〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 题字 → calligraphic inscription〔可用〕　— 旧库保留；按目标模型与具体场景选择。

## 旧库补充-饰品

> 原有分类

### 头饰（49）

- 花冠 → head wreath〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 头上的花 → hair flower〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 发卡 → hairband〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 发花 → hair flower〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 花边 → ribbon〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 绷带 → bandage〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 蝴蝶结 → bowtie〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 头发上系着铃铛 → hair bell〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 头箍 → hairband〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 三重冕 → tiara〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 头饰 → hair ornament〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 铃铛 → bell〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 三叶草发饰 → clover hair ornament〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 恶魔的脚 → demon horns〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 鱼形发饰 → fish hair ornament〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 额前有宝石 → forehead jewel〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 额前有图案 → forehead mark〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 无线蓝牙耳机 → hairpods〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 头发上的铃铛 → hair bell〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 从后脑戴着的耳机 → behind-the-head headphones〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 护肘 → elbow pads〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- X发饰 → x hair ornament〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 黑色发带 → black hairband〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 白色发带 → white hairband〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 发呆 → hair tie〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 青蛙发饰 → frog hair ornament〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 食物发饰 → food-themed hair ornament〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 红色发带 → red hairband〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 蛇发饰 → snake hair ornament〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 洛丽塔发带 → lolita hairband〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 蓝色发带 → blue hairband〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 锚发饰 → anchor hair ornament〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 叶发饰 → leaf hair ornament〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 兔子发饰 → bunny hair ornament〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 骷髅头饰 → skull hair ornament〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 黄色发带 → yellow hairband〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 粉色发带 → pink hairband〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 蝴蝶结发带 → bow hairband〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 猫头饰 → cat hair ornament〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 音符发饰 → musical note hair ornament〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 胡萝卜发饰 → carrot hair ornament〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 紫色发带 → purple hairband〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 多个蝴蝶结 → multiple hair bows〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 蝙蝠发饰 → bat hair ornament〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 骨发饰 → bone hair ornament〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 橙色发带 → orange hairband〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 雪花发饰 → snowflake hair ornament〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 头上有花 → flower on head〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 头上带着花冠 → head wreath〔可用〕　— 旧库保留；按目标模型与具体场景选择。

### 帽子（5）

- 兜帽 → hood〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 东金帽子 → tokin hat〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 放下的兜帽 → hood down〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 带起来的兜帽 → hood up〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 类似警帽的帽子 → peaked cap〔可用〕　— 旧库保留；按目标模型与具体场景选择。

### 面部（2）

- 面具 → mask〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 掀到头上的面具 → mask on head〔可用〕　— 旧库保留；按目标模型与具体场景选择。

### 项链（3）

- 颈部饰品 → choker〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 珠子项链 → bead necklace〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 脖子上挂着口哨 → whistle around neck〔可用〕　— 旧库保留；按目标模型与具体场景选择。

### 手饰（5）

- 珠子手链 → bracelet〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 长袖手套 → elbow gloves〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 手枷 → cuffs〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 警用手铐 → handcuffs〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 缠着绷带的手臂 → bandaged arm〔可用〕　— 旧库保留；按目标模型与具体场景选择。

### 眼部（12）

- 风镜 → goggles〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 眼罩(独眼) → eyepatch〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 面具/眼罩/口罩 → mask〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 下半无框眼镜 → over-rim eyewear〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 单眼罩 → eyepatch〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 卡米纳墨镜 → kamina shades〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 帽子上别着护目镜 → goggles on headwear〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 一只眼缠着绷带 → bandage over one eye〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 眼镜的疤痕 → scar across eye〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 蒙住的眼 → covered eyes〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 眼镜别在头上 → eyewear on head〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 厚如玻璃瓶底的圆眼镜 → coke-bottle glasses〔可用〕　— 旧库保留；按目标模型与具体场景选择。

### 耳饰（1）

- 耳机 → headphones〔可用〕　— 旧库保留；按目标模型与具体场景选择。

### 配饰（2）

- 束腰 → girdling〔可用〕　— 旧库保留；按目标模型与具体场景选择。
- 蓬莱玉枝 → jeweled branch of hourai〔可用〕　— 旧库保留；按目标模型与具体场景选择。
