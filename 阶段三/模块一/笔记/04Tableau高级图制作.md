

数据源： 订单销售明细表

## 1 词云&热力图 

### 1 词云

1. 例如可以在网站[图悦](http://www.picdata.cn/picdata/)中（其他类似的网站：wordcloud等）将URL或者待分析的长文粘贴进去。例如将[Tableau百度百科](https://baike.baidu.com/item/tableau/9328520?fr=aladdin)的内容粘贴进去。然后点击分析出图，导出excel。

<img src="https://blog20200906.oss-cn-hangzhou.aliyuncs.com/uPic/image-20200918064237920.png" alt="image-20200918064237920" style="zoom:50%;" />

 

2. 打开excel，将关键词、词频两列直接复制，在tableau中进行粘贴。

3. 在Tableau数据源中对数据格式进行调整，如“字段名称对于第一行”等。
4. 拖到词频和关键词到标记卡，形成结果 

<img src="https://blog20200906.oss-cn-hangzhou.aliyuncs.com/uPic/image-20200918065241133.png" alt="image-20200918065241133" style="zoom:33%;" />



5. 美化图片，去掉哪些小的圆： 将词频拖入筛选器，选择“所有值”，选择下一步，选择至少大于2

<img src="https://blog20200906.oss-cn-hangzhou.aliyuncs.com/uPic/image-20200918065417837.png" alt="image-20200918065417837" style="zoom:33%;" />

wordcloud等网站可以在线制作词云，样式也很多。



### 2 热力图

在突出显示表的基础上增加一个维度就行。

突出显示表： 

<img src="https://blog20200906.oss-cn-hangzhou.aliyuncs.com/uPic/image-20200918070306551.png" alt="image-20200918070306551" style="zoom:50%;" />

增加一个大小维度：

<img src="https://blog20200906.oss-cn-hangzhou.aliyuncs.com/uPic/image-20200918070245651.png" alt="image-20200918070245651" style="zoom:50%;" />

### 3 热图

场景：例如， 用来展示哪个位置的订单最为集中

<img src="https://blog20200906.oss-cn-hangzhou.aliyuncs.com/uPic/image-20200918070703610.png" alt="image-20200918070703610" style="zoom:50%;" />



## 2 甘特图 

### 2.1 甘特图

现要制作不同类别产品在不同时间的发货时间图。

<img src="https://blog20200906.oss-cn-hangzhou.aliyuncs.com/uPic/image-20200918071059982.png" alt="image-20200918071059982" style="zoom:50%;" />

过程如下： 

1. 新建一个时间间隔的计算字段

<img src="https://blog20200906.oss-cn-hangzhou.aliyuncs.com/uPic/image-20200918071356010.png" alt="image-20200918071356010" style="zoom:25%;" />



2. 各个参数 

<img src="https://blog20200906.oss-cn-hangzhou.aliyuncs.com/uPic/image-20200918071930353.png" alt="image-20200918071930353" style="zoom:50%;" />

### 2.2 瀑布图制作 

<img src="https://blog20200906.oss-cn-hangzhou.aliyuncs.com/uPic/image-20200918072410292.png" alt="image-20200918072410292" style="zoom:50%;" />

1. 拖到子类别和利润到行列 

2. 将子类别排序，利润进行快速表计算-汇总 

<img src="https://blog20200906.oss-cn-hangzhou.aliyuncs.com/uPic/image-20200918072818036.png" alt="image-20200918072818036" style="zoom:25%;" />

3. 桌上最上面选择分析-合计-选择行总和

<img src="https://blog20200906.oss-cn-hangzhou.aliyuncs.com/uPic/image-20200918073849666.png" alt="image-20200918073849666" style="zoom:25%;" />

4. 在标记卡处将标记选为甘特条形图

<img src="https://blog20200906.oss-cn-hangzhou.aliyuncs.com/uPic/image-20200918073333679.png" alt="image-20200918073333679" style="zoom:25%;" />

5. 创建一个利润负值的计算（= -利润值），将其拖到标记卡大小上。初步的瀑布图建立： 

<img src="https://blog20200906.oss-cn-hangzhou.aliyuncs.com/uPic/image-20200918074232191.png" alt="image-20200918074232191" style="zoom:25%;" />

6. 更改图格式（亏损的灰色，盈利红色）： 将利润拖进标记卡的颜色处->点击颜色->编辑颜色，渐变颜色处选择2阶（颜色可以自己调整，我调为了红绿），高级处选择中心为0，勾选上包括合计。

<img src="https://blog20200906.oss-cn-hangzhou.aliyuncs.com/uPic/image-20200918074730114.png" alt="image-20200918074730114" style="zoom:25%;" />

结果：

<img src="https://blog20200906.oss-cn-hangzhou.aliyuncs.com/uPic/image-20200918074835035.png" alt="image-20200918074835035" style="zoom:30%;" />

7. 工具提示中的一些信息可以编辑 

 完成。

## 3 地图 

1. 标记国家/地区/城市数据中的地理位置信息

<img src="https://blog20200906.oss-cn-hangzhou.aliyuncs.com/uPic/image-20200918092331514.png" alt="image-20200918092331514" style="zoom:25%;" />

2. 创建地理位置分层：直接将小类别托到大类别上。

<img src="https://blog20200906.oss-cn-hangzhou.aliyuncs.com/uPic/image-20200918092720914.png" alt="image-20200918092720914" style="zoom:25%;" />

3. 双击维度栏中的省（行列中将会自动生成经度(生成)），将销售额拖到标记卡的颜色处，标记选择地图。具体如下：

<img src="https://blog20200906.oss-cn-hangzhou.aliyuncs.com/uPic/image-20200918093351567.png" alt="image-20200918093351567" style="zoom:50%;" />

4.  编辑地图设置：在屏幕最上方点击地图-编辑

<img src="/Users/Heihei/Library/Application Support/typora-user-images/image-20200918093529819.png" alt="image-20200918093529819" style="zoom:50%;" />

5. 编辑地图层，去掉一些选项，只留下中国地图 

<img src="https://blog20200906.oss-cn-hangzhou.aliyuncs.com/uPic/image-20200918093803365.png" alt="image-20200918093803365" style="zoom:25%;" />

6. 如果要详细展示每个省份的一些数据（比如人口，利润等），我们需要跟另外一些表或者图进行联动。操作如下：点击工具提示，选择插入，选择相应工作表： 

<img src="https://blog20200906.oss-cn-hangzhou.aliyuncs.com/uPic/image-20200918094219017.png" alt="image-20200918094219017" style="zoom:25%;" />



## 4 人口金字塔图 

目标图形： 

<img src="https://blog20200906.oss-cn-hangzhou.aliyuncs.com/uPic/image-20200918104641001.png" alt="image-20200918104641001" style="zoom:50%;" />

可以看到，上面的图本质是一个条形图，X轴是销售额，Y轴是数量。但是相比于一般的条形图，该图有几个地方比较特殊： 

> 1. 横坐标被分为两段。（因此，在数据上，应该存在两个分类/分组变量）——需要分组
>
> 2. X 轴的数据以固定顺序呈现。 ——需要建立数据桶

建立数据桶： 

1. 在度量右侧选中目标字段（这里是销售额），然后点击创建数据桶，选择一个合适的参数

<img src="https://blog20200906.oss-cn-hangzhou.aliyuncs.com/uPic/image-20200918104201037.png" alt="image-20200918104201037" style="zoom:25%;" />

2. 点击度量中的销售额，

3. 创建组 （右键地区，点击创建-组），在设置中将地区划分为南、北两个组

<img src="/Users/Heihei/Library/Application Support/typora-user-images/image-20200918100710163.png" alt="image-20200918100710163" style="zoom:25%;" />

<img src="https://blog20200906.oss-cn-hangzhou.aliyuncs.com/uPic/image-20200918101029715.png" alt="image-20200918101029715" style="zoom:25%;" />

4. 建立两个新字段，分别计算南区销售额和北区销售额。公式如下图： 

<img src="https://blog20200906.oss-cn-hangzhou.aliyuncs.com/uPic/image-20200918161222631.png" alt="image-20200918161222631" style="zoom:25%;" />



5. 将南北销售额分别拖入列，销售额拖入行。点击X轴，选择倒序。



## 5 帕累托图 

帕累托图适用于展示经济学现象，所谓的二八原则就起源于这里：百分之20%的人贡献了百分之80%的收入。当然，该图也适用于很多其他场景。

现在有两列数据： 

<img src="https://blog20200906.oss-cn-hangzhou.aliyuncs.com/uPic/image-20200919142624117.png" alt="image-20200919142624117" style="zoom:50%;" />

要用这两列数实现这样的功能： 

> 查看所有的产品类别中，销售额排名前百分之多少的产品可以实现80%的销售额。

目标图形 ： 

<img src="https://blog20200906.oss-cn-hangzhou.aliyuncs.com/uPic/image-20200919140707407.png" alt="image-20200919140707407" style="zoom:50%;" />

### 5.1 创建思路 

首先查看该图基础元素：坐标轴、图的类型、参考线（两条）。我们从这三个元素分别看下需要做哪些工作。

#### 5.1.1 坐标轴

先看坐标轴： 纵坐标是我们本次想要探索的因变量销售额，纵坐标的副坐标轴是销售累计百分比。横坐标是产品名称的百分比。

> 销售累计百分比：目前为止的所有产品的销售额占了总产品的百分之多少
>
> 产品名称百分比：到目前为止的产品种类占了总产品种类的百分之多少。

考虑到我们的原始数据只有产品名称和销售额，因此这个纵坐标轴的附轴、横坐标都需要我们手动计算。

> 任务一：新建一个新字段销售累计百分比，用来计算为止的所有产品的销售额占了总产品的百分之多少
>
> 任务二：新创建字段“产品名称百分比”，该字段可以计算到目前为止的产品种类占了总产品总类的百分之多少。 

#### 5.1.2 基础图形

可以看到，目标图像中的基础图形有两种：蓝色的柱状图、橙色的曲线图。结合图中有两个纵坐标轴，我们可以知道蓝色的柱状图是不同产品的销售额，橙色的曲线图是不同产品的累积销售额百分比。因此我们有了任务三： 

> 任务三：建立两幅图。第一幅是产品销售额与产品名称百分比的条形图，按照销售额大小降序排列。第二幅图是销售额累积百分比。 考虑到两幅图要合并到一幅图中，因此需要对副坐标轴的字段胶囊设置“双轴”。

#### 5.1.3 参考线 

图中我们可以看到两条参考线：一条纵坐标参考线用来销售额累积百分比，一条横坐标轴参考线用来产品名称百分比。并且，这两条参考线会随着我们的拖到而不断变化。因此，我们有了第四个任务： 

> 任务四：建立动态参考线 

#### 5.1.4 任务总结 

根据以上分析，我们知道了要做帕累托图，需要以下几个步骤： 

> 1. 创建新字段销售累计百分比、产品名称百分比
> 2. 建立销售额柱形图和累计百分比条形图，并合并到一个图中
> 3. 添加动态参考线 

具体操作步骤如下可见5.2 

### 5.2 创建过程

1. 创建销售额累计百分比字段 

1） 建立一个简单的产品名称与销售额的图，并按销售额进行排序 ，**注意视图选择整个视图**

<img src="https://blog20200906.oss-cn-hangzhou.aliyuncs.com/uPic/image-20200919080258705.png" alt="image-20200919080258705" style="zoom:25%;" />

2）创建新字段销售额累计百分比

<img src="https://blog20200906.oss-cn-hangzhou.aliyuncs.com/uPic/image-20200918163633523.png" alt="image-20200918163633523" style="zoom:50%;" />

> RUNNING_SUM : 返回给定表达式从分区第一行到当前行的运行总计。即累计汇总。

2. 创建累计百分比图

   1）用销售累计百分比替换销售额 

<img src="https://blog20200906.oss-cn-hangzhou.aliyuncs.com/uPic/image-20200919080709486.png" alt="image-20200919080709486" style="zoom:25%;" />

​		2）点击销售累计百分比下拉菜单，将计算依据改为产品名称 （以什么计算的，这里就改成什么）

<img src="https://blog20200906.oss-cn-hangzhou.aliyuncs.com/uPic/image-20200918165022303.png" alt="image-20200918165022303" style="zoom:25%;" />

3. 创建销售额柱形图，叠加双轴 

<img src="https://blog20200906.oss-cn-hangzhou.aliyuncs.com/uPic/image-20200919080945220.png" alt="image-20200919080945220" style="zoom:50%;" />

4. 创建产品名称数量百分比字段 

   1）点击计算字段，填写名称与公式：

<img src="https://blog20200906.oss-cn-hangzhou.aliyuncs.com/uPic/image-20200919061217369.png" alt="image-20200919061217369" style="zoom:50%;" />

​		Index返回当前产品序号,size计算总序号,整个公式实现产品名称从0到100的累加。

​	2）转换“产品名称数量百分比”字段的数据格式：选择产品名称数量下拉菜单,点击默认属性,选择数据格式---百分比-小数位数0

​	3)	将该字段拖到列,计算依据选择产品名称

<img src="https://blog20200906.oss-cn-hangzhou.aliyuncs.com/uPic/image-20200919081747461.png" alt="image-20200919081747461" style="zoom:25%;" />

5. 创建动态参数 

   维度下拉菜单选择创建参数，具体设置如下图

<img src="https://blog20200906.oss-cn-hangzhou.aliyuncs.com/uPic/image-20200919062313236.png" alt="image-20200919062313236" style="zoom:25%;" />

在副坐标轴添加参考线：选择副坐标轴，右键添加参考线，值选择刚才设置好的动态参数，即“销售额总量百分比参数”，标签选择为值

<img src="https://blog20200906.oss-cn-hangzhou.aliyuncs.com/uPic/image-20200919083554565.png" alt="image-20200919083554565" style="zoom:50%;" />

在左侧最下方参数这栏，点击下拉菜单，右键选择“选择参数控件”，此时调整右侧控件，参考线会发生变化

<img src="https://blog20200906.oss-cn-hangzhou.aliyuncs.com/uPic/image-20200919083955041.png" alt="image-20200919083955041" style="zoom:50%;" />

7. 添加横坐标轴参考线 

1）在计算字段处添加“横坐标轴参考线 ”，计算公式如下：

> if [销售累计百分比]<=[销售额总量百分比参数] then [产品名称数量%] else null end

**上面公式的意思是：当我们在动态控件处设置好一个销售百分比时（如80%），我们从第一个产品开始累加计算销售额是否到达了目标销售额（80%），如果没到，则把这些产品占总产品百分之多少的数据列出来。举个简单的例子来理解：**

> 假设现在我们4个产品：产品A占销售额30%，产品B占50%，产品C占10%，产品D占10%。现在我们在右侧的动态控件中将“销售额总量百分比参数”设置为80%，即我们需要找到有多少产品的销售额累加起来为总销售额的80%。此时我们在横坐标轴添加了公式，公式的输出结果25%，50%。

此时，我们只要在25%和50%中取最大值（后面会讲如何操作），那么我们就能知道百分之50%的产品贡献了80%的销售额。

2）完成后将该字段的数据格式设置为百分比（字段胶囊处的下拉菜单-默认格式-数字格式）

3）将横坐标轴参考线拖到标记卡的详细信息处。点击下拉菜单，计算依据改为产品名称（因为该图中所有字段的计算依据都是产品名称）

4）然后在工作表点击横坐标轴，右键选择“添加参考线”。

5）值选择刚才建好的动态参数，即“销售额总量百分比参数”，标签选择“值”，“最大值”（即我们的参考线只显示最大值，可以参考刚才第一个步骤中4个产品的例子理解）。另外格式可以适当更改，“突出显示或选的的数据点显示重新计算的线”前面的钩去掉。最后点击确定。

6）在右侧图例出编辑合适的度量名称

<img src="https://blog20200906.oss-cn-hangzhou.aliyuncs.com/uPic/image-20200919090726916.png" alt="image-20200919090726916" style="zoom:50%;" />



## 6 桑基图 & 留存图 

Tableau中实现较为复杂，可以自己找软件/网站。下面说留存图怎么做。

留存率图：用突出显示的表就行









