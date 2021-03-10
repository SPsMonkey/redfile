from tkinter import *
from time import time, localtime, strftime
itemname={
"份号":"份号",
"保密等级":"保密等级",
"保密期限":"保密期限",
"紧急程度":"紧急程度",
"发文机关":"发文机关",
"机关代字":"机关代字",
"年份":"年份",
"发文号":"发文号",
"签发人":"签发人",
"标题":"标题",
"文件内容":"文件内容",
"成文日期":"成文日期",
"印发日期":"印发日期",
"抄送机关":"抄送机关",
"印发机关":"印发机关",
"附件":"附件",
"红头纸":"是否使用红头纸打印",
"高度调整":"高度调整",
"签发人调整":"签发人调整"
}
hintmsg={
"份号":"公文印制份数的顺序号，涉密公文应当标注份号，一般为6位阿拉伯数字。\n例如：123456",
"保密等级":"涉密公文应当根据涉密程度分别标注“绝密”“机密”“秘密”。",
"保密期限":"涉密公文应当根据情况标注保密期限。例如：1年",
"紧急程度":"公文送达和办理的时限要求。根据紧急程度，紧急公文应当分别标注“特急”“加急”，电报应当分别标注“特提”“特急”“加急”“平急”。",
"发文机关":"发文机关全称",
"机关代字":"填写发文机关代字",
"年份":"填写发文年份。例如：2020",
"发文号":"填写发文顺序号。例如：20",
"签发人":"填写签发人姓名，多个人请用空格隔开。例如：李某某 张某某",
"标题":"填写文件标题，由发文机关名称、事由和文种组成。",
"文件内容":"文件内容",
"成文日期":"署会议通过或者发文机关负责人签发的日期。联合行文时，署最后签发机关负责人签发的日期。例如：2020年1月1日",
"印发日期":"公文的送印日期。例如：2020年1月1日。如不填写则默认与成文日期一致。",
"抄送机关":"除主送机关外需要执行或者知晓公文内容的其他机关，应当使用机关全称、规范化简称或者同类型机关统称。名称之间用顿号隔开。",
"印发机关":"公文的送印机关名称。如不填写则默认与发文机关一致",
"附件":"依次公文附件名称",
"高度调整":"这个参数决定发文字号的高低，必须是正数，数值越大，位置越低，单位为毫米，设置合适的数值使其刚好位于红头文件纸的红线之上。例如：30。",
"签发人调整":"这个参数决定签发人左右位置，必须是正整数，数值越大，位置越靠右，单位为字符，设置合适的数值使其刚好位于签发人右侧。数值范围为0-26例如：20。"
}
 
class ToolTip( Toplevel ):
  """
  Provides a ToolTip widget for Tkinter.
  To apply a ToolTip to any Tkinter widget, simply pass the widget to the
  ToolTip constructor
  """ 
  def __init__( self, wdgt, msg=None, msgFunc=None, delay=1, follow=True ):
    """
    Initialize the ToolTip
     
    Arguments:
     wdgt: The widget this ToolTip is assigned to
     msg: A static string message assigned to the ToolTip
     msgFunc: A function that retrieves a string to use as the ToolTip text
     delay:  The delay in seconds before the ToolTip appears(may be float)
     follow: If True, the ToolTip follows motion, otherwise hides
    """
    self.wdgt = wdgt
    self.parent = self.wdgt.master                     # The parent of the ToolTip is the parent of the ToolTips widget
    Toplevel.__init__( self, self.parent, bg='black', padx=1, pady=1 )   # Initalise the Toplevel
    self.withdraw()                             # Hide initially
    self.overrideredirect( True )                      # The ToolTip Toplevel should have no frame or title bar
     
    self.msgVar = StringVar()                        # The msgVar will contain the text displayed by the ToolTip    
    if msg == None:                             
      self.msgVar.set( 'No message provided' )
    else:
      self.msgVar.set( msg )
    self.msgFunc = msgFunc
    self.delay = delay
    self.follow = follow
    self.visible = 0
    self.lastMotion = 0
    Message( self, textvariable=self.msgVar, bg='#FFFFDD',
         aspect=1000 ).grid()                      # The test of the ToolTip is displayed in a Message widget
    self.wdgt.bind( '<Enter>', self.spawn, '+' )              # Add bindings to the widget. This will NOT override bindings that the widget already has
    self.wdgt.bind( '<Leave>', self.hide, '+' )
    self.wdgt.bind( '<Motion>', self.move, '+' )
     
  def spawn( self, event=None ):
    """
    Spawn the ToolTip. This simply makes the ToolTip eligible for display.
    Usually this is caused by entering the widget
     
    Arguments:
     event: The event that called this funciton
    """
    self.visible = 1
    self.after( int( self.delay * 1000 ), self.show )            # The after function takes a time argument in miliseconds
     
  def show( self ):
    """
    Displays the ToolTip if the time delay has been long enough
    """
    if self.visible == 1 and time() - self.lastMotion > self.delay:
      self.visible = 2
    if self.visible == 2:
      self.deiconify()
       
  def move( self, event ):
    """
    Processes motion within the widget.
     
    Arguments:
     event: The event that called this function
    """
    self.lastMotion = time()
    if self.follow == False:                        # If the follow flag is not set, motion within the widget will make the ToolTip dissapear
      self.withdraw()
      self.visible = 1
    self.geometry( '+%i+%i' % ( event.x_root+10, event.y_root+10 ) )    # Offset the ToolTip 10x10 pixes southwest of the pointer
    try:
      self.msgVar.set( self.msgFunc() )                  # Try to call the message function. Will not change the message if the message function is None or the message function fails
    except:
      pass
    self.after( int( self.delay * 1000 ), self.show )
       
  def hide( self, event=None ):
    """
    Hides the ToolTip. Usually this is caused by leaving the widget
     
    Arguments:
     event: The event that called this function
    """
    self.visible = 0
    self.withdraw()
 
 
def xrange2d( n,m ):
  """
  Returns a generator of values in a 2d range
   
  Arguments:
   n: The number of rows in the 2d range
   m: The number of columns in the 2d range
  Returns:
   A generator of values in a 2d range
  """
  return ( (i,j) for i in xrange(n) for j in xrange(m) )
 
 
def range2d( n,m ):
  """
  Returns a list of values in a 2d range
   
  Arguments:
   n: The number of rows in the 2d range
   m: The number of columns in the 2d range
  Returns:
   A list of values in a 2d range
  """
  return [(i,j) for i in range(n) for j in range(m) ]
 
 
def print_time():
  """
  Prints the current time in the following format:
  HH:MM:SS.00
  """
  t = time()
  timeString = 'time='
  timeString += strftime( '%H:%M:', localtime(t) )
  timeString += '%.2f' % ( t%60, )
  return timeString
   
def main():
  root = Tk()
  btnList = []
  for (i,j) in range2d( 6, 4 ):
    text = 'delay=%i\n' % i
    delay = i
    if j >= 2:
      follow=True
      text += '+follow\n'
    else:
      follow = False
      text += '-follow\n'
    if j % 2 == 0:
      msg = None
      msgFunc = print_time
      text += 'Message Function'
    else:
      msg = 'Button at %s' % str( (i,j) )
      msgFunc = None
      text += 'Static Message'
    btnList.append( Button( root, text=text ) )
    ToolTip( btnList[-1], msg=msg, msgFunc=msgFunc, follow=follow, delay=delay)
    btnList[-1].grid( row=i, column=j, sticky=N+S+E+W )
  root.mainloop()
   
if __name__ == '__main__':
  main()