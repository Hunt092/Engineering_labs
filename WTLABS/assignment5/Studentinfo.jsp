<%@ page import="java.sql.*"%>
<%
String ID=request.getParameter("ID");
String Name=request.getParameter("Name");
String Division=request.getParameter("Division");
String City=request.getParameter("City");
try{
Class.forName("com.mysql.cj.jdbc.Driver");
Connection 
con=DriverManager.getConnection("jdbc:mysql://localhost:3306/mbtb", "root", 
"SejalFeb@521");
Statement st=con.createStatement();
st.executeUpdate("insert into students_info(ID,Name,Division,City) values 
('"+ID+"','"+Name+"','"+Division+"','"+City+"')");
response.sendRedirect("success.html");
}
catch(Exception e){
response.sendRedirect("tryagain.html");
}
%>