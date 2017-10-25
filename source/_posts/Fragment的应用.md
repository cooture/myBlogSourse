---
title: Fragment的应用
date: 2017-10-26 00:33:22
tags:	
	- 	Android
	-  Fragment
	-  入门
categories: Android
---
# Fragment的应用
## 准备
1.	新建一个类，并继承Fragment（android.support.v4.app)
2. 为这个类创建一个布局文件作为fragment
3. 重写onCreatView()方法要求其返回一个view

## 静态加载
1. 建一个active以用来展示静态加载demo
2. 注意：新建的xml文件中需要添加xml布局文件的ID
3. xml文件中添加一个fragment，其中添加	android:name="刚刚建的fragment的包名"
4. 预览种可能无法显示fragment，需要添加	tools:layout="@layout/fragment_test"
5. 在主active中添加按钮并跳转到xml文件定义的fragment_demo中		startActivity(new Intent(this,DemoFragmentActivity.class));


## 动态加载
1.	在刚才的那个xml文件中新建一个framelayout标签（容器布局）以用来存放fragment，并添加ID
2. 添加一个button用来触发动态加载并创建事件addfragment（）；
3. 创建一个fragment管理器		FragmentManager fragmentManager = getSupportFragmentManager();	(如果主类使用继承的是activity的话则获取方法为getFragmentManager();)
4. 创建一个FragmentTransaction开启事务，并用刚才的管理器获取到FragmentTransaction对象		FragmentTransaction transaction = fragmentManager.beginTransaction();
5. 新建一个刚才的fragment类
6. 通过fragmentTransaction事务添加fragment		transaction.add(添加到的容器的ID，添加的fragment对象)；
7. 提交事务方可加载fragment		transition.commit();

 
  
  

**动态加载的典型代码**  


	public void addFragment(View view){
		FragmentManager fragmentManager = getSupportFragmentManager();
		FragmentTransaction transaction = fragmentManager.beginTransaction();
		FragmentDemo fragmentDemo = new FragmentDemo();
		transaction.add(R.id.framelayout，fragmentDemo)；
		transition.commit();
	}
	
