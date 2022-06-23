# Crosst 第三方UWP

>真正的菜鸡会把自己会的东西全部展现出来撑门面，而不是躲在后面自谦(｀･ω･)
>    —— Igor


https://space.bilibili.com/18340402/channel/seriesdetail?sid=1276538&ctype=0
我正在使用此教程
## Learning
### Learning Days 01 - 2022.01.25
**绝赞摸鱼中**

### Learning Days 02 - 2022.01.26

```xml
<StackPanel><!--侧边栏-->
    <StackPanel Orientation="Horizontal" HorizontalAlignment="Right">
    	<Button Name="Sidebar" Width="40" Height="40" />
	</StackPanel>
</StackPanel>
```
```cs
private void Sidebar_Show(object sender, RoutedEventArgs e)
        {
            //侧边栏开启
        }
```
侧边栏搁置了.
***


```xml
<Button Content="Save"/>
<TextBlock Text="Save"/>
```
需要记住的是,Butoon跟TextBlock的文本显示的子属性是不同的(之前我老是给Button用Text="")
***

**Object 1 - 登录界面**
```xml
<Page
    x:Class="App1.MainPage"
    xmlns="http://schemas.microsoft.com/winfx/2006/xaml/presentation"
    xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml"
    xmlns:d="http://schemas.microsoft.com/expression/blend/2008"
    xmlns:mc="http://schemas.openxmlformats.org/markup-compatibility/2006"
    mc:Ignorable="d"
    Background="{ThemeResource ApplicationPageBackgroundThemeBrush}">


    <Grid Margin="10,0,0,0" Background="{ThemeResource AppBarBackgroundThemeBrush}">
        <Grid.RowDefinitions>
            <RowDefinition Height="Auto"/>
            <RowDefinition Height="Auto"/>
            <RowDefinition Height="Auto"/>
            <RowDefinition Height="Auto"/>
            <RowDefinition Height="Auto"/>
            <RowDefinition Height="Auto"/>
        </Grid.RowDefinitions>
        <Grid.ColumnDefinitions>
            <ColumnDefinition Width="Auto"/>
            <ColumnDefinition Width="Auto"/>
            <ColumnDefinition Width="Auto"/>
        </Grid.ColumnDefinitions>
        <TextBlock Grid.Row="1" Grid.Column="1" Grid.ColumnSpan="3" FontSize="48" Text="Welcom"/>
        <TextBox Grid.Row="2" Grid.Column="3" Width="200" Margin="0,10,10,0"/>
        <TextBlock Grid.Row="2" Grid.Column="1" Text="First Name:" Margin="0,10,0,0"/>
        <TextBox Grid.Row="3" Grid.Column="3" Width="200" Margin="0,10,10,0"/>
        <TextBlock Grid.Row="3" Grid.Column="1" Text="Last Name:" Margin="0,10,0,0"/>
        <TextBox Grid.Row="4" Grid.Column="3" Width="200" Margin="0,10,10,0"/>
        <TextBlock Grid.Row="4" Grid.Column="1" Text="Email:" Margin="0,10,0,0"/>
        <Button Grid.Row="5" Grid.Column="3" VerticalAlignment="Top" Margin="0,10,0,0" Content="Save"/>
    </Grid>
</Page>
```
我看完了教程11,然后上手做了,做完后看答案才发现我完全没有用Grid来做. 于是偷瞄了几眼答案,把这个作业做出来了(某种意义上也算完成吧.)

---


**Object 2 - "传说级"布局方案**
```xml
<Page
    x:Class="App1.MainPage"
    xmlns="http://schemas.microsoft.com/winfx/2006/xaml/presentation"
    xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml"
    xmlns:d="http://schemas.microsoft.com/expression/blend/2008"
    xmlns:mc="http://schemas.openxmlformats.org/markup-compatibility/2006"
    mc:Ignorable="d"
    Background="{ThemeResource ApplicationPageBackgroundThemeBrush}">

    
    <StackPanel HorizontalAlignment="Left" VerticalAlignment="Top" Orientation="Vertical" Margin="20,0,0,0" >
        <TextBlock Text="Bilibili" FontSize="48" Width="1257"/>
        <StackPanel Orientation="Horizontal">
            <TextBlock Text="文本内容" Height="Auto" TextWrapping="Wrap" Width="250" HorizontalAlignment="Left" FontSize="17"/>
            <StackPanel Orientation="Vertical">
                <TextBlock Text="文本内容" TextWrapping="Wrap" Height="Auto" Width="500" Margin="20,0,0,0"/>
            </StackPanel>
            <StackPanel Orientation="Horizontal">
                <Rectangle Fill="Blue" Width="160" Height="160" Margin="20,0,0,500" />
                <StackPanel Orientation="Vertical">
                    <Rectangle Fill="Red" Width="80" Height="80" Margin="0,0,0,0" />
                    <StackPanel Orientation="Horizontal">
                        <Rectangle Fill="Yellow" Width="80" Height="80" Margin="0,0,0,0" />
                    </StackPanel>
                </StackPanel>
            </StackPanel>
        </StackPanel>
    </StackPanel>
</Page>
```
我独立思考了许久,最后还是啃了点以前的教程,才做出来. 
在 `<StackPanel Orientation="Horizontal">` 下套一个 `<StackPanel Orientation="Vertical">` 就可以做出两个 StackPanel 横列相并的效果了.


### Learning Days 02 - 2022.01.26


**Objects 3 - 段落式**
```xml
<Grid Width="500" HorizontalAlignment="Left">
            <Grid.RowDefinitions>
                <RowDefinition Height="Auto"/>
                <RowDefinition Height="Auto"/>
                <RowDefinition Height="Auto"/>
            </Grid.RowDefinitions>
            <Grid.ColumnDefinitions>
                <ColumnDefinition Width="1*"/>
                <ColumnDefinition Width="2*"/>
            </Grid.ColumnDefinitions>
            <TextBlock FontSize="24">Title</TextBlock>
            <TextBlock Grid.Row="1" Grid.Column="1" FontSize="18" TextWrapping="Wrap">Text</TextBlock>
            <StackPanel Orientation="Horizontal" Grid.Row="2" Grid.Column="2">
                <Rectangle Fill="Black" Width="100" Height="30"/>
                <Rectangle Fill="Yellow" Width="100" Height="30"/>
                <Rectangle Fill="Blue" Width="100" Height="30"/>
            </StackPanel>
        </Grid>
```
一个模板. 觉得以后可能会有用就存下来了.

**Objects 4 - 复杂式布局**
```xml
<Page
    x:Class="App1.MainPage"
    xmlns="http://schemas.microsoft.com/winfx/2006/xaml/presentation"
    xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml"
    xmlns:d="http://schemas.microsoft.com/expression/blend/2008"
    xmlns:mc="http://schemas.openxmlformats.org/markup-compatibility/2006"
    mc:Ignorable="d"
    Background="{ThemeResource ApplicationPageBackgroundThemeBrush}">


    <ScrollViewer VerticalScrollBarVisibility="Auto">
        <StackPanel Margin="20">
            <Grid Width="500" HorizontalAlignment="Left">
                <Grid.RowDefinitions>
                    <RowDefinition Height="Auto"/>
                    <RowDefinition Height="Auto"/>
                    <RowDefinition Height="Auto"/>
                </Grid.RowDefinitions>
                <Grid.ColumnDefinitions>
                    <ColumnDefinition Width="1*"/>
                    <ColumnDefinition Width="2*"/>
                </Grid.ColumnDefinitions>
                <TextBlock FontSize="24">标题 1</TextBlock>
                <TextBlock Grid.Row="1" Grid.Column="1" FontSize="18" TextWrapping="Wrap">在网上时间久了就会发现一点，那就是光用结论来划分阵营其实非常粗糙，真正把人区分开的是得出结论的方法。</TextBlock>
                <StackPanel Orientation="Horizontal" Grid.Row="2" Grid.Column="2">
                    <Rectangle Fill="Black" Width="100" Height="30"/>
                    <Rectangle Fill="Yellow" Width="100" Height="30"/>
                    <Rectangle Fill="Blue" Width="100" Height="30"/>
                </StackPanel>
            </Grid>

            <Grid Width="500" HorizontalAlignment="Left">
                <Grid.RowDefinitions>
                    <RowDefinition Height="Auto"/>
                    <RowDefinition Height="Auto"/>
                    <RowDefinition Height="Auto"/>
                </Grid.RowDefinitions>
                <Grid.ColumnDefinitions>
                    <ColumnDefinition Width="1*"/>
                    <ColumnDefinition Width="2*"/>
                </Grid.ColumnDefinitions>
                <TextBlock FontSize="24">标题 2</TextBlock>
                <TextBlock Grid.Row="1" Grid.Column="1" FontSize="18" TextWrapping="Wrap">比如，现在有一款治疗消化系统疾病的药摆在面前，张三和李四都表示拒绝服药，乍看上去，他俩仿佛是一个立场的，但如果你让他们具体阐述一下自己的理由，就会发现他俩根本不是一路人。
· 张三说，他拒绝服药是因为药厂在这胶囊里藏了微型录音机，能留在他肚子里监听他平时说话的内容，以盗取他永动机的专利。
· 李四说，他拒绝服药是因为他运用了一套数学模型，从药物之前一系列临床试验和后续副作用追踪的数据来看，他现在这种程度的患者服药的收益期望实际为负。
如果只摆出结论和立场，张三和李四之间就会产生「咱都不吃药，咱是一伙人」的错觉。</TextBlock>
                <StackPanel Orientation="Horizontal" Grid.Row="2" Grid.Column="2">
                    <Rectangle Fill="Black" Width="100" Height="30"/>
                    <Rectangle Fill="Yellow" Width="100" Height="30"/>
                    <Rectangle Fill="Blue" Width="100" Height="30"/>
                </StackPanel>
            </Grid>

            <Grid Width="500" HorizontalAlignment="Left">
                <Grid.RowDefinitions>
                    <RowDefinition Height="Auto"/>
                    <RowDefinition Height="Auto"/>
                    <RowDefinition Height="Auto"/>
                </Grid.RowDefinitions>
                <Grid.ColumnDefinitions>
                    <ColumnDefinition Width="1*"/>
                    <ColumnDefinition Width="2*"/>
                </Grid.ColumnDefinitions>
                <TextBlock FontSize="24">标题 3</TextBlock>
                <TextBlock Grid.Row="1" Grid.Column="1" FontSize="18" TextWrapping="Wrap">这时候，王五又来了，他表示应该服药，光从立场上来看，这新来的和前两位结论相反，阵营对立。
但王五说，他运用了和李四同样的数学模型，只不过昨天刚看了最新一期的《新英格兰医学》，里边的一篇论文修正了早先的数据错误，再带入之前的数学模型后，服药的期望就为正了，所以应该服药。
王五和李四的结论虽然相反，但那只不过是信息交流不充分造成的暂时结果，从思维逻辑上来看，他俩其实才是真正的同路人。</TextBlock>
                <StackPanel Orientation="Horizontal" Grid.Row="2" Grid.Column="2">
                    <Rectangle Fill="Black" Width="100" Height="30"/>
                    <Rectangle Fill="Yellow" Width="100" Height="30"/>
                    <Rectangle Fill="Blue" Width="100" Height="30"/>
                </StackPanel>
            </Grid>

            <Grid Width="500" HorizontalAlignment="Left">
                <Grid.RowDefinitions>
                    <RowDefinition Height="Auto"/>
                    <RowDefinition Height="Auto"/>
                    <RowDefinition Height="Auto"/>
                </Grid.RowDefinitions>
                <Grid.ColumnDefinitions>
                    <ColumnDefinition Width="1*"/>
                    <ColumnDefinition Width="2*"/>
                </Grid.ColumnDefinitions>
                <TextBlock FontSize="24">标题 4</TextBlock>
                <TextBlock Grid.Row="1" Grid.Column="1" FontSize="18" TextWrapping="Wrap">所以，在网上，如果大家光说个结论摆个立场，而不充分展开论证，其实会无意中掩盖张三李四的分歧，并扩大李四王五的矛盾，因此，我还是建议大家多写作，遇到事，不仅要给出结论，也要给出论证过程，这样才能知道谁是站在身边的陌路人，谁又是站在对面的同志。</TextBlock>
                <StackPanel Orientation="Horizontal" Grid.Row="2" Grid.Column="2">
                    <Rectangle Fill="Black" Width="100" Height="30"/>
                    <Rectangle Fill="Yellow" Width="100" Height="30"/>
                    <Rectangle Fill="Blue" Width="100" Height="30"/>
                </StackPanel>
            </Grid>

            <Grid Width="500" HorizontalAlignment="Left">
                <Grid.RowDefinitions>
                    <RowDefinition Height="Auto"/>
                    <RowDefinition Height="Auto"/>
                    <RowDefinition Height="Auto"/>
                </Grid.RowDefinitions>
                <Grid.ColumnDefinitions>
                    <ColumnDefinition Width="1*"/>
                    <ColumnDefinition Width="2*"/>
                </Grid.ColumnDefinitions>
                <TextBlock FontSize="24">标题 5</TextBlock>
                <TextBlock Grid.Row="1" Grid.Column="1" FontSize="18" TextWrapping="Wrap">比如，李四王五在具体阐述自己的思路并互相探讨后就能达成共识，并且一起被张三骂了。</TextBlock>
                <StackPanel Orientation="Horizontal" Grid.Row="2" Grid.Column="2">
                    <Rectangle Fill="Black" Width="100" Height="30"/>
                    <Rectangle Fill="Yellow" Width="100" Height="30"/>
                    <Rectangle Fill="Blue" Width="100" Height="30"/>
                </StackPanel>
            </Grid>
        </StackPanel>
    </ScrollViewer>
</Page>

```
完全放弃(悲)
最终还是看答案才茅塞顿开(我先前都不知道Stackpanel还能 `Grid.Row` 或 `Grid.Column` ...) 
在完成这副作品后,我发现我的例文字数太多了,窗口装不下,于是便学习了一个新功能:滚动条
```xml
<ScrollViewer VerticalScrollBarVisibility="Auto">
    <!--在滚动条中的内容-->
</ScrollViewer>
```
这几天的高强度码字整得我眼睛非常疲劳,且伴着点轻微疼痛. 不过我现在已经觉得视力什么的无所谓了(我现在已经500多度了).
***

**Objects 5- 自制搜索栏**
```xml
<Page
    x:Class="App1.MainPage"
    xmlns="http://schemas.microsoft.com/winfx/2006/xaml/presentation"
    xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml"
    xmlns:d="http://schemas.microsoft.com/expression/blend/2008"
    xmlns:mc="http://schemas.openxmlformats.org/markup-compatibility/2006"
    mc:Ignorable="d"
    Background="{ThemeResource ApplicationPageBackgroundThemeBrush}">

    <Grid>
        <Grid.ColumnDefinitions>
            <ColumnDefinition Width="1*"/>
            <ColumnDefinition Width="2*"/>
            <ColumnDefinition Width="2*"/>
            <ColumnDefinition Width="Auto"/>
        </Grid.ColumnDefinitions>
        <TextBlock Text="Tittle" FontSize="35"/>
        <RelativePanel MinWidth="50" MinHeight="35" Grid.Column="3" >
            <Button Width="50" Height="50" RelativePanel.AlignRightWithPanel="True"/>
        </RelativePanel>
        <RelativePanel MinWidth="150" MinHeight="35" Grid.Column="2" >
            <TextBox Width="150" Height="35" RelativePanel.AlignRightWithPanel="True" Margin="0,0,20,0"/>
        </RelativePanel>
    </Grid>
</Page>
```
`<RelativePanel MinWidth="" MinHeight="">` 下,在元素中添加 `RelativePanel.AlignRightWithPanel="True"` 就可以将元素固定在左侧,可以伸缩,宽最小值是MinWidth,高最小值是MinHeight.


```xml
<Page
    x:Class="App1.MainPage"
    xmlns="http://schemas.microsoft.com/winfx/2006/xaml/presentation"
    xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml"
    xmlns:d="http://schemas.microsoft.com/expression/blend/2008"
    xmlns:mc="http://schemas.openxmlformats.org/markup-compatibility/2006"
    mc:Ignorable="d"
    Background="{ThemeResource ApplicationPageBackgroundThemeBrush}">

    <StackPanel>
        <SplitView Name="Split" OpenPaneLength="80">
            <SplitView.Pane>
                <StackPanel>
                    <TextBlock FontSize="25">hi</TextBlock>
                    <TextBlock FontSize="25">hi</TextBlock>
                    <TextBlock FontSize="25">hi</TextBlock>
                    <TextBlock FontSize="25">hi</TextBlock>
                </StackPanel>
            </SplitView.Pane>
            <SplitView.Content>
                <StackPanel>
                    <TextBlock FontSize="25">a</TextBlock>
                    <TextBlock FontSize="25">b</TextBlock>
                    <TextBlock FontSize="25">c</TextBlock>
                    <TextBlock FontSize="25">d</TextBlock>
                </StackPanel>
            </SplitView.Content>
        </SplitView>
        <Button Width="50" Height="50" Click="Button_Click" VerticalAlignment="Bottom"/>
    </StackPanel>
</Page>

```

### Learning Days 03 - 2022.01.27

**Objects 4.2 - 复杂式布局 + 侧边栏**
```xml
<Page
    x:Class="App1.MainPage"
    xmlns="http://schemas.microsoft.com/winfx/2006/xaml/presentation"
    xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml"
    xmlns:d="http://schemas.microsoft.com/expression/blend/2008"
    xmlns:mc="http://schemas.openxmlformats.org/markup-compatibility/2006"
    mc:Ignorable="d"
    Background="{ThemeResource ApplicationPageBackgroundThemeBrush}">

    <Grid VerticalAlignment="Top">
        <ScrollViewer VerticalScrollBarVisibility="Auto">
            <StackPanel >
                <SplitView Name="Split" DisplayMode="CompactOverlay" CompactPaneLength="102">
                    <SplitView.Pane>
                        <StackPanel>
                            <Button FontSize="25" Margin="8,30,0,0">章节一 重生之我是刘姥姥</Button>
                            <Button FontSize="25" Margin="8,20,0,0">章节二 我妈竟是博丽灵梦</Button>
                            <Button FontSize="25" Margin="8,20,0,0">章节三 刘姥姥七进七出</Button>
                            <Button FontSize="25" Margin="8,20,0,0">章节四 八辈渔民 大海血脉</Button>
                            <Button FontSize="25" Margin="8,20,0,0">章节五 微软大法好</Button>
                            <Button FontSize="25" Margin="8,20,0,0">章节六 完结</Button>
                        </StackPanel>
                    </SplitView.Pane>
                    <SplitView.Content>
                        <StackPanel Margin="20">
                            <Grid Width="500" HorizontalAlignment="Left" Margin="30,0,0,0">
                                <Grid.RowDefinitions>
                                    <RowDefinition Height="Auto"/>
                                    <RowDefinition Height="Auto"/>
                                    <RowDefinition Height="Auto"/>
                                </Grid.RowDefinitions>
                                <Grid.ColumnDefinitions>
                                    <ColumnDefinition Width="1*"/>
                                    <ColumnDefinition Width="2*"/>
                                </Grid.ColumnDefinitions>
                                <TextBlock FontSize="24">标题 1</TextBlock>
                                <TextBlock Grid.Row="1" Grid.Column="1" FontSize="18" TextWrapping="Wrap">在网上时间久了就会发现一点，那就是光用结论来划分阵营其实非常粗糙，真正把人区分开的是得出结论的方法。</TextBlock>
                                <StackPanel Orientation="Horizontal" Grid.Row="2" Grid.Column="2">
                                    <Rectangle Fill="Black" Width="100" Height="30"/>
                                    <Rectangle Fill="Yellow" Width="100" Height="30"/>
                                    <Rectangle Fill="Blue" Width="100" Height="30"/>
                                </StackPanel>
                            </Grid>

                            <Grid Width="500" HorizontalAlignment="Left" Margin="30,0,0,0">
                                <Grid.RowDefinitions>
                                    <RowDefinition Height="Auto"/>
                                    <RowDefinition Height="Auto"/>
                                    <RowDefinition Height="Auto"/>
                                </Grid.RowDefinitions>
                                <Grid.ColumnDefinitions>
                                    <ColumnDefinition Width="1*"/>
                                    <ColumnDefinition Width="2*"/>
                                </Grid.ColumnDefinitions>
                                <TextBlock FontSize="24">标题 2</TextBlock>
                                <TextBlock Grid.Row="1" Grid.Column="1" FontSize="18" TextWrapping="Wrap">比如，现在有一款治疗消化系统疾病的药摆在面前，张三和李四都表示拒绝服药，乍看上去，他俩仿佛是一个立场的，但如果你让他们具体阐述一下自己的理由，就会发现他俩根本不是一路人。
· 张三说，他拒绝服药是因为药厂在这胶囊里藏了微型录音机，能留在他肚子里监听他平时说话的内容，以盗取他永动机的专利。
· 李四说，他拒绝服药是因为他运用了一套数学模型，从药物之前一系列临床试验和后续副作用追踪的数据来看，他现在这种程度的患者服药的收益期望实际为负。
如果只摆出结论和立场，张三和李四之间就会产生「咱都不吃药，咱是一伙人」的错觉。</TextBlock>
                                <StackPanel Orientation="Horizontal" Grid.Row="2" Grid.Column="2">
                                    <Rectangle Fill="Black" Width="100" Height="30"/>
                                    <Rectangle Fill="Yellow" Width="100" Height="30"/>
                                    <Rectangle Fill="Blue" Width="100" Height="30"/>
                                </StackPanel>
                            </Grid>

                            <Grid Width="500" HorizontalAlignment="Left " Margin="30,0,0,0">
                                <Grid.RowDefinitions>
                                    <RowDefinition Height="Auto"/>
                                    <RowDefinition Height="Auto"/>
                                    <RowDefinition Height="Auto"/>
                                </Grid.RowDefinitions>
                                <Grid.ColumnDefinitions>
                                    <ColumnDefinition Width="1*"/>
                                    <ColumnDefinition Width="2*"/>
                                </Grid.ColumnDefinitions>
                                <TextBlock FontSize="24">标题 3</TextBlock>
                                <TextBlock Grid.Row="1" Grid.Column="1" FontSize="18" TextWrapping="Wrap">这时候，王五又来了，他表示应该服药，光从立场上来看，这新来的和前两位结论相反，阵营对立。
但王五说，他运用了和李四同样的数学模型，只不过昨天刚看了最新一期的《新英格兰医学》，里边的一篇论文修正了早先的数据错误，再带入之前的数学模型后，服药的期望就为正了，所以应该服药。
王五和李四的结论虽然相反，但那只不过是信息交流不充分造成的暂时结果，从思维逻辑上来看，他俩其实才是真正的同路人。</TextBlock>
                                <StackPanel Orientation="Horizontal" Grid.Row="2" Grid.Column="2">
                                    <Rectangle Fill="Black" Width="100" Height="30"/>
                                    <Rectangle Fill="Yellow" Width="100" Height="30"/>
                                    <Rectangle Fill="Blue" Width="100" Height="30"/>
                                </StackPanel>
                            </Grid>

                            <Grid Width="500" HorizontalAlignment="Left" Margin="30,0,0,0">
                                <Grid.RowDefinitions>
                                    <RowDefinition Height="Auto"/>
                                    <RowDefinition Height="Auto"/>
                                    <RowDefinition Height="Auto"/>
                                </Grid.RowDefinitions>
                                <Grid.ColumnDefinitions>
                                    <ColumnDefinition Width="1*"/>
                                    <ColumnDefinition Width="2*"/>
                                </Grid.ColumnDefinitions>
                                <TextBlock FontSize="24">标题 4</TextBlock>
                                <TextBlock Grid.Row="1" Grid.Column="1" FontSize="18" TextWrapping="Wrap">所以，在网上，如果大家光说个结论摆个立场，而不充分展开论证，其实会无意中掩盖张三李四的分歧，并扩大李四王五的矛盾，因此，我还是建议大家多写作，遇到事，不仅要给出结论，也要给出论证过程，这样才能知道谁是站在身边的陌路人，谁又是站在对面的同志。</TextBlock>
                                <StackPanel Orientation="Horizontal" Grid.Row="2" Grid.Column="2">
                                    <Rectangle Fill="Black" Width="100" Height="30"/>
                                    <Rectangle Fill="Yellow" Width="100" Height="30"/>
                                    <Rectangle Fill="Blue" Width="100" Height="30"/>
                                </StackPanel>
                            </Grid>

                            <Grid Width="500" HorizontalAlignment="Left" Margin="30,0,0,0">
                                <Grid.RowDefinitions>
                                    <RowDefinition Height="Auto"/>
                                    <RowDefinition Height="Auto"/>
                                    <RowDefinition Height="Auto"/>
                                </Grid.RowDefinitions>
                                <Grid.ColumnDefinitions>
                                    <ColumnDefinition Width="1*"/>
                                    <ColumnDefinition Width="2*"/>
                                </Grid.ColumnDefinitions>
                                <TextBlock FontSize="24">标题 5</TextBlock>
                                <TextBlock Grid.Row="1" Grid.Column="1" FontSize="18" TextWrapping="Wrap">比如，李四王五在具体阐述自己的思路并互相探讨后就能达成共识，并且一起被张三骂了。</TextBlock>
                                <StackPanel Orientation="Horizontal" Grid.Row="2" Grid.Column="2">
                                    <Rectangle Fill="Black" Width="100" Height="30"/>
                                    <Rectangle Fill="Yellow" Width="100" Height="30"/>
                                    <Rectangle Fill="Blue" Width="100" Height="30"/>
                                </StackPanel>
                            </Grid>
                        </StackPanel>
                    </SplitView.Content>
                </SplitView>
            </StackPanel>
        </ScrollViewer>
        <Button Height="50" Width="50" Click="Button_Click_1" VerticalAlignment="Bottom"/>
    </Grid>
</Page>
```
```xml
<SplitView><!--Name="" DisplayMode="" CompactPaneLength="" OpenPanelLength""-->
    
    <SplitView.Pane>
        <StackPanel>
            <!--侧边栏里的内容-->
        </StackPanel>
    </SplitView.Pane>

    <SplitView.Content>
        <!--侧边栏外的内容-->
    </SplitView.Content>
</SplitView>            
```
画面效果我非常满意,有点uwp应用的模样了,可惜的是我不知道怎么把侧边栏固定. 以后再回头做.
还有一个不足的是,打开侧边栏时,它总是从左侧弹出,但Crosst的侧边栏是在右边的,费了许些心思,最后放弃了,今晚再查资料. *2022.01.28后记:那天晚上没查,而是娱乐去了,适之啊适之.*


### Learning Days 04 - 2022.01.28

xaml `<Frame Name=""></Frame>`
C# `MainFrame.Navigate(typeof(PageName));`
可以实现页面间的跳转,我一般配合Grid用.

### Learning Days 05 - 2022.01.30
**巨大阻碍Websocket**
许久未见，我也在好奇 Day5 去哪了。

实不相瞒，我在“用 Websocket 连上服务器”这步卡了整整一天！Day5 里，我像只兔子挖洞般翻阅网络资料，终以五花八门的报错收尾，继续挖洞。因此我没有写下任何实际代码。

转念一想，其实我应该先给自己定个小计划，Day 几什么，Day 几又什么，不然我倒像个无头苍蝇乱勾八飞。

中午的时间到了我就加一个新分区——“时间线”。

“先试试拿 WebSocket 连接到服务器吧”
“再看看 JSON”

——Henrize 的原话。这两句长短句像两栋大坝，而我一直邯郸学步地，毫无耐心地想要跨过去、一步登天。



## 碎语
### Hello World!
这是这里的第一篇文章。

之前新学的一个词，博客，就是这个。我身边很多人都在搭。我想搭，但不会，纵使搭好了，也可能半途而废。

那就先省去博客这一环，暂先存在本地，平时有时没事自己翻阅，也就足了，倘以后有需求，我再搭便是。

至于为什么要写这些东西，一来是我以前写日记的想法投映到这里了；二来是想多多保存这稀贵的寒假，保存嘛，总要记录点什么，便又投映到这里了。希望我能多多记录，一定一定不要弃坑。

我弃过的坑想必是我两只小手数不过来的：灵光一闪，到完全放弃，竟然是如此简单！这简单催使我的脑瓜子愈想愈多，弃的也就愈多。这里不妨再提醒自己一次：一定一定不要弃坑！

回过神来……离上学还有两周时间，一想到寒假作业，我头便发昏，我总该抽点时间来处理处理他们了。

2022.01.27 - 20222.01.28




## 碎碎念

1. 成功登上Crosst *理所应当的第一步*
2. 自动本地保存聊天记录
3. 可选主题
4. 分割Username&Password
5. UsersList
6. 黑名单
