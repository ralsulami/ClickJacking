Demo: A simple example of Clickjacking
Student Name: Rayan Alsulami
CINF302: Secure Coding 
Due Date: November 25, 2024

What is Clickjacking?
A user is tricked into clicking on something on a webpage that they can’t see or that looks like something else. This trick can cause unexpected actions to happen without the user realizing it.

Examples of Clicking Jacking:
Like/Share Clickjacking
Cursor Jacking
Scroll-Related Attacks
Cookie Jacking
Transparent Overlays
Password Manager Attacks

What is iFrame?
An element which loads another HTML page within your current web page.

How to prevent iFrame? 
X-Frame-Options is a HTTP header tells browsers whether a page is allowed to be displayed in a <frame> or <iframe>:
X-Frame-Options: deny - Completely blocks the content from being framed by any domain.
X-Frame-Options: sameorigin - Allows only the current website to frame its content.
X-Frame-Options: Permits framing only from a specific trusted URL.


Content Security Policy (CSP) is a security standard that prevents Clickjacking and other attacks by defining which sources are allowed to load content on your site.


Resources:

https://book.hacktricks.xyz/pentesting-web/clickjacking
https://securitytrails.com/blog/clickjacking-attacks
https://portswigger.net/web-security/clickjacking
