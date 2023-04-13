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
#include <arpa/inet.h>
void main()
{
	int b,sockfd,connfd,sin_size,l,n,len;
	char operator;
	char op1[50],op2[50],result[50];
	if((sockfd=socket(AF_INET,SOCK_STREAM,0))>0)
		printf("socket created sucessfully\n");               
	struct sockaddr_in servaddr;              
	struct sockaddr_in clientaddr;

	servaddr.sin_family=AF_INET;
	servaddr.sin_addr.s_addr=inet_addr("192.168.43.76");
	servaddr.sin_port=6006;

	if((bind(sockfd, (struct sockaddr *)&servaddr,sizeof(servaddr)))==0)
	printf("bind sucessful\n");  

	if((listen(sockfd,5))==0) 
	printf("listen successful\n");
	sin_size = sizeof(struct sockaddr_in);
	if((connfd=accept(sockfd,(struct sockaddr *)&clientaddr,&sin_size))>0);
		printf("accept successful\n");
	read(connfd,op1,sizeof(op1));
	printf("%s",op1);
	//result=op1*op1;
	printf(" Enter the Msg\n");
	scanf("%s",&result); 
	write(connfd,result,sizeof(result));   
	close(sockfd);
}
