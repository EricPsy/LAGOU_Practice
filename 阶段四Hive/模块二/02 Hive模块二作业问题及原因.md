### 其他问题

如果用view:

```sql
create view userinfo_view as 
select gender,age,occupation,marital_status, count(distinct user_id) amount, 
concat(cast(round(100*count(distinct user_id)/(select count(distinct user_id) from model2_datas),2) as string),'%') amount_percent,
sum(purchase)/count(distinct user_id) avg_purchase,
sum(purchase) total_purchase,
concat(cast(round(100*sum(purchase)/(select sum(purchase) from model2_datas),2) as string),'%') purchase_percent
from model2_datas
group by gender,age,occupation,marital_status
grouping sets(gender,age,occupation,marital_status)
order by  purchase_percent desc;
```

<img src="https://blog20200906.oss-cn-hangzhou.aliyuncs.com/uPic/image-20201225121716604.png" alt="image-20201225121716604" style="zoom:50%;" />

视图下不存数据，但是怎么查看数据？？



现在有表查出来了，可以把查出来的表直接导出吗，还是必须在导出的语句中把select的查询代码重写写一遍？有没有更好的办法？



报错

1 把数值用concat和cast转为百分比形式后直接用order by排序，但是字符排序是一个字符一个字符对比的

2 报错 ：FAILED: SemanticException [Error 10025]: Line 4:7 Expression not in GROUP BY key '10'

```sql
select product_id, count(product_id) sales, count(product_id)/(select count(product_id) from model2_datas) sale_percent, rank() over(order by count(product_id)) rank_number
from model2_datas
group by product_id
having rank_number <=10
order by rank_number ;
```

原因：开窗函数和group by 一起使用了。开窗函数返回多列，group by返回合并列，列数明显冲突。

```sql
select *,rank() over(order by sales) rank_number
from (
  select product_id, count(product_id) sales, 
  concat(round(100*count(product_id)/(select count(product_id) from model2_datas),4),'%') sale_percent
  from model2_datas
  group by product_id
  order by sales desc
  limit 10
)  ; 
```

报错：ParseException line 3:2 cannot recognize input near '(' 'select' 'product_id' in joinSource

原因，需要给子查询命名，否则无法查询。



4 细化分析第一题原来代码：

```sql
select *
from 
(select *, rank() over(partition by gender,product_category_1, product_category_2,product_category_3,product_id order by sales desc) rank_number 
from ( 
select gender,product_category_1, product_category_2,product_category_3,product_id,count(1) sales,sum(purchase) purchase,sum(purchase)/(select sum(purchase) from model2_datas) purchase_percent
from model2_datas
group by gender,product_id  
) a
) b 
where rank_number <=10;
```

报错

> FAILED: SemanticException [Error 10025]: Line 5:14 Expression not in GROUP BY key 'product_category_1'

检查后错误的点有两个：

1.table a中，group by后面没有放product_category1,2,3。

> product_id属于类别1、2、3之中，已经以更细颗粒度的product_id 进行group by了，并且在select中需要加上类别1-3，因此在group by后面也需要加上类别1，2，3。加上之后的结果其实和“select 不要类别1-3，以及group by后面只放product_id”的结果是一样的。

2.table b中，partition后面只要放gender就行了，不用放其他。

> 原因是我们要的是各性别内的产品排名，因此是以性别为划分的。如果加上了product_id，相当于以product_id为划分，那么结果就是所有的结果排序都是1.