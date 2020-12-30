### Hive 基础知识

分布式计算( Distributed computing )是一种把需要进行大量计算的工程数据分割成小块，由多台计算机分别计算，在上传运算结果后，将结果统一合并得出数据结论的科学。

Hadoop

> Hadoop不是指具体的一个框架或者组件，它是Apache软件基金会下用Java语言开发的一个开源分布式 计算平台，实现在大量计算机组成的集群中对海量数据进行分布式计算，适合大数据的分布式存储和计 算，从而有效弥补了传统数据库在海量数据下的不足。

Hadoop生态圈

<img src="https://blog20200906.oss-cn-hangzhou.aliyuncs.com/uPic/image-20201125104455402.png" alt="image-20201125104455402" style="zoom:50%;" />

总体理解：

<img src="https://blog20200906.oss-cn-hangzhou.aliyuncs.com/uPic/image-20201125104614479.png" alt="image-20201125104614479" style="zoom:50%;" />

HDFS（分布式存储）： 

> HDFS就是将文件切分成固定大小的数据块block(文件严格按照字节来切,所以若是最后切得省一点点,也 算单独一块,hadoop2.x默认的固定大小是128MB,不同版本,默认值不同.可以通过Client端上传文件设 置)

分布式计算(MapReduce)

> MapReduce就是"任务的分解与结果的汇总"。

mapreduce包含mapper、reducer两个部分，具体执行过程如图

<img src="https://blog20200906.oss-cn-hangzhou.aliyuncs.com/uPic/f7fbb747fc3e7a42112f1ccf82cfa1c7_r.jpg" alt="preview" style="zoom:50%;" />

详细理解可以参考这篇文章(https://www.zhihu.com/question/23345991)

Hive 

> Hive是Facebook为了解决海量日志数据的统计分析而开发的基于Hadoop的一个**数据仓库工具**(后来开 源给了Apache软件基金会)，可以将**结构化**的数据文件映射为一张数据库表，并提供类SQL查询功 能.HQL。本质上:将HQL语句转换为MapReduce任务进行运行(转化流程如下)

Hive 用于海量数据的离线分析。 Hive 具有sql数据库的外表，但应用场景完全不同，Hive 只适用于批量数据统计分析。

流程如下：

<img src="https://blog20200906.oss-cn-hangzhou.aliyuncs.com/uPic/image-20201125104850945.png" alt="image-20201125104850945" style="zoom:50%;" />

#### Hive架构

<img src="https://blog20200906.oss-cn-hangzhou.aliyuncs.com/uPic/image-20201125104952955.png" alt="image-20201125104952955" style="zoom:50%;" />

用户接口：

> Client CLI(hive shell)、JDBC/ODBC(java 访问 hive)、WEBUI(浏览器访问 hive)

元数据:

> Metastore 元数据包括:表名、表所属的数据库(默认是 default)、表的拥有者、列/分区字段、表的类型(是否是外部表)、表的数据所在目录等;

驱动器:Driver

> (1)解析器(SQL Parser):将 SQL 字符串转换成抽象语法树 AST，这一步一般都用第三方工具库完成，比如 antlr;对 AST 进行语法分析，比如表是否存在、字段是否存在、SQL语义是否有误。
>
> (2)编译器(Physical Plan):将 AST 编译生成逻辑执行计划。
>
>  (3)优化器(Query Optimizer):对逻辑执行计划进行优化。
>
> (4)执行器(Execution):把逻辑执行计划转换成可以运行的物理计划。对于 Hive 来说，就是MR/Spark。

hive与传统数据库对比：

<img src="https://blog20200906.oss-cn-hangzhou.aliyuncs.com/uPic/image-20201125110558585.png" alt="image-20201125110558585" style="zoom:50%;" />





ping时停不下来，按command+c



### 1 Hive DDL：数据定义语言

#### 1.1 Hive启动与关闭

1）开启虚拟机

2）用terminus链接

3）启动hive

<img src="https://blog20200906.oss-cn-hangzhou.aliyuncs.com/uPic/Hive%E5%90%AF%E5%8A%A8:%E5%85%B3%E9%97%AD%E6%AD%A5%E9%AA%A4.png" alt="Hive启动:关闭步骤" style="zoom:50%;" />

> 1. start-all 已经弃用，可以用start-dfs.sh and start-yarn.sh (stop同理)
> 2. terminus中按table键可以自动补全目录
> 3. su-hadoop进入后，用ls / 可以查看目录
> 4. start 后，可以用jps来看是否正常启动，若正常启动，再cd
> 5. start-all 表示启动所有的节点

#### 1.2 数据库查看及删除

创建数据库

```sql
create database 数据库名;
```

查看数据库

```sql
show databases;
```

删除空数据库

```sql
drop databse 数据库名;
```

删除非空数据库

```sql
drop database 数据库名 cascade
```

进入数据库

```sql
use 数据库名;
```

#### 1.3 创建数据表

1. 查看数据库中是否有数据表

```
show tables;
```

2. 创建数据表 

1）直接建表

内部表

```
create table 表名(字段名1 字段类型, 字段名2 字段类型)
```

外部表

```sql
create external table 表名
```

```sql
 create external table test_external_1(id int, name string) location '/datas/test_external_1';  #location后面指定放置的文件及位置
```

插入数据和其他操作和内部表一样，不用加external。只在删除时代码有些区别。

Hive内部表与外部表区别：

<img src="https://blog20200906.oss-cn-hangzhou.aliyuncs.com/uPic/image-20201209111536132.png" alt="image-20201209111536132" style="zoom:50%;" />

> **元数据**（**Metadata**），又称**中介数据**、**中继数据**，为描述[数据](https://baike.baidu.com/item/数据/5947370)的数据（data about data），主要是描述数据[属性](https://baike.baidu.com/item/属性/1405051)（property）的[信息](https://baike.baidu.com/item/信息/111163)，用来支持如指示存储位置、[历史](https://baike.baidu.com/item/历史/360)数据、[资源](https://baike.baidu.com/item/资源/9089683)查找、文件记录等功能。
>
> **元数据**（**Metadata**），又称**中介数据**、**中继数据**，为描述[数据](https://baike.baidu.com/item/数据/5947370)的数据（data about data），主要是描述数据[属性](https://baike.baidu.com/item/属性/1405051)（property）的[信息](https://baike.baidu.com/item/信息/111163)，用来支持如指示存储位置、[历史](https://baike.baidu.com/item/历史/360)数据、[资源](https://baike.baidu.com/item/资源/9089683)查找、文件记录等功能。

2）复制建表

```
create table 表名 like 表名；
```

只复制表结构，不复制数据

3）查询建表

create [EXTERNAL] table [IF NOT EXISTS] 表名 as select 语句;

例如：

```sql
create table NewTableBySelect as select * from test_create_table;
```

会导入数据

- 使用查询创建并填充表，select 中选取的列名会作为新表的列名(所以通常是要取别名)，会改变 表的属性、结构，比如只能是内部表、分区分桶也没了

- 目标表不允许使用分区分桶的;对于旧表中的分区字段，如果通过 select * 的方式，新表会把它 看作一个新的字段，这里要注意 ;

- 目标表不允许使用外部表，会报错
-  创建的表存储格式会变成默认的格式 TEXTFILE ,可以指定表的存储格式，行和列的分隔符等。

3. 查看表结构

```
desc 表名
```

4. 查看表的具体信息:lacation等--**查看表在创建时有哪些数据，例如有无分区**

```
show create table test_create_table;
```

进入hadoop页面(http://192.168.5.100:50070/)，点击Utilities进入系统：

<img src="https://blog20200906.oss-cn-hangzhou.aliyuncs.com/uPic/image-20201209110325167.png" alt="image-20201209110325167" style="zoom:33%;" />

选择user

<img src="https://blog20200906.oss-cn-hangzhou.aliyuncs.com/uPic/image-20201209110503214.png" alt="image-20201209110503214" style="zoom:33%;" />

选择hive，进入数据库。

5. 注释 

用comment

```
create table table_Comment(id int comment '编号',name string comment '姓名') comment '员工信息表';
```

6. 插入数据(与mysql一样)

```
insert into test_create_table values(1,'test');
```

```
select * from 表名 （和sql代码一样）
```



#### 1.4 指定分隔符建表

<img src="https://blog20200906.oss-cn-hangzhou.aliyuncs.com/uPic/image-20201209161025394.png" alt="image-20201209161025394" style="zoom:33%;" />

^A ：字段与字段的分隔符

^B：array(数组)内各个元素间的分隔符

^C：map的分隔符。相当于python字典中key与元素之间那个冒号



#### 1.5 案例：搭建电商线下单业务流程数据库

现在ATOM或者文本中写好hive代码，然后直接执行就行。文件类型为sql。

```
cd /home/hadoop/datas
ls
vim shop_test.sql #目标文件夹名字
cd /opt
ls 
cd /module 
ls
cd apache-hive-3.1.1-bin/  #这里是hive的安装目录：即module/apache...
hive - f '/home/hadoop/datas/shop_test.sql' #即文件路径
```

分区与分桶的区别

+ 分区使用表外字段，分桶使用表内字段
+ 分区对应不同的文件夹，分桶对应不同的文件
+ 分区可以进行添加、删除、清空操作，分桶则不行



### 2 Hive DML：数据操作语言 （加载、删除）



#### 案例

<img src="https://blog20200906.oss-cn-hangzhou.aliyuncs.com/uPic/image-20201211105206008.png" alt="image-20201211105206008" style="zoom:50%;" />

### 2 hive常用按钮

```
!clear;  #清屏幕
```

```
dfs -lsr / ; # 执行dfs命令
```



### 其他问题

#### 1 hive内部表与外部表的区别

**对于外部表-**

- 外部表将文件存储在HDFS服务器上，但表未完全链接到源文件。

- 如果删除外部表，该文件仍保留在HDFS服务器上。

  例如，如果您使用HIVE-QL在HIVE中创建一个名为**“ table_test”**的**外部表**并将该表链接到文件**“ file”**，***则从HIVE中删除“ table_test”不会从HDFS中删除“ file”\***。

- 有权访问HDFS文件结构的任何人都可以访问外部表文件，因此需要在HDFS文件/文件夹级别管理安全性。

- **元数据保留在主节点上，从HIVE中删除外部表只会删除元数据，而不会删除数据/文件。**

**对于内部表-**

- 根据设置存储在目录中`hive.metastore.warehouse.dir`， ***默认情况下，内部表存储\***在以下目录***“ / user / hive / warehouse”中，\***您可以通过更新配置文件中的位置来进行更改。
- 删除表将分别从主节点和HDFS中删除元数据和数据。
- 内部表文件安全性仅通过HIVE控制。安全需要在HIVE内部进行管理，可能需要在架构级别（取决于组织）进行管理。

####  2 hive结构体与map的区别

STRUCT则封装一组有名字的字段（named filed）,其类型可以是任意的基本类型，元素的访问使用点号

在整体形式上两者相似，但map中的values其类型都是一样的，全部为string或者全部为int。而结构体struct的value类型可以不一样。另外map的访问是map['key']来访问value，而struct的访问是通过struct.元素名的方式来返回元素的值。

#### 3 执行顺序

执行顺序：

from … where … select … group by … having … order by …

其实总结hive的执行顺序也是总结mapreduce的执行顺序：

MR程序的执行顺序：

map阶段：

 1.执行from加载，进行表的查找与加载

2.执行where过滤，进行条件过滤与筛选

3.执行select查询：进行输出项的筛选

4.执行group by分组：描述了分组后需要计算的函数

5.map端文件合并：map端本地溢出写文件的合并操作，每个map最终形成一个临时文件。 然后按列映射到对应的reduceReduce阶段：

Reduce阶段：

1.group by：对map端发送过来的数据进行分组并进行计算。

2.select：最后过滤列用于输出结果

3.limit排序后进行结果输出到HDFS文件

所以通过上面的例子我们可以看到，在进行selectt之后我们会形成一张表，在这张表当中做分组排序这些操作。





#### 4 Terminus进入hive后，代码输错了怎么删除，delete好像删除不了。里面的基本操作是操作linux系统吗？



#### 5 hive本地数据载入报错 

hive (lagou)> load data local inpath '/home/hadoop/datas/model2_datas.csv' overwrite into table model2_datas
            >  ;
FAILED: SemanticException Line 1:23 Invalid path ''/home/hadoop/datas/model2_datas.csv'': No files matching path file:/home/hadoop/datas/model2_datas.csv

出错的原因

> 我直接把数据所在的电脑路径打上来了，但是Hive本地装载数据中的"本地"指的是服务器的本地，而非我们电脑所在的“本地”。接下来我们把远程服务器称为本地，我们自己的电脑称为“本机”，来实现“本机”数据导入hive表格。

百度了很多教程，都默认本地是服务器，没有明确说明“本地”这个概念，因此作为小白我一头雾水。直到看到[hive Invalid path xxxx: No files matching path file: xxxx](https://blog.csdn.net/shengruxiahua2571/article/details/103074123) 才明白原来本地路径指的是服务器的路径。我想很多教程没有说明的原因是因为分布式计算所用到的数据量非常大，不太可能存在自己的电脑上，默认是存在服务器上的。因此本地装在数据在这种情况下非常好理解，就是指服务器。但是对于非计算机背景的初学者，没有任务服务器知识，所以我们搭建好伪分布式的练习环境、下载了少量练习数据到自己的电脑，我们往往会把教程中的“本地”当做自己电脑上的本地。因此会报错。  

那么如何将自己电脑上的文件传到hive中就是一个问题。我为这个问题折腾了一天，想把整个过程写出来，希望能帮助需要的人。在操作之前有几个前提假设：

> 1. 假设操作者可以无障碍连接虚拟机：如果是hive练习，在自己电脑上用了伪分布式服务器，就假设你已经会用远程连接虚拟机；如果是真实场景，就假设你已经可以无障碍连接远程服务器。
> 2. 操作的电脑是Mac，windows的操作原理同理。

接下来从头说明如何将你电脑上的数据载入到hive表。

> 1. 想好要把数据存储在服务器的什么位置。  
>
>    假设现在已经启动hadoop，但是没有进入hive。可以在服务器界面输入
>
> ```
> ls /
> ```
>
> 看一下有哪些目录，例如我的界面就是：
>
> <img src="https://blog20200906.oss-cn-hangzhou.aliyuncs.com/uPic/image-20201224134731700.png" alt="image-20201224134731700" style="zoom:50%;" />
>
> ps: 在服务器界面的所有操作都会用到linux代码，包括如何移动文件夹、创建文件夹、访问文件、修改保存文件等，如果这方面不是很清楚，可以去百度下linux的常用代码。对于Mac用户来说，平时在terminal中操作用到的代码就是linux代码。
>
> 看到目录后，想好你想把数据存在服务器的哪个位置。比如，我想存储在home这个文件夹中：
>
> <img src="https://blog20200906.oss-cn-hangzhou.aliyuncs.com/uPic/image-20201224135229836.png" alt="image-20201224135229836" style="zoom:50%;" />
>
> 上面的代码意思是，移动到home文件夹中的hadoop文件夹中，用ls指令看下该文件夹下有什么文件，结果发现有datas怎么一个文件夹。
>
> 2. 把本机文件上传到服务器。
>
> 打开terminal，输入
>
> ```
> scp '文件在计算机上的路径' root@服务器IP:服务器中的存储位置
> ```
>
> 例如，我要把电脑桌上上的csv文件存入到服务器的home/hadoop/datas文件夹中，我的服务器IP是111.112.113.114，那么我应该输入：
>
> ```
> scp '/Users/name/Desktop/model2_datas.csv' root@111.112.113.114:/home/hadoop/datas/
> ```
>
> 接下来会要求你输入服务器的密码，输入就可以。如果成功加载数据会在界面显示加载进度，例如：
>
> <img src="https://blog20200906.oss-cn-hangzhou.aliyuncs.com/uPic/image-20201224140238252.png" alt="image-20201224140238252" style="zoom:50%;" />
>
> 3. 重新回到服务器界面，我们可以看到数据已经加载成功：
>
> ```
> [hadoop@node100 data]$ cd /home/hadoop/datas 
> [hadoop@node100 data]$ ls
> model2_datas.csv  --返回的结果
> ```
>
> 上面可以看到datas文件夹中已经有我们载入的csv数据。
>
> 4. 将数据载入到hive表：
>
> 1）首先进入hive的数据库界面，进入你的数据库，然后根据你的数据创建一个表：
>
> ```
> create table 表名
> (字段 字段类型，
> 字段2 字段类型2，
> ....)
> row format delimited fields terminated by ',' --指定字段间的分隔符
> tblproperties(
> "skip.header.line.count"="1" --跳过文件行首1行
> )
> ```
>
> 2）将服务器本地的数据载入hive表
>
> ```
> load data local inpath '服务器中的文件路径' into table 表名
> ```
>
> 例如我刚才的例子，代码就是
>
> ```
> load data local inpath '/home/hadoop/datas/model2_datas.csv' into table model2_datas.csv
> ```



参考资料 

1. 拉勾数据分析训练营资料
2. 百度linux代码资料
3. [hive Invalid path xxxx: No files matching path file: xxxx](https://blog.csdn.net/shengruxiahua2571/article/details/103074123)

4. [Hive之 Hql语法解析](https://developer.aliyun.com/article/566078)
5. [实战Hive本地文件系统导入数据](https://blog.csdn.net/zt15732625878/article/details/85926402)
6. [mac与虚拟机传输文件](https://www.cnblogs.com/soymilk2019/p/13517937.html)
7. [Mac终端连接虚拟机及传输文件](https://www.pianshen.com/article/39621347904/)

#### 6 hive查询结果显示字段名

进入hive页面后，有时候在hive后不会显示数据库名称，临时方式是在hive客户端设置参数：hive.cli.print.current.db为true

```
hive> set hive.cli.print.current.db;
hive.cli.print.current.db=false
hive> set hive.cli.print.current.db=true;
hive (default)> use test;
```

hive查询结果默认是不显示字段名的，要显示的话通过设置参数：hive.cli.print.header为true就可以显示字段名称。

```bash
hive (test)> set hive.cli.print.header=true;
```

但是这样的话，除了字段名称，表名称也显示出来了，这是为了防止字段名出现重复的，所以在字段名前面加上了表名。

如何去除表名？设置参数hive.resultset.use.unique.column.names为false就可以不显示表名。

```
hive (test)> set hive.resultset.use.unique.column.names=false;
```

**永久生效**

前面三步的设置都是在当前客户端临时生效的，如果退出客户端，那么又会回到之前的设置，如何将这些设置永久生效呢？就需要修改hive-site.xml配置文件。在该文件中加入如下三个配置内容：

```
  <property>
    <name>hive.cli.print.header</name>
    <value>true</value>
  </property>
  <property>
    <name>hive.resultset.use.unique.column.names</name>
    <value>false</value>
  </property>
   <property>
    <name>hive.cli.print.current.db</name>
    <value>true</value>
  </property>
```

参考资料：

[Hive高阶之显示数据库名称和字段名](https://zhuanlan.zhihu.com/p/59767587)

####  7 sql：如何在group by后，求所有值的和。

#### 8 hive导出数据时报错：movetask

代码

<img src="https://blog20200906.oss-cn-hangzhou.aliyuncs.com/uPic/image-20201226092506676.png" alt="image-20201226092506676" style="zoom:50%;" />

结果：

<img src="https://blog20200906.oss-cn-hangzhou.aliyuncs.com/uPic/image-20201226092557533.png" alt="image-20201226092557533" style="zoom:50%;" />



#### 9 数据量大时如何进行全局排序？

order by只能进行reducer=1时的全局排序，sort by只能对reducer内排序，那数据量大时怎么全局排序？？有没有这种需求存在，为什么？

order by前需要对reducer个数进行设置吗？为什么我的order by无效



[hive的全局排序和局部排序](https://blog.csdn.net/weixin_38629422/article/details/109745613) ?
