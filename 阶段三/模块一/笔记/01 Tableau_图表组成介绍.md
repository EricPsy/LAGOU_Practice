## 1 Tableau工作表基本界面

<img src="https://blog20200906.oss-cn-hangzhou.aliyuncs.com/uPic/image-20200909231659797.png" alt="image-20200909231659797" style="zoom:50%;" />

基础概念：维度、度量、聚合、粒度。

1. 维度: 维度包含定量值(例如名称、日期或地理数据)，可以使用维度进行分类、分段以及揭示数据中的详细信息。维度影响视图中的详细级别。
2. 度量：度量包含可以测量的数字定量值。度量可以聚合。将度量拖到视图中时，Tableau(默认情况下) 会向该度量应用一个聚合。
3. 聚合：和其他软件中概念类似，指sum、average、max、min等聚合计算
4. 粒度：数据的不同聚合粒度。如果决定要以最详细的粒度级别查看数据，需要解聚。例如下图中的年订单日期这里，可以看到前面有一个加号。点击加号后，后面会出现季度；如果点击季度，后面会出来月...图表也还会根据不同的粒度（年、季度、月）进行变化。

对于维度和度量中的字段（如产品名称、利润等），我们将其拖拽到右侧的列、行，就能形成图表。而对维度和度量中字段的处理和操作，可以通过选择相应的字段，然后右键选择相应的操作。

基本的字段处理有：

> * 数据类型转换:文本转数字，数字转文本 
> * 度量、维度互转
> * 字段排序:按照源排序，不要按字母排序 
> * 分文件夹管理字段:如果字段过多，可以按类建文件夹 
> * 数据格式设置:百分比设置; 
> * 复制字段:一个字段用做原始值，复制的字段用做衍生 
> * 日期类型转化和几种日期类型

高级的字段操作有：

> * 字段拆分
> *  分组
> * 创建集
> *  创建数据桶:是直方图的基础数据 （即将数据按照一定间隔进行分组） 
> * 创建新字段
>
> \#创建参数

## 2 Tableau 工作表各个区域详细介绍

### 2.1 行和列 

**添加行和列:**

* 任意拖拽~ 也可以直接拖拽到画布 
* 双击指标实现
* 取消:拖出

维度字段的排序、度量指标的聚合方式、不同行和列隐藏均可通过右键点击相应的视图中行、列里相应的字段实现。

### 2.2 视图

![image-20200909233538176](https://blog20200906.oss-cn-hangzhou.aliyuncs.com/uPic/image-20200909233538176.png)



> **A.** **字段标签**- 添加到行或列功能区的离散字段的标签，用于说明该字段的成员。例如，“类别”是一个离 散字段，它包含以下三个成员:“家具”、“办公用品”和“技术”。
>
> **B.** **标题**- 工作表、仪表板或故事提供的名称，系统会为工作表和故事自动显示标题。
>
>  **C.** **区 /单元格** - 表示视图中所包括的字段(维度和度量)交集的数据。可以用线、条、形状、地图、文本等来表示标记。
>
> **D.** **图例**- 描述视图中的数据编码方式的图例。例如，如果您在视图中使用形状或颜色，则图例会描述每 个形状或颜色所代表的项。
>
> **E.** **坐标轴**- 是在将度量(包含定量数值信息的字段)添加到视图时创建的。默认情况下，Tableau 会针 对此数据生成连续的轴。
>
> **F.** **横坐标字段名或标**签- 字段的成员名称。
>
> **G.** **说明**- 描述视图中的数据的文本。说明可以自动生成，并且可以打开和关闭。

Tableau还有一些非常简便的交互操作，可以通过选中想应的数据，然后右键选择相应的功能来实现。

> * 突出
> * 圈选
> * 排除
> * 隐藏/显示
> * 查看数据和详细数据（可以将相应的数据导出）
> * 复制粘贴数据

### 2.3 标记卡

标记卡主要用来使图表的可读性更强，我们可以通过更改图表类型、颜色、大小、形状来改变展示形式，也可以通过标签、详细信息、工具提示等选项来增加对不同数据点的信息的提取。  

操作方式：直接拖动目标段到目标位置：

<img src="https://blog20200906.oss-cn-hangzhou.aliyuncs.com/uPic/image-20200909095804948.png" alt="image-20200909095804948" style="zoom:50%;" />

接下里对各个选项进行展示： 

#### 2.3.1 颜色

<img src="https://blog20200906.oss-cn-hangzhou.aliyuncs.com/uPic/image-20200909095900645.png" alt="image-20200909095900645" style="zoom:50%;" />

#### 2.3.2 大小

<img src="https://blog20200906.oss-cn-hangzhou.aliyuncs.com/uPic/image-20200909100336089.png" alt="image-20200909100336089" style="zoom:50%;" />

#### 2.3.3 形状

<img src="https://blog20200906.oss-cn-hangzhou.aliyuncs.com/uPic/image-20200909103314078.png" alt="image-20200909103314078" style="zoom:50%;" />

#### 2.3.4 标签

<img src="https://blog20200906.oss-cn-hangzhou.aliyuncs.com/uPic/image-20200909100447202.png" alt="image-20200909100447202" style="zoom:50%;" />

#### 2.3.5 详细信息 

将鼠标悬停在某个数据点时，会在信息卡片中显示结果所选择的详细信息

<img src="https://blog20200906.oss-cn-hangzhou.aliyuncs.com/uPic/image-20200909102219596.png" alt="image-20200909102219596" style="zoom:50%;" />

#### 2.3.6 工具提示

配置刚才信息提示表的一些选项。

<img src="https://blog20200906.oss-cn-hangzhou.aliyuncs.com/uPic/image-20200909102337753.png" alt="image-20200909102337753" style="zoom:50%;" />



### 2.4 筛选器

在介绍工作表的筛选区域之前，先来看下Tableau中的筛选功能分别位于哪些位置：

> Tableau的筛选功能主要有两种：针对源数据的筛选，在工作表中的筛选。
>
> 源数据的筛选包括：
>
> > 1. 数据提取筛选器 （源数据筛选）
> > 2. 数据源筛选器 （源数据筛选）
>
> 工作区的筛选（作用于结果）：
>
> > 3. 筛选器功能区
> > 4. 视图内的筛选
> > 5. 行列功能区、标记卡字段胶囊筛选

可以看下这些筛选器分别在什么地方：

#### 2.4.1 对源数据筛选

1. 数据提取筛选器  

这里是对源数据的一种筛选，一般不建议在此处进行数据的筛选，除非数据量真的太大了。

<img src="https://blog20200906.oss-cn-hangzhou.aliyuncs.com/uPic/image-20200909104757618.png" alt="image-20200909104757618" style="zoom:50%;" />

2. 数据源筛选器  

也是对源数据的一种筛选，一般不建议进行数据的筛选，除非数据量真的太大了。

<img src="https://blog20200906.oss-cn-hangzhou.aliyuncs.com/uPic/image-20200909105537609.png" alt="image-20200909105537609" style="zoom:50%;" />

#### 2.4.2 功能区筛选

1. 筛选器功能区（工作表区） 

工作表中的筛选有点类似于SQL中的Having，只作用于展示的结果，并不会对源数据产生影响。 

<img src="https://blog20200906.oss-cn-hangzhou.aliyuncs.com/uPic/image-20200909112618050.png" alt="image-20200909112618050" style="zoom:50%;" />

2. 视图区进行筛选（主要是排除某些数据）

首选鼠标左键长按视图区，选中自己要的数据，然后右键选择排除。

<img src="https://blog20200906.oss-cn-hangzhou.aliyuncs.com/uPic/image-20200909112950253.png" alt="image-20200909112950253" style="zoom:50%;" />

<img src="https://blog20200906.oss-cn-hangzhou.aliyuncs.com/uPic/image-20200909113232475.png" alt="image-20200909113232475" style="zoom:50%;" />

3. 行列功能区、标记卡字段胶囊筛选 

Tableau会根据不同的字段展示不同的筛选器类型 （无论是维度还是度量，都可以像图中一样操作）

<img src="https://blog20200906.oss-cn-hangzhou.aliyuncs.com/uPic/image-20200909113601824.png" alt="image-20200909113601824" style="zoom:50%;" />



#### 2.4.3 筛选顺序

这几个地方的筛选，在Tableau中的过滤顺序不同。过滤顺序依次为: 

> 1. 数据提取筛选器
> 2. 数据源筛选器
> 3. 上下文筛选器 
> 4. 维度上的筛选器(无论是在“筛选器”功能区上还是在视图内的筛选器卡中) 
>
> 5. 度量上的筛选器(无论是在“筛选器”功能区上还是在视图内的筛选器卡中)

上下文筛选器：

我们在工作表视图处进行筛选时，右键维度可以将其设置为上下文。当执行筛选功能时，会优先执行被设置了上下文的维度，然后执行其他维度。设置过程如下图：

<img src="https://blog20200906.oss-cn-hangzhou.aliyuncs.com/uPic/image-20200909153228500.png" alt="image-20200909153228500" style="zoom:50%;" />

#### 2.4.4 联动筛选

小一级的筛选范围值根据大一级筛选范围值的变化而变化。

方法：

> 1. 通过分层结构
>
> 2. 仅相关值

**方法一：通过分层结构实现联动筛选**

首先创建分层结构：command选中两个维度（例如子类别和类别），然后右键-分层结构-创建分层结构-取名-点击确定。

<img src="https://blog20200906.oss-cn-hangzhou.aliyuncs.com/uPic/image-20200909143845286.png" alt="image-20200909143845286" style="zoom:50%;" />

将类别-子类别分别拖入筛选器（注意左侧的顺序，类别要在子类别上面，否则无法识别分层结构），子类别拖入时注意勾选全部选项。

<img src="https://blog20200906.oss-cn-hangzhou.aliyuncs.com/uPic/image-20200909144333482.png" alt="image-20200909144333482" style="zoom:50%;" />

选择筛选器中的类别和子类别，右键选择显示筛选器。

<img src="https://blog20200906.oss-cn-hangzhou.aliyuncs.com/uPic/image-20200909144648288.png" alt="image-20200909144648288" style="zoom:50%;" />

可以在右侧看到筛选器（如果类别的框在下方，可以拖到子类别上面来）：

<img src="https://blog20200906.oss-cn-hangzhou.aliyuncs.com/uPic/image-20200909144742509.png" alt="image-20200909144742509" style="zoom:50%;" />

完成联动筛选，我们点击类别中的办公用品时，子类别会显示该大类下的所有类目。

<img src="https://blog20200906.oss-cn-hangzhou.aliyuncs.com/uPic/image-20200909144947770.png" alt="image-20200909144947770" style="zoom:50%;" />

在右侧筛选器这里，点击下拉三角，下面红框中的选项是与联合筛选有关的：

<img src="https://blog20200906.oss-cn-hangzhou.aliyuncs.com/uPic/image-20200909145455368.png" alt="image-20200909145455368" style="zoom:50%;" />

其中“分层结构中的所有值”这一选择只有在我们建立了分层结构的情况下才会有。**在建立了分层结构的情况下，无论选择三个选项中的哪个选项，当我们选定一个大类别时，子类别都会自动出现该类别下的所有子类目，即实现了联动筛选。  **



**方法二：通过仅相关值实现联动筛选**

如果没有在左侧维度这里建立分层结构，那么这里的选择就只有两项：

> 仅相关值：选择该项还是会进行联动筛选，即当我们选定一个大类别时，子类别都会自动出现该类别下的所有子类目
>
> 数据库中的所有值：选择该项目后，联动筛选消失。无论选择哪个大类别，都会显示所有的子类目。



### 2.5 页面

<img src="https://blog20200906.oss-cn-hangzhou.aliyuncs.com/uPic/image-20200909160211989.png" alt="image-20200909160211989" style="zoom:50%;" />

页面常用来制造动态图表：

![页面](https://blog20200906.oss-cn-hangzhou.aliyuncs.com/uPic/%E9%A1%B5%E9%9D%A2.gif)



### 2.6 智能显示 

<img src="https://blog20200906.oss-cn-hangzhou.aliyuncs.com/uPic/image-20200909160621214.png" alt="image-20200909160621214" style="zoom:50%;" />

### 2.7 分析窗口

<img src="https://blog20200906.oss-cn-hangzhou.aliyuncs.com/uPic/image-20200909161241760.png" alt="image-20200909161241760" style="zoom:50%;" />

分析窗口可以做一些简单的统计分析。比较常用的如常量线、趋势线等。例如，常量线可以进行一些区域划分。

### 2.8 格式设置

1. **整体工作簿的设置**

主要设置整体的视觉样式，如整个工作表中的字体颜色、字体大小、趋势线样式等。

![image-20200909162628617](https://blog20200906.oss-cn-hangzhou.aliyuncs.com/uPic/image-20200909162628617.png)

要横总坐标轴的格式，直接点击-右键，然后选择格式就行。例如改变纵轴格式：

<img src="https://blog20200906.oss-cn-hangzhou.aliyuncs.com/uPic/image-20200909162943767.png" alt="image-20200909162943767" style="zoom:50%;" />

如果要改变边界、字体、对齐方式、阴影、线的格式，在图表空白区域点击右键，设置格式，然后在上方进行设置：

<img src="https://blog20200906.oss-cn-hangzhou.aliyuncs.com/uPic/image-20200909163701711.png" alt="image-20200909163701711" style="zoom:50%;" />

2. **将列名从竖排转为横排**

如下图可以看到子类别的文字都是竖向排列

![image-20200909164316096](https://blog20200906.oss-cn-hangzhou.aliyuncs.com/uPic/image-20200909164316096.png)

现在要将竖排文字转为横排（选中下方坐标轴，右键设置格式，在左侧表格中的对齐这里点击下来框）：

<img src="https://blog20200906.oss-cn-hangzhou.aliyuncs.com/uPic/image-20200909213318743.png" alt="image-20200909213318743" style="zoom:50%;" />

找到方向，选择正着的A，此时图标的子类别显示会改为横向的文字。

<img src="https://blog20200906.oss-cn-hangzhou.aliyuncs.com/uPic/image-20200909213556779.png" alt="image-20200909213556779" style="zoom:50%;" />

结果如图：

<img src="https://blog20200906.oss-cn-hangzhou.aliyuncs.com/uPic/image-20200909213948493.png" alt="image-20200909213948493" style="zoom:50%;" />



3. 将度量（Y轴标签利润、销售额）横向的字符转换为竖向。

<img src="https://blog20200906.oss-cn-hangzhou.aliyuncs.com/uPic/image-20200909214246335.png" alt="image-20200909214246335" style="zoom:50%;" />

操作步骤如下：

![image-20200909214818435](https://blog20200906.oss-cn-hangzhou.aliyuncs.com/uPic/image-20200909214818435.png)

结果（更改成功）：

<img src="https://blog20200906.oss-cn-hangzhou.aliyuncs.com/uPic/image-20200909214941544.png" alt="image-20200909214941544" style="zoom:50%;" />

