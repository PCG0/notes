// #include <bits/stdc++.h>
// #include <Windows.h>
// #include <wininet.h>
// using namespace std;

// #pragma comment(lib,"wininet.lib")
// #define BUF_SIZE 1024

// LPSTR GetInterNetURLText(LPSTR lpcInterNetURL,char* buff)
// {
//     HINTERNET hSession;
//     LPSTR lpResult = NULL;
//     hSession = InternetOpen("WinInet",INTERNET_OPEN_TYPE_PRECONFIG,NULL,NULL,0);
//     __try
//     {
//         if(hSession != NULL)
//         {
//             HINTERNET hRequest;
//             hRequest = InternetOpenUrlA(hSession,lpcInterNetURL,NULL,0,INTERNET_FLAG_RELOAD,0);
//             __try
//             {
//                 if(hRequest != NULL)
//                 {
//                     DWORD dwBytesRead;
//                     char szBuffer[BUF_SIZE] = {0};

//                     if(InternetReadFile(hRequest,szBuffer,BUF_SIZE,&dwBytesRead))
//                     {
//                         RtlMoveMemory(buff,szBuffer,BUF_SIZE);
//                         return 0;
//                     }
//                 }
//             }__finally
//             {
//                 InternetCloseHandle(hRequest);
//             }
//         }
//     }__finally
//     {
//         InternetCloseHandle(hSession);
//     }
//     return lpResult;
// }

// int _tmain()
// {
//     char buf[BUF_SIZE] = {0};
//     char url[MAX_PATH] = "https://firebook.store/book/chapter/1808";
//     GetInterNetURLText(url,buf);
//     return 0;
// }

// // LPSTR GetInterNetURLText(LPSTR lpcInterNetURL,char* buff)

// readTxt.cpp :Defines the entry point for the console application.
//
 
// #include "stdafx.h"
// #include <Windows.h>
// #include <wininet.h>
// #include <string>
// using namespace std;
// #pragma comment(lib, "wininet.lib")
// #define BUF_SIZE 1024
 
// LPSTR GetInterNetURLText(LPSTR lpcInterNetURL, char* buff);
 
// int _tmain(int argc, _TCHAR* argv[])
// {
//     char buf[BUF_SIZE] = {0};
//     char url[MAX_PATH] = "http://www.baidu.com/xxx.txt";
//     GetInterNetURLText(url, buf);
 
//     return 0;
// }
 
// LPSTR GetInterNetURLText(LPSTR lpcInterNetURL, char* buff)
// {   
//     HINTERNET hSession;   
//     LPSTR lpResult = NULL;
//     hSession = InternetOpen("WinInet", INTERNET_OPEN_TYPE_PRECONFIG, NULL, NULL, 0);   
//     __try
//     {       
//        if(hSession != NULL)        
//        {          
//            HINTERNET hRequest;            
//            hRequest = InternetOpenUrlA(hSession,lpcInterNetURL, NULL,0, INTERNET_FLAG_RELOAD, 0);        
//            __try         
//            {                
//               if(hRequest != NULL)        
//               {           
//                   DWORD dwBytesRead;                  
//                   char szBuffer[BUF_SIZE] = {0};
 
//                   if(InternetReadFile(hRequest, szBuffer, BUF_SIZE, &dwBytesRead))           
//                   {                 
//                      RtlMoveMemory(buff, szBuffer, BUF_SIZE);   
//                      return 0;              
//                   }               
//               }           
//            }__finally     
//            {              
//               InternetCloseHandle(hRequest);  
//            }       
//        }   
//     }__finally    
//     {       
//        InternetCloseHandle(hSession);  
//     }   
//     return lpResult;
// }