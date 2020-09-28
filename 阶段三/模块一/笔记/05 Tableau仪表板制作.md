执著618期间销售凭空仪表盘

## 1 思路 

目标仪表板： 

<img src="https://blog20200906.oss-cn-hangzhou.aliyuncs.com/uPic/image-20200926063819060.png" alt="image-20200926063819060" style="zoom:50%;" />

一般会展示一些数据大盘，需要展示当天的，所以要新建一个字段，判断日期是否为最新日期，然后计算该日的销售量和各品类占比等信息。上面仪表板可以分为几块内容：

> 1 销售量计算 
>
> 2 销售量环比、同比计算
>
> 3 销售额完成百分比计算（靶心图）
>
> 4 各品类销售额占比（圆环图）
>
> 5 单品销量排行 

需要针对每一步进行操作，然后汇总为仪表盘。



## 2 数据准备

1. 将要合并的数据放到一个文件夹 
2. 进入数据源界面（导入一个数据 ，并将其重新拖出）

<img src="https://blog20200906.oss-cn-hangzhou.aliyuncs.com/uPic/image-20200920063125113.png" alt="image-20200920063125113" style="zoom:25%;" />

3. 选择新建并集，选项选择通配符（自动），清空工作簿后面内容，点击确定



## 3 制作图表

### 任务1：建立截止目前各销售指标完成的绝对值。

1.新建字段“是否最新日期”

建立一个新字段“是否最新日期”，计算公式如下： 

> [订单日期] = {FIXED:MAX([订单日期])}

将其拖动筛选器，筛选条件为真。



2.新建字段“最新日期”，用来动态更新表格标题

1）新建字段

<img src="https://blog20200906.oss-cn-hangzhou.aliyuncs.com/uPic/image-20200920082313091.png" alt="image-20200920082313091" style="zoom:25%;" />

2）把最新日期拖到详细信息中来，点击下拉菜单，将年改为天

> 图表中一般只能添加位于筛选器、标记卡、及行列中的一些信息，要想添加新信息，又不想让它们直接在图表中显示，可以将他们都拖到标记卡中的详细信息中 

<img src="https://blog20200906.oss-cn-hangzhou.aliyuncs.com/uPic/image-20200920083330175.png" alt="image-20200920083330175" style="zoom:25%;" />

3）修改标题 

<img src="https://blog20200906.oss-cn-hangzhou.aliyuncs.com/uPic/image-20200920083556930.png" alt="image-20200920083556930" style="zoom:25%;" />

4）任务一完成：

<img src="https://blog20200906.oss-cn-hangzhou.aliyuncs.com/uPic/image-20200920083727850.png" alt="image-20200920083727850" style="zoom:50%;" />



如果出现没有用到的信息,可以把“显示标题”前面的钩去掉 (**注意不要轻易做删除操作，可能影响后续表格显示与制作**)



### 任务2：计算环比增长情况（今天比昨天）

**新建一张工作表**

展示销量和销售额的环比

1.筛选出要计算的日期数据 

将订单日期拖到筛选器，选择“# 年/月/日”，点击下一步，在最上方“常规、条件、顶部”三个栏中选择“顶部这一栏”，填写参数

<img src="https://blog20200906.oss-cn-hangzhou.aliyuncs.com/uPic/image-20200920085121632.png" alt="image-20200920085121632" style="zoom:50%;" />

2 建立表格 

将订单日期拖到列（细化到天），将销售额、销量拖到行，并在它们的下拉菜单中选择“快速表计算”、“复合增长率”。智能显示处选择表格。

<img src="https://blog20200906.oss-cn-hangzhou.aliyuncs.com/uPic/image-20200920092924519.png" alt="image-20200920092924519" style="zoom:50%;" />

3 去除无用信息 

把表格中的标题都反选掉，同时把前一天的数据隐藏掉。结果如图： 

<img src="https://blog20200906.oss-cn-hangzhou.aliyuncs.com/uPic/image-20200920092546853.png" alt="image-20200920092546853" style="zoom:50%;" />





### 任务3：同比去年增长情况 

创建新字段“去年同期” 

> {FIXED :MAX(MAKEDATE(2019,MONTH([最新日期]),DAY([最新日期])))}

建立用来筛选去年同期和今年同期的字段“同比日期筛选”

> if [订单日期] = [最新日期] or [订单日期]=[去年同期]
> then 1 else 0 end 

<img src="https://blog20200906.oss-cn-hangzhou.aliyuncs.com/uPic/image-20200920095040898.png" alt="image-20200920095040898" style="zoom:25%;" />

隐藏掉标题的显示，然后转置一下： 

<img src="https://blog20200906.oss-cn-hangzhou.aliyuncs.com/uPic/image-20200920100700869.png" alt="image-20200920100700869" style="zoom:25%;" />

设置可视化: 

<img src="https://blog20200906.oss-cn-hangzhou.aliyuncs.com/uPic/image-20200920102019666.png" alt="image-20200920102019666" style="zoom:50%;" />



PS：如果操作有问题，例如订单日期拖到行中后，将其细化到天时，不能完整显示年、月、日（例如只显示年），可能的原因是之前在该工作表中对表做过隐藏、删除之类的操作。解决该问题的一个办法是重新建立一个工作表。



### 任务4： 目标完成百分比

需要用到靶心图 :

<img src="https://blog20200906.oss-cn-hangzhou.aliyuncs.com/uPic/image-20200920102202645.png" alt="image-20200920102202645" style="zoom:75%;" />

主要查看当前数据到目标数据的完成度。

做昨天的靶心图完成情况。 

**1 编辑数据：由于数据分布在两个表格中，需要将数据进行集合**

点击菜单栏“数据”——>“编辑关系”，可以看到主数据源和辅助数据源是按照订单日期进行关联的，点击“确定”。

<img src="https://blog20200906.oss-cn-hangzhou.aliyuncs.com/uPic/image-20200920102734080.png" alt="image-20200920102734080" style="zoom:25%;" />



此时点击主数据源，拖动主数据源一个字段到行/列。

去辅助数据源，可以看到辅助数据源的后面有个小的回形针，点击该标志，变红后表示已经关联成功。

<img src="https://blog20200906.oss-cn-hangzhou.aliyuncs.com/uPic/image-20200920103737687.png" alt="image-20200920103737687" style="zoom:50%;" />

完成，此时可以在主数据源和辅助数据源中对数据进行操作。

**2  将主数据源的“是否为最新日期”拖到筛选器进行筛选 **

**3 点击智能显示的靶心图。至此靶心图初步完成 **

**注意，有时候靶心图显示如下 ： **

<img src="https://blog20200906.oss-cn-hangzhou.aliyuncs.com/uPic/image-20200921070042302.png" alt="image-20200921070042302" style="zoom:25%;" />

我们可以看到上面的图型中蓝色条显示的是”销售额目标“，中间的参考线处显示的“销售额”，这与我们的预期不一样。我们的预期应该是以“销售额目标”为参考，销售额为蓝条。

> 即标记卡中的详细信息应该是“总和（销售额目标）”，列中的数值应该是“总和（销售额)”。

此时我们需要点击靶心图的坐标，选择“交换参考线字段”

<img src="https://blog20200906.oss-cn-hangzhou.aliyuncs.com/uPic/image-20200921070811370.png" alt="image-20200921070811370" style="zoom:25%;" />

然后我们就会看到靶心图变成我们要的样子：

<img src="https://blog20200906.oss-cn-hangzhou.aliyuncs.com/uPic/image-20200921073409589.png" alt="image-20200921073409589" style="zoom:25%;" />

**4 把完成度转换为百分比**

1）新建一个字段“完成百分比”

2）公式为“实际销售额/目标销售额”，将sum(销售额)/  将辅助数据源中的目标销售额拖到这（辅助数据源拖到公式后会自动生成聚合函数sum）

<img src="https://blog20200906.oss-cn-hangzhou.aliyuncs.com/uPic/image-20200921063403473.png" alt="image-20200921063403473" style="zoom:50%;" />





**5 回到主数据源，将完成百分比放到标记卡的标签上。**

> 如果在图中“完成百分比”显示的是数字，而不是百分数，可以在字段的默认格式处进行设置(在左侧度量处，找到“完成百分比”字段，然后右键选择默认属性--数字格式，选择百分比就行



### 任务5 目标值完成百分比 （圆环图制作）



1 建立一级品类与销售额的饼图 

<img src="https://blog20200906.oss-cn-hangzhou.aliyuncs.com/uPic/image-20200921104233326.png" alt="image-20200921104233326" style="zoom:25%;" />

2 对每个一级品类建立包含二级品类数目的饼图 

<img src="https://blog20200906.oss-cn-hangzhou.aliyuncs.com/uPic/image-20200921104545873.png" alt="image-20200921104545873" style="zoom:25%;" />

结果如下 ：

<img src="https://blog20200906.oss-cn-hangzhou.aliyuncs.com/uPic/image-20200921104649811.png" alt="image-20200921104649811" style="zoom:25%;" />

3 将饼图转换为圆环图

1） 将记录数拖两次到行（一个用来显示外环，一个用来显示内环），在下拉菜单将它们改为平均值，然后选择“双轴”

<img src="https://blog20200906.oss-cn-hangzhou.aliyuncs.com/uPic/image-20200921104932918.png" alt="image-20200921104932918" style="zoom:25%;" />

2） 右键副轴，选择同步轴，反选“显示标题”。结果如下： 

<img src="https://blog20200906.oss-cn-hangzhou.aliyuncs.com/uPic/image-20200921105350628.png" alt="image-20200921105350628" style="zoom:25%;" />

3）将饼图调整到中间 ：点击主轴，单击编辑轴。在编辑轴页面，范围选择固定，固定开始处选择0.8（自己看做坐标轴调整即可）。好了之后关系编辑轴页面，点击X轴，反选“显示标题”。

<img src="https://blog20200906.oss-cn-hangzhou.aliyuncs.com/uPic/image-20200921105858916.png" alt="image-20200921105858916" style="zoom:25%;" />

4）选择第一个平均值，让大小变大；选择第二个平均值，让大小变小。

<img src="https://blog20200906.oss-cn-hangzhou.aliyuncs.com/uPic/image-20200921110535000.png" alt="image-20200921110535000" style="zoom:25%;" />

最后，在第二个平均值处，将颜色选择为白色。 结果如下 ： 

<img src="https://blog20200906.oss-cn-hangzhou.aliyuncs.com/uPic/image-20200921110635048.png" alt="image-20200921110635048" style="zoom:25%;" />

5）设置圆环图的信息 

显示一级品类和二级品类可以如下操作：

<img src="https://blog20200906.oss-cn-hangzhou.aliyuncs.com/uPic/image-20200921111025130.png" alt="image-20200921111025130" style="zoom:25%;" />

操作完之后可以反选掉X轴的（显示标题），因为它提供的信息和我们的标签一样。

二级品类的操作类似：点击第标记卡处第一个平均值，将二级品类拖到标签

如果要显示各个二级品类的销售额占比： 

> 拖动销售额到标记卡第一个平均值的标签处-->在下面的字段胶囊中点击下拉菜单-->快速表计算选择“合计百分比” --> 计算依据选择“表向下”

另外一个小功能： 匹配标识颜色： 

<img src="https://blog20200906.oss-cn-hangzhou.aliyuncs.com/uPic/image-20200921112631359.png" alt="image-20200921112631359" style="zoom:25%;" />

其他操作类似，对外面的圆环操作，选择标记卡的第一个平均值；对里面的圆操作，选择标记卡的第二个平均值。

6）设置最后的格式 （把网格线去掉）

点击图表区，右键选择“设置格式” ，将网格线都去掉。

<img src="https://blog20200906.oss-cn-hangzhou.aliyuncs.com/uPic/image-20200921113412255.png" alt="image-20200921113412255" style="zoom:25%;" />

最后结果（圆环颜色可以自己调）： 



<img src="https://blog20200906.oss-cn-hangzhou.aliyuncs.com/uPic/image-20200921113534744.png" alt="image-20200921113534744" style="zoom:50%;" />



### 6 任务六：单品销量Top10展示：每个类别都展示前10



1 拖动SKU字段到筛选器，设置具体如下图所示： 

<img src="https://blog20200906.oss-cn-hangzhou.aliyuncs.com/uPic/image-20200925124231660.png" alt="image-20200925124231660" style="zoom:50%;" />

2 将相应字段拖到标记卡和行列中

<img src="https://blog20200906.oss-cn-hangzhou.aliyuncs.com/uPic/image-20200926061623438.png" alt="image-20200926061623438" style="zoom:50%;" />



## 4 汇总成仪表板

1 点击新建仪表板，左下方选择“浮动”

<img src="https://blog20200906.oss-cn-hangzhou.aliyuncs.com/uPic/image-20200926063041530.png" alt="image-20200926063041530" style="zoom:50%;" />

2 把之前的图表全部拖入，格式和颜色可以自己设置。如果要进行对齐操作，可以点击仪表板，在布局中的X、Y轴处进行设置。

<img src="https://blog20200906.oss-cn-hangzhou.aliyuncs.com/uPic/image-20200926063222944.png" alt="image-20200926063222944" style="zoom:50%;" />

3 最后的仪表板草图如下： 

<img src="https://blog20200906.oss-cn-hangzhou.aliyuncs.com/uPic/image-20200926063307237.png" alt="image-20200926063307237" style="zoom:50%;" />





 

