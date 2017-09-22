# auto_ui_test
这是selenium POM基于unittest 简单的测试框架  1、自动化框架 由一个或多个自动化测试基础模块、自动化测试管理模块、自动化测试统计模块等组成的工具集合。  2、根据不同的分类可以分为 按框架的定义分：基础功能测试框架、管理执行框架 按不同的测试类型来分：功能自动化测试框架、性能自动化测试框架 按测试阶段分：单元自动化测试框架、接口自动化测试框架、系统自动化测试框架 按组成结构分：单一自动化测试框架、综合自动化测试框架 按部署方式分：单机自动化测试框架、分布式自动化测试框架  3、自动化框架的原则： 测试框架脚本与业务、数据分离 测试框架与被测试应用程序独立 测试框架脚本应易于扩展、维护 测试脚本所使用语言应该与框架独立 测试框架不应该让框架的复杂性影响到测试人员  4、进入主题介绍selenium POM基于unittest 测试框架说明 1.第三方包功能重新封装 2.界面元素与测试内部对象名分离 3.脚本与数据分离 4.通过Jenkins持续从svn中获取测试用例，进行持续化集成  5、总体目录结构以及说明  1.1 conf 目录： 存放的是配置文件 1.2 data目录：存放Excel的文件，参数多少可以使用Excel参数存放和读取参数以及对于的值 1.3 public包：存放的封装的工具类 1.4 report ：测试报告 1.5 testcase : 存放的是测试用例 1.6 run_all.py : 运行入口  2、各模块介绍： 2.1 配置文件 如果我们程序没有任何配置文件时，这样的程序对外是全封闭的，一旦程序需要修改一些参数必须要修改程序代码本身并重新编译，这样很不好，所以要用配置文件，让程序在不同的操作系统以及环境中根据本地实际情况正常运行；配置文件有很多如INI配置文件，XML配置文件等。  conf 目录： 存放的是配置文件 conf,ini  2.2 数据文件 当我们的测试用例中需要填写很多参数时，为了方便修改以及读取，参数化就应运而生。使用参数，当我们后期维护测试用例时，可以减少必要的冗余，减少后期的维护量。  data目录：存放Excel的文件，参数多少可以使用Excel参数存放和读取参数以及对于的值 这个结合本地的项目自行选择  2.3 工具类的封装 首先要说明POM（PageObjectModel）的好处 POM是Selenium中的一种测试设计模式，主要是将每一个页面设计为一个Class，其中包含页面中需要测试的元素（按钮，输入框，标题 等），这样在Selenium测试页面中可以通过调用页面类来获取页面元素，这样巧妙的避免了当页面元素id或者位置变化时，需要改测试页面代码的情况。 当页面元素id变化时，只需要更改测试页Class中页面的属性即可。  base: 存放页面上的元素以及业务流程，业务流程比较复杂也可以单独重新封装业务流程，根据本地项目自行选择 login_page.py   common： 存放的工具类， 读取配置，获取Excel，发送邮件，读取数据库，封装的selenium的api等 base_obj.py      selenium的二次封装   get_config.py    获取配置文件   get_db.py        连接数据库   get_excel.py     获取Excel   get_files.py     获取测试报告   get_images.py    获取截图   get_log.py       获取日志   my_unit.py       unittest开始和结束，净化测试环境   send_email.py    发送邮件  pakeage: 存放第三方的包，浏览器的驱动等 HTMLTestRunner3.py   2.3 测试报告以及日志 存放测试报告以及日志 image：存放测试截图 log:存放的日志文件 report: 存放测试报告  2.4 testcase 存放测试用例，测试用例需要以 test 开头 login_case.py   2.5 run_all.py 程序的入口