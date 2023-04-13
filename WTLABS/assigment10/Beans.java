package ejb; 
import javax.ejb.Stateless; 
@Stateless 
public class EJBBean implements EJBBeanRemote{ 
 @Override 
 public Integer addData(int a, int b){ 
 return a+b; 
 } 
} 
