<%@ page import="java.sql.*"%>
<%
String ID=request.getParameter("ID");
String Title=request.getParameter("Title");
String Author=request.getParameter("Author");
String Price=request.getParameter("Price");
String Quantity=request.getParameter("Quanitiy");
try{
Class.forName("com.mysql.cj.jdbc.Driver");
Connection 
con=DriverManager.getConnection("jdbc:mysql://localhost:3306/mbtb", "root", 
"SejalFeb@521");
Statement st=con.createStatement();
st.executeUpdate("insert into ebookshop(ID,Title,Author,Price,Quantity) 
values ('"+ID+"','"+Title+"','"+Author+"','"+Price+"','"+Quantity+"')");
response.sendRedirect("success.html");
}
catch(Exception e){
response.sendRedirect("tryagain.html");
}
%>