<%@page import="java.sql.DriverManager"%>
<%@page import="java.sql.ResultSet"%>
<%@page import="java.sql.Statement"%>
<%@page import="java.sql.Connection"%>
<%
String id = request.getParameter("ID");
String driver = "com.mysql.jdbc.Driver";
String connectionUrl = "jdbc:mysql://localhost:3306/";
String database = "mbtb";
String userid = "root";
String password = "SejalFeb@521";
try {
Class.forName(driver);
} catch (ClassNotFoundException e) {
e.printStackTrace();
}
Connection connection = null;
Statement statement = null;
ResultSet resultSet = null;
%>
<!DOCTYPE html>
<html>
<body>
<h1>EBookShop Data</h1>
<table border="1">
<tr>
<td>ID</td>
<td>Title</td>
<td>Author</td>
<td>Price</td>
<td>Quantity</td>
</tr>
<%
try{
connection = DriverManager.getConnection(connectionUrl+database, userid, 
password);
statement=connection.createStatement();
String sql ="select * from ebookshop";
resultSet = statement.executeQuery(sql);
while(resultSet.next()){
%>
<tr>
<td><%=resultSet.getString("ID") %></td>
<td><%=resultSet.getString("Title") %></td>
<td><%=resultSet.getString("Author") %></td>
<td><%=resultSet.getString("Price") %></td>
<td><%=resultSet.getString("Quantity") %></td>
</tr>
<%
}
connection.close();
} catch (Exception e) {
e.printStackTrace();
}
%>
</table>
</body>
</html>
