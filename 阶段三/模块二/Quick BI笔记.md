月至今什么意思（MTD）？

Quick BI官方文档有非常详细的入门概述，包括如何准备、载入数据，如何进行可视化，并且还配备了非很多案例报表。详细信息可以参考[Quick BI](https://help.aliyun.com/document_detail/161417.html?spm=a2c4g.11186623.6.560.1b892e55YETnTU)，我这里仅对整体功能及操作逻辑做一个说明。

这意味着你在使用过程中，如果出现任何问题，优先可以去看官方文档，这是最方便也是最快速的方式。

QuickBI简介 

> 智能分析套件Quick BI是一个专为云上用户量身打造的新一代智能BI服务平台，也支持线下用户哟~
>
> Quick BI可以提供海量数据实时在线分析服务，支持拖拽式操作和丰富的可视化效果，帮助您轻松自如 地完成数据分析、业务数据探查、报表制作等工作。

优势在大屏可视化，在线产品，无需下载。具体启用如下：

<img src="https://blog20200906.oss-cn-hangzhou.aliyuncs.com/uPic/image-20200930061336433.png" alt="image-20200930061336433" style="zoom:25%;" />

收费：个人使用的标准版是499/一年，可以试用30天。 



四个步骤： 

> 1 数据源导入与管理
>
> 2 数据集处理 
>
> 3 仪表板进行可视化
>
> 4 数据门户进行可视化分析



# 2 数据导入与管理

添加数据，以CSV为例 

<img src="https://blog20200906.oss-cn-hangzhou.aliyuncs.com/uPic/image-20200930063352927.png" alt="image-20200930063352927" style="zoom:50%;" />

Excel导入时只能导入第一个sheet，要导入多个sheet只能将多个sheet放入多个表中。

上传CSV如果出现乱码，如

<img src="https://blog20200906.oss-cn-hangzhou.aliyuncs.com/uPic/image-20200930063906275.png" alt="image-20200930063906275" style="zoom:50%;" />

那么需要将csv改为UTF-8形式(用excel打开csv，另存为UTF-8CSV格式)

> 如果上传数据时选择本地上传，那么删除数据时要在两个地方删除：数据源中删除、数据集中找到同名文件进行删除

Excel、csv上传的限制： 

> 1 单个文件表头必须放第一行，Sheet1不能有合并单元格。
>
> 2 单个文件列数不超过100列。Excel文件大小建议不超过20M，CSV文件大小建议不超过50M。若文 件较大，建议以追加的方式分批次上传。
>
> 3 列的类型根据前100行确定: 如果前100行均为数字，则系统会识别此列为数值型。
>
> 4 如果有1行为字符串系统，则系统会识别此列为字符串型。 数值型字段不兼容字符串类型数据(一列数据中有任何一个是字符串类型，就会将该列定义为字符串），字符串类型可以兼容数值型数据。 温馨提示:请使用Chrome浏览器上传文件



# 3 管理数据集

数据源上传到QuickBI后，存储在QuickBI中，就称为数据集。

## 3.1 创建数据集

### 3.1.1 数据源中的表自动创建

当上传源数据到Quick BI时，数据会自动生成数据集

### 3.1.2 数据库导入 

在数据源中选择“即席分析SQL”，执行后选择右上角创建数据集

## 3.2 数据表关联 

在数据源中，点击目标数据，选择右侧的“编辑”

星状关联： 

<img src="https://blog20200906.oss-cn-hangzhou.aliyuncs.com/uPic/image-20200930073520053.png" alt="image-20200930073520053" style="zoom:50%;" />

雪花状关联： 

将上面的“订单是否退货”作为左表进行关联。

## 3.3 字段处理

具体有的功能如下：  

<img src="https://blog20200906.oss-cn-hangzhou.aliyuncs.com/uPic/image-20200930071232271.png" alt="image-20200930071232271" style="zoom:25%;" />

好了之后可以选择预览。有两个点需要注意

> 1 新增字段在预览中不能呈现
>
> 2 不能用新建的字段来计算新的字段



# 4 大屏可视化 

两个必备元素：

> 1 指标看板
>
> 2 仪表盘 

操作逻辑： 

<img src="https://blog20200906.oss-cn-hangzhou.aliyuncs.com/uPic/image-20201001085350109.png" alt="image-20201001085350109" style="zoom:50%;" />



操作逻辑：要操作东西，需要的思考步骤如下：

> 1 需要什么控件，图片/表格/图表（如柱形图等）/指标看板 ？——去左上角控件区查找
>
> 2 该控件中需要什么元素？——点击控件，去右侧设置中查找：数据有关的在”数据“中找，如字段的添加、计算、字段格式的显示；样式有关的，如坐标轴、颜色、字体、标题、背景等，去”样式“中找；其他功能看看”高级“是否包含

我把仪表板中各个控件及其操作的功能列了下  (3.8.1.0版）：

<img src="https://blog20200906.oss-cn-hangzhou.aliyuncs.com/uPic/image-20201001095752269.png" alt="image-20201001095752269" style="zoom:50%;" />



例如，我要在数据看板中展现“销售额的年同比”，并且需要相应颜色的箭头表示。那么我操作的逻辑如下:

> 1 需要数据看板——在控件区选择数据看板
>
> 2 需要展示“销售额的年同比”——这个数据位于看板上，所以直接在控件设计的右侧，找到数据进行操作（操作完不要忘记点更新） 
>
> 3 需要展示的箭头——箭头是一种样式，因此，需要在控件设置的“样式”中查找。另外箭头会根据数值变化，它的本质是一种条件函数呈现，所以需要在样式中中到条件格式对应的东西，即“功能配置”



这个逻辑在产品上体现的很完美，我们可以从版本演进来看到这一逻辑。例如老版中数据显示格式在样式中，新版本3.8.10将其放到了“数据”这一功能栏（[具体文档可点击此处](https://help.aliyun.com/document_detail/178418.html)），如下图： 

<img src="https://blog20200906.oss-cn-hangzhou.aliyuncs.com/uPic/image-20201001090853857.png" alt="image-20201001090853857" style="zoom:50%;" />

每次操作后记得保存！



# 常规图表



组合图的图标类型更改：

<img src="https://blog20200906.oss-cn-hangzhou.aliyuncs.com/uPic/image-20201001105216684.png" alt="image-20201001105216684" style="zoom:50%;" />



# 6 分析可视化 

## 6.1 细分分析： 如何突出问题重点

### 6.1.1 下钻上卷

建立层级结构后，将数据放入目标图表的维度，会出现钻取选项

<img src="https://blog20200906.oss-cn-hangzhou.aliyuncs.com/uPic/image-20201003062557578.png" alt="image-20201003062557578" style="zoom:33%;" />

下钻上卷不一定要在数据编辑处完成，在图表设计的数据这里，直接将目标维度拖动到钻取维度下面也可以，会自动形成三级结构。



### 6.1.2 图表联动

<img src="https://blog20200906.oss-cn-hangzhou.aliyuncs.com/uPic/image-20201003064715956.png" alt="image-20201003064715956" style="zoom:50%;" />

### 6.1.3 链接

<img src="https://blog20200906.oss-cn-hangzhou.aliyuncs.com/uPic/image-20201003065003020.png" alt="image-20201003065003020" style="zoom:50%;" />



## 6.2 预警分析：如何增强信息增益

<img src="https://blog20200906.oss-cn-hangzhou.aliyuncs.com/uPic/image-20201003075244323.png" alt="image-20201003075244323" style="zoom:50%;" />

趋势线-聚类在专业版中才有，个人版没有。

## 6.3 查询控件：如何进行信息集中

### 6.3.1 日期查询控件  

### 6.3.2 文本查询控件  

### 6.3.3 数值查询控件  

### 6.3.4 配置条件级联  

要实现的效果：

当选择特定的渠道类型时，渠道名称的筛选处只会显示该渠道类型下的一些渠道名称：

<img src="https://blog20200906.oss-cn-hangzhou.aliyuncs.com/uPic/image-20201003092222100.png" alt="image-20201003092222100" style="zoom:33%;" />

1 设置一级类目查询（渠道类型）

<img src="https://blog20200906.oss-cn-hangzhou.aliyuncs.com/uPic/image-20201003084119420.png" alt="image-20201003084119420" style="zoom:50%;" />



2  设置二级类目查询(渠道查询)：与一级类目的设置类似

<img src="https://blog20200906.oss-cn-hangzhou.aliyuncs.com/uPic/image-20201003091932430.png" alt="image-20201003091932430" style="zoom:50%;" />



3 配置条件级联

有两个地方可以配置条件级联：

1）在一级类目（渠道类型）处配置条件级联

<img src="https://blog20200906.oss-cn-hangzhou.aliyuncs.com/uPic/image-20201003092758103.png" alt="image-20201003092758103" style="zoom:50%;" />

<img src="https://blog20200906.oss-cn-hangzhou.aliyuncs.com/uPic/image-20201003090908490.png" alt="image-20201003090908490" style="zoom:50%;" />

2）点击空白页面配置  

<img src="https://blog20200906.oss-cn-hangzhou.aliyuncs.com/uPic/image-20201003092849736.png" alt="image-20201003092849736" style="zoom:30%;" />





## 6.4 其他分析：个性化展示

### 6.4.1 新增字段时涉及的函数

1 数字函数 

```
ABS(-7) = 7 CEILING(3.1415) = 4 FLOOR(3.1415) = 3 ROUND(3.1415,2) = 3.14 ROUND(324,-2) = 300
EXP(2) = 7.389
```

2 文本函数

```
REPLACE("Version8.5", "8.5", "9.0") = "Version9.0"
LENGTH("Matador") = 7
UPPER("Calculation") = "CALCULATION"
LOWER("ProductVersion") = "productversion"
TRIM(" Calculation ") = "Calculation"
LTRIM(" Matador ") = "Matador "
RTRIM(" Calculation ") = " Calculation"
SPLIT_PART (‘a-b-c-d’, ‘-‘, 2) = ‘b’ LEFT("Matador", 4) = "Mata" RIGHT("Calculation", 4) = "tion"
REGEXP_MATCHES(STRING TEXT, PATTERN TEXT [, FLAGS TEXT])
REGEXP_REPLACE(STRING TEXT, PATTERN TEXT, REPLACEMENT TEXT [, FLAGS TEXT])
```

3 日期函数 

```
DATE_PART('year', #2004-04-15#) = 2004 DATE_PART('month', #2004-04-15#) = 4 TO_DATE()
MAKE_INTERVAL(DAYS := 10) = 10 DAYS
```

4 聚合函数

```
SUM()
AVG()
MAX()
MIN()
MEDIAN()
COUNT()
COVAR_SAMP()
STDEV()
COVAR_POP()
{CORR(Sales, Profit)}
```

5 逻辑函数 

```
CASE
WHEN hour([report_date]) >= 0 and hour([report_date])<6 THEN '凌晨0-6' WHEN hour([report_date]) >= 6 and hour([report_date])<12 THEN '上午7-12' WHEN hour([report_date]) >= 12 and hour([report_date])<18 THEN ‘下午13-18’ ELSE ‘晚上19-23’
END
LEAD()
LAG()
RANK()
PERCENT_RANK()
LAST_VALUE()
```



# 7 案例实战：公司级销售大盘

载入需要的数据销售数据：

> 1 订单销售明细
>
> 2 订单是否退货 

其中，订单销售明细有22个字段如下：

> 1 省/自治区 
>
> 2  国家 
>
> 3 地区：如华东、西北等
>
> 4  产品ID： 如办公用品-美术-10001691
>
> 5 类别：如办公用品、家具、技术等
>
> 6 子类别：如美术、信封等 
>
> 7 产品名称：如Stanley速写本，蓝色 
>
> 8 订单ID 
>
> 9 订单日期(day)
>
> 10 订单日期(ymdhms): 如2015-01-21 00:00:00
>
> 11 发货日期(day)： 如20150123
>
> 12 发货日期(ymdhms)：如2015-01-21 00:00:00
>
> 13 邮寄方式：如一级、二级、标准、当日等 
>
> 14 客户ID 
>
> 15 客户名称 
>
> 16 细分：表示客户是哪种类型，如消费者、小型企业等
>
> 17 城市 
>
> 18 行ID 
>
> 19 销售额 
>
> 20 数量 
>
> 21 折扣
>
> 22 利润 

订单是否退货有字段如下：

> 1 订单ID 
>
> 2 退回： 是/否 

## 7.1 载入并查看数据 

### 7.1.1 载入数据 

在数据源中载入数据，并在数据集中检查是否出现，如果数据集中未出现目标数据集，那么在数据源中更需要找到对应的数据源并建立数据集。  

### 7.1.2 检查修改字段 

在数据集中查看各字段数据类型并查看是否需要对字段进行操作。例如“订单销售明细表”中，需要将国家、省、城市等字段转化为地理位置信息字段；看到一些有层级关系的字段，需要给它们建立层级关系；以及一些需要计算的字段。**修改完后别忘了点击保存**。

### 7.1.3 数据集关联

在数据集中进行数据关联。 

<img src="https://blog20200906.oss-cn-hangzhou.aliyuncs.com/uPic/image-20201004090442161.png" alt="image-20201004090442161" style="zoom:33%;" />

## 7.2 仪表板可视化

指标看板，在数据中看日环比、年同比、月至今、季至今等。然后数据中设置数据格式（度量的右上角设置标志）、在样式中设置样式。

> MTD和QTD的意思



