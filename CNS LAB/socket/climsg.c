#include<sys/types.h>
#ifdef __WIN32__
# include <winsock2.h>
#else
# include <sys/socket.h>
#endif
#include<stdio.h>
#include<netinet/in.h> 
#include <unistd.h>
#include<string.h> 
#include<strings.h>
#include <arpa/inet.h>

void main()
{
	int b,sockfd,sin_size,con,n,len;
	char operator;
	int op1,op2;
	char msg[50],result[50];
	if((sockfd=socket(AF_INET,SOCK_STREAM,0))>0)
	printf("socket created sucessfully\n");
	struct sockaddr_in servaddr;
	servaddr.sin_family=AF_INET;
	servaddr.sin_addr.s_addr=inet_addr("192.168.43.76");
	servaddr.sin_port=6006;
	sin_size = sizeof(struct sockaddr_in);
	if((con=connect(sockfd,(struct sockaddr *) &servaddr, sin_size))==0); 
	printf("connection successful\n");
	printf("Enter the msg:\n");
	scanf("%s", &msg);
	write(sockfd,msg,sizeof(msg));
	read(sockfd,result,sizeof(result)); 
	printf("Message from server=%s\n",result);  
	close(sockfd);
}
