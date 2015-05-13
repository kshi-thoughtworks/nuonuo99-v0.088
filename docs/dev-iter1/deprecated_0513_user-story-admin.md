## 管理员功能 - 开发 story

迭代 1, 重点是原料与产品管理,
管理员可登录 CMS 系统管理原料与产品.

注: 标记 TODO 的操作步骤, 需要细化

#### dev001. 为新签约供应商添加物料和产品

###### 预置条件

供应商已签约

###### 操作步骤与预期结果

1. 新增供应商, 填写供应商的基本信息、星级信息.

    操作结果: 数据库`供应商基本信息表`中成功增加一条供应商记录. `供应商业绩信息表`新增一条记录， 并赋初始值.
2. 添加供应商的物料, 填写物料基本信息.  -- TODO

    操作结果: 数据库中增加对应的 n 条物料信息.
3. 添加产品, 定价, 设置可购买时间等产品信息.  -- TODO

    操作结果: 数据库中增加对应的 1 条产品信息.

###### 注意事项

1. v1 版本, 不设专门的供应商 SLA 管理功能. 只进行简单的星级管理.
2. 此处的供应商, 是公司的概念, 司仪、主持人等自由职业者, 需要提供一个虚拟的公司身份。
3. 供应商的案例、宣传材料等, 不在该 story 讨论范围之内. 在供应商主页相关的 story 中讨论.

#### dev002. 打包婚礼方案, 供用户购买.

###### 预置条件

系统中存在多款用户可购买的产品.

###### 操作步骤与预期结果

1. 新增 1 条婚礼方案, 填写名称等基本信息.  -- TODO
2. 为婚礼方案添加 n 个产品, 打包销售.  -- TODO
3. 定价, 设置可购买时间等产品信息.  -- TODO

###### 注意事项

添加产品后, 再设置定价 / 可购买时间等产品信息. 方便验, 后续产品 / 商品概念分离.



###### 婚礼产品包属性
###### 司仪：
头像
服务理念    
主持场次    
从业时间    
风格      筛选  中式/西式/不限
性别      筛选  不限/男/女
年龄      筛选  不限  60后  80后  70后  90后
语言      
身高      筛选  170以下    170-175    175以上
籍贯      筛选  不限/各省
荣誉      
中式定妆照
西式定妆照
生活照
自我介绍视频
价格      筛选  2000以下  2000-4000  4000以上
级别      

###### 化妆师：
头像      
服务理念        
主持场次        
从业时间        
专业      筛选  不限/中式/西式
性别      筛选  男/女
年龄      
荣誉
    盘头          加价格        
    提供饰品       加价格  
    包含妈妈装     加价格
    包含伴娘装     加价格
价格
从业年限
常用化妆品品牌
化妆品是否进口
生活照
自我介绍视频
化妆师等级
价格
化妆风格   筛选  韩系/日系/不限


###### 花艺：
花艺类型    花门/花套/.....
花艺产品名称  
产品描述    
产品描述2   
产品描述3   
样图1
样图2
样图3
样图4
尺寸      
花材多选    花类型品种组合    
花朵数量    
颜色描述    色系品种组合
价格      
婚礼风格    中式/西式

###### AV产品
AV产品名称
产品描述
产品描述2
产品描述3
样图1
样图2
样图3
样图4
瓦数
覆盖面积      
起步价格      
起步数量      
计价数量      
计价价格      