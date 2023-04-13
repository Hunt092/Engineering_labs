import java.io.IOExecption; 
import java.io.PrintWriter; 
import javax.servlet.ServletException; 
import javax.servlet.http.HttpServlet; 
import javax.servlet.http.HttpServletRequest; 
import javax.servlet.http.HttpServletResponse; 
public class EJBServlet extends HttpServlet{ 
 protected void processRequest(HttpServletRequest request, 
HttpServletResponse response) 
 throws ServletException, IOExecption{ 
 response.setContentType("text/html;charset=UTF-8"); 
 try (PrintWriter out = response.getWriter()){ 
 int a = Integer.parsInt(request.getParameter("n1")); 
 int b = Integer.parsInt(request.getParameter("n2")); 
 
 out.println(eJBBean.addData(a,b)); 
 } 
 } 
}