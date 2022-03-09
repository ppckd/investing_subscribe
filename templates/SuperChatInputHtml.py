

def superChatInputHtml():
    htmlcode = """
   <html>
   <h1> 슈퍼챗 입력 </h1>
      <body>
         <form method = "POST">
            <p>roomNo <input type = "text" name = "roomNo" /></p>
            <p>userID <input type = "text" name = "userID" /></p>
            <p>stockName <input type = "text" name = "stockName" /></p>
            <p>stockCode <input type ="text" name = "stockCode" /></p>
            <p>currentPrice <input type ="text" name = "currentPrice" /></p>
            <p>predictPrice <input type ="text" name = "predictPrice" /></p>
            <p>stopLossPrice <input type ="text" name = "stopLossPrice" /></p>
            <p>today(0000-00-00) <input type ="text" name = "today" /></p>
            <p>predictDate <input type ="text" name = "predictDate" /></p>
            <p>contents <input type ="text" name = "contents" /></p>
            <p><input type = "submit" value = "submit" /></p>
         </form>

      </body>
   </html>"""
    return htmlcode