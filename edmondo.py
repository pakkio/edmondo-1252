# coding=UTF-8
import webapp2
# modify
from google.appengine.ext import db

class Scores(db.Model):
  session = db.StringProperty(multiline=False) 
  name = db.StringProperty(multiline=False)
  score = db.IntegerProperty()

def header():
    return """
    <html xmlns="http://www.w3.org/1999/xhtml">
<head>
<style type="text/css">

/*
This was made by João Sardinha
Visit me at http://johnsardine.com/

The table style doesnt contain images, it contains gradients for browsers who support them as well as round corners and drop shadows.

It has been tested in all major browsers.

This table style is based on Simple Little Table By Orman Clark,
you can download a PSD version of this at his website, PremiumPixels.
http://www.premiumpixels.com/simple-little-table-psd/

PLEASE CONTINUE READING AS THIS CONTAINS IMPORTANT NOTES

*/

/*
Im reseting this style for optimal view using Eric Meyer's CSS Reset - http://meyerweb.com/eric/tools/css/reset/
------------------------------------------------------------------ */
body, html  { height: 100%; }
html, body, div, span, applet, object, iframe,
/*h1, h2, h3, h4, h5, h6,*/ p, blockquote, pre,
a, abbr, acronym, address, big, cite, code,
del, dfn, em, font, img, ins, kbd, q, s, samp,
small, strike, strong, sub, sup, tt, var,
b, u, i, center,
dl, dt, dd, ol, ul, li,
fieldset, form, label, legend,
table, caption, tbody, tfoot, thead, tr, th, td {
    margin: 0;
padding: 0;
border: 0;
outline: 0;
font-size: 100%;
vertical-align: baseline;
background: transparent;
}
body { line-height: 1; }
ol, ul { list-style: none; }
blockquote, q { quotes: none; }
blockquote:before, blockquote:after, q:before, q:after { content: ''; content: none; }
:focus { outline: 0; }
del { text-decoration: line-through; }
table {border-spacing: 0; } /* IMPORTANT, I REMOVED border-collapse: collapse; FROM THIS LINE IN ORDER TO MAKE THE OUTER BORDER RADIUS WORK */

/*------------------------------------------------------------------ */

/*This is not important*/
body{
        font-family:Arial, Helvetica, sans-serif;
background: url(background.jpg);
margin:0 auto;
width:520px;
}
a:link {
    color: #666;
        font-weight: bold;
text-decoration:none;
}
a:visited {
    color: #666;
        font-weight:bold;
text-decoration:none;
}
a:active,
a:hover {
    color: #bd5a35;
        text-decoration:underline;
}


/*
Table Style - This is what you want
------------------------------------------------------------------ */
table a:link {
    color: #666;
        font-weight: bold;
text-decoration:none;
}
table a:visited {
    color: #999999;
        font-weight:bold;
text-decoration:none;
}
table a:active,
table a:hover {
    color: #bd5a35;
        text-decoration:underline;
}
table {
          font-family:Arial, Helvetica, sans-serif;
color:#666;
font-size:12px;
text-shadow: 1px 1px 0px #fff;
background:#eaebec;
margin:20px;
border:#ccc 1px solid;

-moz-border-radius:3px;
-webkit-border-radius:3px;
border-radius:3px;

-moz-box-shadow: 0 1px 2px #d1d1d1;
                        -webkit-box-shadow: 0 1px 2px #d1d1d1;
box-shadow: 0 1px 2px #d1d1d1;
}
table th {
    padding:21px 25px 22px 25px;
border-top:1px solid #fafafa;
border-bottom:1px solid #e0e0e0;

background: #ededed;
background: -webkit-gradient(linear, left top, left bottom, from(#ededed), to(#ebebeb));
    background: -moz-linear-gradient(top,  #ededed,  #ebebeb);
}
table th:first-child{
    text-align: left;
padding-left:20px;
}
table tr:first-child th:first-child{
    -moz-border-radius-topleft:3px;
-webkit-border-top-left-radius:3px;
border-top-left-radius:3px;
}
table tr:first-child th:last-child{
    -moz-border-radius-topright:3px;
-webkit-border-top-right-radius:3px;
border-top-right-radius:3px;
}
table tr{
    text-align: center;
padding-left:20px;
}
table tr td:first-child{
    text-align: left;
padding-left:20px;
border-left: 0;
}
table tr td {
    padding:18px;
border-top: 1px solid #ffffff;
border-bottom:1px solid #e0e0e0;
border-left: 1px solid #e0e0e0;

background: #fafafa;
background: -webkit-gradient(linear, left top, left bottom, from(#fbfbfb), to(#fafafa));
    background: -moz-linear-gradient(top,  #fbfbfb,  #fafafa);
}
table tr.even td{
    background: #f6f6f6;
        background: -webkit-gradient(linear, left top, left bottom, from(#f8f8f8), to(#f6f6f6));
    background: -moz-linear-gradient(top,  #f8f8f8,  #f6f6f6);
}
table tr:last-child td{
    border-bottom:0;
}
table tr:last-child td:first-child{
    -moz-border-radius-bottomleft:3px;
-webkit-border-bottom-left-radius:3px;
border-bottom-left-radius:3px;
}
table tr:last-child td:last-child{
    -moz-border-radius-bottomright:3px;
-webkit-border-bottom-right-radius:3px;
border-bottom-right-radius:3px;
}
table tr:hover td{
    background: #f2f2f2;
        background: -webkit-gradient(linear, left top, left bottom, from(#f2f2f2), to(#f0f0f0));
    background: -moz-linear-gradient(top,  #f2f2f2,  #f0f0f0);
}

</style></head><body>"""

class MainPage(webapp2.RequestHandler):
  def get(self):

    session=self.request.get('session') #the session
    name=self.request.get('name') # name
    scoreString=self.request.get('score')
    if(len(scoreString)>0):
        score=long(self.request.get('score')) # score
    else:
        score=0
 
    if self.request.get('type')=='add':  # Adding a new score
          q = db.GqlQuery("SELECT * FROM Scores WHERE session = :k1 AND name = :k2",k1=session, k2=name)
          count=q.count(2)
 
          if count==0 :  # the service doesn't exist, so add it.
              if session=="" or name=="" :
                  self.response.out.write('must provide session, name')
              else:
                  newrec=Scores(session=session,name=name,score=score)
                  newrec.put()
                  self.response.out.write('Added new score for ' + name)
          else:
              rec=q.get()
              rec.score = rec.score + score
              rec.put()
              self.response.out.write('Updated '+name+" now is "+str(rec.score))
    elif self.request.get('type')=='list':
        q = db.GqlQuery("SELECT * FROM Scores WHERE session = :k1 ORDER BY score DESC",k1=session)
        count = q.count(2)
        #self.response.out.write("Found "+str(count)+" results ")
        if count==0 :
            self.response.out.write('Empty')
        else:
            results = q.fetch(1000)
            for result in results:
                self.response.out.write(result.name+','+str(result.score)+"\n")
            self.response.out.write('END')  # Cap the list
    elif self.request.get('type')=='show':
        q = db.GqlQuery("SELECT * FROM Scores WHERE session = :k1 ORDER BY score DESC",k1=session)
        count = q.count(2)
        #self.response.out.write("Found "+str(count)+" results ")
        if count==0 :
            self.response.out.write('<h1>Empty</h1>')
        else:
            self.response.out.write(header())
            self.response.out.write("<table cellspacing=0>")
            results = q.fetch(1000)
            for result in results:
                self.response.out.write("<tr><td>"+
                                        result.name+
                                        '</td><td>'+
                                        str(result.score)+
                                        "</td></tr>")
            self.response.out.write('</table>')  # Cap the list


    elif self.request.get('type')=='clear':
          q = db.GqlQuery("SELECT * FROM Scores WHERE session = :kk",kk=session)
          count=q.count(2)
 
          if count==0 :
            self.response.out.write('None')
          else:
            results=q.fetch(100)
            db.delete(results)  
            self.response.out.write('Removed '+str(count))
         


app = webapp2.WSGIApplication([
	('/', MainPage),
	],
debug=True)
