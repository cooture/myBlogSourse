---
title: 在Android中Menu的使用
date: 2017-09-28 00:58:26
tags:
	- Android
	- 入门
categories: Android
---

# 在Android中Menu的使用
## Menu的分类
1. 选项菜单(Options Menu);当用户触发 menu 项时弹出的菜单
2. 上下文菜单(Context Menu):用户长按那个控件时弹出的类似对话框
3. 弹出菜单，当用户点击某个 View 视图是弹出的菜单

## 前提准备
1. java创建了menu对象
2. 使用XML方法定义Menu要在XML文件中正确填写并添加ID

## 使用XML定义Menu

> XML文件的基本属性  

	<?xml version="1.0" encoding="utf-8"?>
	<menu xmlns:android="http://schemas.android.com/apk/res/android">
	    <item
	        android:id="@+id/daxiao"
	        android:title="设置字体大小"
	        android:orderInCategory="3">
	    </item>
	    <item
	        android:id="@+id/yanse"
	        android:title="设置字体颜色"
	        android:orderInCategory="2"
	        >
	    </item>
	    <item
	        android:id="@+id/shuxing"
	        android:title="设置字体属性"
	        android:orderInCategory="1">
	
	    </item>
	</menu>
	
					<!--
				        android:id="@+id/lalala_mune"  设置id
				        android:title="设置字体大小"      设置title
				        android:orderInCategory="3"     显示顺序
					-->
					
> Menu 菜单的嵌套使用规则  
1. Item 中可以嵌套 menu，但是不能嵌套 group2. Menu 中既可以嵌套 group，又可以嵌套 item。3. Group 中只能嵌套 item，不能嵌套 menu


## 选项菜单的添加
### 添加XML文件中的Menu

> 选项菜单需要重写在在java代码中重写onCreateOptionsMenu(Menu menu)方法  

	public boolean onCreateOptionsMenu(Menu menu) {
        /*第一步需要加载菜单选项*/
        /*菜单填充器将菜单获取然后添加至active中*/
        /*第一种比较麻烦的方法*/
        /*MenuInflater inflater = getMenuInflater();
        inflater.inflate(R.menu.options_menu,menu);*/
        /*第二种方法*/
        getMenuInflater().inflate(R.menu.options_menu,menu);
        
        return true;
    }
    
### 在Java代码中动态定义Menu
> 可以在java代码中的onCreateOptionsMenu(Menu menu)方法中使用menu.add()方法动态定义增加Menu

		/*另外可以通过代码添加menu项*/
        //menu.add(group id,itmeid  自己设置);里面填menu的分组  group可以是itme的父标签
        menu.add(Menu.NONE,ITMEID,Menu.NONE,"lalala我是后设置的");
        
        
## 上下文菜单
> 定义后添加的方法与选项菜单类似  
> 当用户长按 Activity 页面时，弹出的菜单我们称为上下文菜单。我们经常在 Windows 中用鼠标右键单击弹出的菜单就是上下文菜单。

1. 覆盖 Activity 的 onCreateContextMenu()方法，调用 Menu 的 add 方法添加菜单项MenuItem
2. 覆盖 onContextItemSelected()方法，响应菜单单击事件3. 调用 registerForContextMenu()方法，为视图注册上下文菜单

## 子菜单
> 定义后添加的方法与选项菜单类似  
> 子菜单就是将相同功能的分组进行多级显示的一种菜单，比如，Windows 的“文件”菜单中就有“新建”，“打开”，“关闭”等子菜单。创建子菜单的方法

1. 覆盖 Activity 的 onCreateOptionsMenu()方法，调用 Menu 的 addSubMenu()方法 添加子菜单项2. 调用 SubMenu 的 add()饭饭，添加子菜单项3. 覆盖 onCreateItemSelected()方法，响应菜单单击事件

## 添加单击事件

### 选项菜单

> 以下为对于使用XML文件加载的选项菜单为例  
> 选项菜单需要重写onOptionsItemSelected(MenuItem item)方法使其触发  

	 /**
     * !!只针对选项菜单!!
     * 当选项菜单被选中时调用的方法
     * @param item  表示菜单项对象
     * @return      false表示不进行处理
     */
    @Override
    public boolean onOptionsItemSelected(MenuItem item) {
    	//对于使用XML文件加载的菜单
        int itemid = item.getItemId();//获取触发的item的id
        float a;
        switch (itemid) {
            case R.id.daxiao:
                a =  ceshi.getTextSize();
                Toast.makeText(MainActivity.this,""+a,Toast.LENGTH_SHORT).show();
                if (a==100) ceshi.setTextSize(TypedValue.COMPLEX_UNIT_PX,50);
                    else ceshi.setTextSize(TypedValue.COMPLEX_UNIT_PX,100);
                break;
            case R.id.yanse:
                //随机生成颜色
                int red = (int) (Math.random()*256);
                int green = (int) (Math.random()*256);
                int blue = (int) (Math.random()*256);
                ceshi.setTextColor(Color.rgb(red,green,blue));
                break;
        }
        return super.onOptionsItemSelected(item);
    }
    
### 上下文菜单

上下文菜单:上下文菜单是和某一种控件绑定使用的，也就是说每个控件只有注册了上下文菜单，并且长 按时弹出的菜单就是上下文菜单，上下文菜单加载菜单是通过重写 onCreateContextMenu()来完成的，上下文菜单的 点击事件是通过抽重写 onContextItemSelected()方法来实现的

### PopMenu

是通过创建 popMenu 的对象，再通过菜单加载器将其加载进来的， popMenu 的点击事件是通过 popMenu.setOnMenuItemClickListener()方法实现的。


