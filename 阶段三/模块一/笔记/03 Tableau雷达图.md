最近在学习用Tableau制作雷达图，对制作过程中的公式不是很明白，网上查了一圈也没有对雷达图制作过程中的公式有什么解释，因此自己搜索资料后写成下面的教程。

**声明：** 本文中Tableau操作内容来源于拉钩教育数据分析训练营，关于弧度的资料来源于维基百科。

### 1 画图背景

现在要通过雷达图来了解办公用品、技术、家具三个类别的产品在销售能力、盈利情况、销售额能力、市场空间、消费者信心度这五个角度的表现如何。数据如下：

<img src="https://blog20200906.oss-cn-hangzhou.aliyuncs.com/uPic/image-20200912143812048.png" alt="image-20200912143812048" style="zoom:50%;" />

最终要实现的结果如下：  

<img src="https://blog20200906.oss-cn-hangzhou.aliyuncs.com/uPic/image-20200913114832793.png" alt="image-20200913114832793" style="zoom:50%;" />

可以看到：上面的图片中，有五个灰色的五边形，分别代表各个维度的层级，数值为20、40、60、80、100。五个角分别代表销售能力、盈利情况、销售额能力、市场空间、消费者信心度五个指标。让我们看看如何实现以上雷达图。

### 2 画图思路 

#### 2.1 整体思路

可以看到，上面的图片中有五个灰色的规则五边形，以及办公用品、技术、家具三类产品组成的不规则五边形。可以把灰色的五边形看作一个处在下图坐标轴上的图形：  

<img src="https://blog20200906.oss-cn-hangzhou.aliyuncs.com/uPic/image-20200913144900511.png" alt="image-20200913144900511" style="zoom:50%;" />

对于每一个五边形，要想把它们画出来，可以以中心为原点建立一个坐标轴，把每个点的坐标标记出来，然后相邻的点之间连线就可以。要计算坐标，可以先计算每个点和原点之间的夹角角度，然后根据三角函数，计算出它们的X坐标和Y坐标。

> 例如，对于点A，只要知道半径r的长度，以及夹角1的角度，就可以根据三角函数算出A的坐标。x坐标为 r×cos(角度1)，Y坐标 r×sin(角度1)。

对于不同的灰色五边形，只要改变r的长度，就可以画出不同大小的五边形。因此，要画出雷达图，我们的步骤是： 

> 1. 在数据中标注好不同灰色五边形的半径长度，以及准备我们要展现的数据
> 2. 计算灰色多边形各个点的角度
> 3. 计算各个点的X、Y轴坐标
> 4. 将相邻坐标点连接，形成五边形
> 5.  将数据以彩色形式展现到灰色五边形构成的雷达图上

上面的步骤还存在最后一个问题： 

> 我们如果只将相邻的两个点的路径画出来，那么第5个点和第1个点不会相连（因为不连续）。为了达成第5个点和第1个点相连，我们需要格外增加一个点6，这个点的位置和第一个点重合。这样当我们设置路径时，第5个点和第6个点相连，在视觉呈现上等同于第5个点和第1个点相连。因此，在数据载入时，我们需要设置将第1个点的数据复制一列，将其作为第6个点。

所以，整体的步骤应该是：

> 1. 在数据中加入灰色五边形的半径长度，以及增加一列点6的数据，该列数据与点1的数据一样
> 2. 计算灰色多边形各个点的角度
> 3. 计算各个点的X、Y轴坐标
> 4. 将相邻坐标点连接，形成雷达图坐标（即五个灰色的五边形）
> 5.  将数据以彩色形式展现到灰色五边形构成的雷达图上

#### 2.2 Tableau操作过程

接下来对我们的原始数据进行操作： 

<img src="https://blog20200906.oss-cn-hangzhou.aliyuncs.com/uPic/image-20200912143812048.png" alt="image-20200912143812048" style="zoom:50%;" />

1 数据准备：将第一列销售能力复制一下，然后在数据下面增添5行。 如下图：

<img src="https://blog20200906.oss-cn-hangzhou.aliyuncs.com/uPic/image-20200913153935517.png" alt="image-20200913153935517" style="zoom:50%;" />

其中Ring1-5分别指五个灰色圆环的五个点所表示的数值大小。（注意: 此时有7列9行）  

2 将数据复制到Tableau （在excel中复制，然后在Tableau工作区的视图区域直接粘贴contrl+v），结果如下图：

<img src="https://blog20200906.oss-cn-hangzhou.aliyuncs.com/uPic/image-20200913153954265.png" alt="image-20200913153954265" style="zoom:50%;" />

3 点击tableau左下角数据源，找到刚才复制的数据，点击下拉菜单，选择文本文件数据，之后选择制表符（操作过程如下图：）

![image-20200912150114196](https://blog20200906.oss-cn-hangzhou.aliyuncs.com/uPic/image-20200912150114196.png)

可以看到左下角的标题有点奇怪，所以需要重新点击刚才的下拉菜单这，选择“字段名称位于第一行”。选完之后就会发现标题正常了但是出现了几列无用的数据（整个视图如右下角所示），这时选中值为空的那几列数据，右键选择删除就行。

![image-20200912151006341](https://blog20200906.oss-cn-hangzhou.aliyuncs.com/uPic/image-20200912151006341.png)

4 将多列指标转为一列 （选中几列指标，右键点击转置）

<img src="https://blog20200906.oss-cn-hangzhou.aliyuncs.com/uPic/image-20200913154344817.png" alt="image-20200913154344817" style="zoom:50%;" />

5 	结果如图

<img src="https://blog20200906.oss-cn-hangzhou.aliyuncs.com/uPic/image-20200912151649270.png" alt="image-20200912151649270" style="zoom:50%;" />

6 将上图的列2重命名为变量，列3重命名为数值

7 计算路径字段（步骤4中的变量是指维度中的变量这个字段，可以在写完case之后，将左侧维度下面的变量字段拖到case后面，会自动变成黄色的[变量]）

<img src="https://blog20200906.oss-cn-hangzhou.aliyuncs.com/uPic/image-20200912152606427.png" alt="image-20200912152606427" style="zoom:50%;" />

写计算方式时要注意是否有空格，例如源数据中如果1和销售能力之间有空格，那么这里写when ‘1 销售能力’时，1和销售能力之间也要有空格。

8 计算角度（弧度）

<img src="https://blog20200906.oss-cn-hangzhou.aliyuncs.com/uPic/image-20200912164404774.png" alt="image-20200912164404774" style="zoom:50%;" />

为了简化计算过程，我们用弧度来替代角度（两者本质上是一样的）来计算每个点的位置（**因此1弧度=180/π 度，1°=π/180 弧度**）。

> 弧度(radian)：弧长等于半径的弧，其所对应的圆心角为一弧度。

<img src="https://blog20200906.oss-cn-hangzhou.aliyuncs.com/uPic/image-20200912165245585.png" alt="image-20200912165245585" style="zoom:50%;" />

由上面这个图可以更直观的理解：对于一个特定的角度（蓝色部分），如果他的半径为1，并且对应的弧长为1，那么这个角度可以看做1个弧度。 对于半径为1的圆，它的周长2πr = 2π（因为r=1)，弧长为2π，对应的弧度也是2π（这里半径为1，即一个弧长对应一个弧度）。而我们知道一个圆有360°，**因此1弧度=360/(2π) 度，1°=2π/360 弧度**。

我们要做的雷达图是正五边形，如下图：  

<img src="https://blog20200906.oss-cn-hangzhou.aliyuncs.com/uPic/image-20200913112205354.png" alt="image-20200913112205354" style="zoom:50%;" />

要想在图中画出这个五边形，我们只需要建立一个二维坐标轴，知道五边形的五个点在这个坐标轴中的坐标就能画出五边形。要计算五边形的坐标，我们只需知道中心点距离各个点的位置（可以理解为圆的半径，对于一个正五边形，该值是固定的）、每个点的弧度，利用三角函数就能计算出X、Y坐标。  

首先计算每个点的弧度：例如对于正上方第一个点， 他的角度为90°，即90°×2π/360 =π/2 弧度。由于一个圆有2π弧度，那么五边形每相邻两点间的夹角为2π/5弧度。所以对于第二个点，它的弧度为 π/2-2π/5，第三个点的弧度为 π/2- 2×(2π/5)，第三个点弧度为 π/2- 3×(2π/5)....综上所述，五个点的弧度我们可以用以下公式： 

> 该点弧度 = π/2- (该点的顺序-1）×(2π/5)

算出了弧度后，我们可以根据三角函数计算每个点的坐标。

> X坐标 = 半径长度×cos（弧度)，Y轴坐标=半径长度xSin(弧度)  

例如：对于第一个点，他的x坐标为 半径长度xcos(π/2)，Y轴坐标为半径长度×sin(π/2)。 有了五个点的坐标，我们只需将五个点相连，就可以画出一个五边形。



9 计算坐标X、Y

<img src="https://blog20200906.oss-cn-hangzhou.aliyuncs.com/uPic/image-20200913151841978.png" alt="image-20200913151841978" style="zoom:50%;" />

Y的坐标计算同理.

10 画雷达图 

<img src="https://blog20200906.oss-cn-hangzhou.aliyuncs.com/uPic/image-20200913154834757.png" alt="image-20200913154834757" style="zoom:50%;" />

结果如下图： 

<img src="https://blog20200906.oss-cn-hangzhou.aliyuncs.com/uPic/image-20200913155058749.png" alt="image-20200913155058749" style="zoom:50%;" />

如果画出的五边形缺边，可以看下路径设置那里的代码是否正确，检查下变量中的名称和路径代码这里的名称设置是否对的上。  

最后，将类别拖到标记卡的颜色选项上:  

<img src="https://blog20200906.oss-cn-hangzhou.aliyuncs.com/uPic/image-20200913155308061.png" alt="image-20200913155308061" style="zoom:50%;" />

11 修改灰色轴颜色

<img src="https://blog20200906.oss-cn-hangzhou.aliyuncs.com/uPic/image-20200913155959047.png" alt="image-20200913155959047" style="zoom:50%;" />

注意点选后还要再选择一下灰色度。

12 把要展示的信息拖到工具提示 

<img src="https://blog20200906.oss-cn-hangzhou.aliyuncs.com/uPic/image-20200913160154148.png" alt="image-20200913160154148" style="zoom:33%;" />





至此操作完成。  

另外，如果要想制作六维度或者七维的雷达图，只要根据路径处的原理，来计算相应的弧度就可以。



### 参考资料 

1. 拉钩数据分析训练营课程资料

2. 维基百科-弧度](https://zh.wikipedia.org/wiki/%E5%BC%A7%E5%BA%A6#)

3. Mathword-Radian](https://mathworld.wolfram.com/Radian.html)

