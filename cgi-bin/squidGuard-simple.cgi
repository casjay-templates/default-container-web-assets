#!/usr/bin/env perl 
#
# Sample CGI to explain to the user that the URL is blocked and by which rule set
#
# By P�l Baltzersen 1998
# Modifications by Christine Kronberg, 2007.
#

$QUERY_STRING = $ENV{'QUERY_STRING'};
$DOCUMENT_ROOT = $ENV{'DOCUMENT_ROOT'};

# Email Adresse des Proxy Administrators:
# Edit to your requirements. Make sure to keep the @ escaped.
my $PROXYEMAIL = "proxymaster\@foo.bar";
#
#
$clientaddr = "";
$clientname = "";
$clientuser = "";
$clientgroup = "";
$targetgroup = "";
$url = "";
$time = time;
@day = ("Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday");
@month = ("Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec");

while ($QUERY_STRING =~ /^\&?([^&=]+)=([^&=]*)(.*)/) {
  $key = $1;
  $value = $2;
  $QUERY_STRING = $3;
  if ($key =~ /^(clientaddr|clientname|clientuser|clientgroup|targetgroup|url)$/) {
    eval "\$$key = \$value";
  }
  if ($QUERY_STRING =~ /^url=(.*)/) {
    $url = $1;
    $QUERY_STRING = "";
  }
}

if ($url =~ /\.(gif|jpg|jpeg|mpg|mpeg|avi|mov)$/i) {
  print "Content-Type: image/gif\n";
  ($sec,$min,$hour,$mday,$mon,$year,$wday,$yday,$isdst) = gmtime($time);
  printf "Expires: %s, %02d-%s-%02d %02d:%02d:%02d GMT\n\n", $day[$wday],$mday,$month[$mon],$year,$hour,$min,$sec;
  open(GIF, "$DOCUMENT_ROOT/images/blocked.gif");
  while (<GIF>) {
    print;
  }
  close(GIF)
} else {
  print "Content-type: text/html\n";
  ($sec,$min,$hour,$mday,$mon,$year,$wday,$yday,$isdst) = gmtime($time);
  printf "Expires: %s, %02d-%s-%02d %02d:%02d:%02d GMT\n\n", $day[$wday],$mday,$month[$mon],$year,$hour,$min,$sec;
  print "<HTML>\n\n  <HEAD>\n    <TITLE>302 Access denied</TITLE>\n  </HEAD>\n\n";
  print "  <BODY BGCOLOR=\"#FFFFFF\">\n";
  if ($srcclass eq "unknown") {
    print "    <P ALIGN=RIGHT>\n";
    print "      <A HREF=\"//www.squidguard.org/\"><IMG SRC=\"/images/your-logo.gif\"\n";
    print "         BORDER=0></A>\n      </P>\n\n";
    print "    <H1 ALIGN=CENTER>Access denied because<BR>this client is not<BR>defined on the proxy</H1>\n\n";
    print "    <TABLE BORDER=0 ALIGN=CENTER>\n";
    print "      <TR><TH ALIGN=RIGHT>Supplementary info</TH><TH ALIGN=CENTER>:</TH><TH ALIGN=LEFT>&nbsp;</TH></TR>\n";
    print "      <TR><TH ALIGN=RIGHT>Client address</TH><TH ALIGN=CENTER>=</TH><TH ALIGN=LEFT>$clientaddr</TH></TR>\n";
    print "      <TR><TH ALIGN=RIGHT>Client name</TH><TH ALIGN=CENTER>=</TH><TH ALIGN=LEFT>$clientname</TH></TR>\n";
    print "      <TR><TH ALIGN=RIGHT>User ident</TH><TH ALIGN=CENTER>=</TH><TH ALIGN=LEFT>$clientuser</TH></TR>\n";
    print "      <TR><TH ALIGN=RIGHT>Client group</TH><TH ALIGN=CENTER>=</TH><TH ALIGN=LEFT>$clientgroup</TH></TR>\n";
    print "    </TABLE>\n\n";
    print "    <P ALIGN=CENTER>If this is wrong, contact<BR>\n";
    print "      <A HREF=$PROXYEMAIL>$PROXYEMAIL</A>\n";
    print "    </P>\n\n";
  } elsif ($targetclass eq "in-addr") {
    print "    <P ALIGN=RIGHT>\n";
    print "      <A HREF=\"//www.squidguard.org/\"><IMG SRC=\"/images/your-logo.gif\"\n";
    print "         BORDER=0></A>\n      </P>\n\n";
    print "    <H1 ALIGN=CENTER>IP address URLs<BR>are not allowed<BR>from this client</H1>\n\n";
    print "    <TABLE BORDER=0 ALIGN=CENTER>\n";
    print "      <TR><TH ALIGN=RIGHT>Supplementary info</TH><TH ALIGN=CENTER>:</TH><TH ALIGN=LEFT>&nbsp;</TH></TR>\n";
    print "      <TR><TH ALIGN=RIGHT>Client address</TH><TH ALIGN=CENTER>=</TH><TH ALIGN=LEFT>$clientaddr</TH></TR>\n";
    print "      <TR><TH ALIGN=RIGHT>Client name</TH><TH ALIGN=CENTER>=</TH><TH ALIGN=LEFT>$clientname</TH></TR>\n";
    print "      <TR><TH ALIGN=RIGHT>User ident</TH><TH ALIGN=CENTER>=</TH><TH ALIGN=LEFT>$clientuser</TH></TR>\n";
    print "      <TR><TH ALIGN=RIGHT>Client group</TH><TH ALIGN=CENTER>=</TH><TH ALIGN=LEFT>$clientgroup</TH></TR>\n";
    print "      <TR><TH ALIGN=RIGHT>URL</TH><TH ALIGN=CENTER>=</TH><TH ALIGN=LEFT>$url</TH></TR>\n";
    print "      <TR><TH ALIGN=RIGHT>Target class</TH><TH ALIGN=CENTER>=</TH><TH ALIGN=LEFT>$targetgroup</TH></TR>\n";
    print "    </TABLE>\n\n";
    print "    <P ALIGN=CENTER>No domain matching the given IP address could be found. Access to this\n";
    print "    kind of address is forbidden.<BR>\n";
    print "    If this is wrong, contact<BR>\n";
    print "    <A HREF=mailto:$PROXYEMAIL>$PROXYEMAIL</A>\n";
    print "    </P>\n\n";
  } else {
    print "    <P ALIGN=RIGHT>\n";
    print "      <A HREF=\"//www.squidguard.org/\"><IMG SRC=\"/images/your-logo.gif\"\n";
    print "         BORDER=0></A>\n      </P>\n\n";
    print "    <H1 ALIGN=CENTER>Access denied</H1>\n\n";
    print "    <TABLE BORDER=0 ALIGN=CENTER>\n";
    print "      <TR><TH ALIGN=RIGHT>Supplementary info</TH><TH ALIGN=CENTER>:</TH><TH ALIGN=LEFT>&nbsp;</TH></TR>\n";
    print "      <TR><TH ALIGN=RIGHT>Client address</TH><TH ALIGN=CENTER>=</TH><TH ALIGN=LEFT>$clientaddr</TH></TR>\n";
    print "      <TR><TH ALIGN=RIGHT>Client name</TH><TH ALIGN=CENTER>=</TH><TH ALIGN=LEFT>$clientname</TH></TR>\n";
    print "      <TR><TH ALIGN=RIGHT>User ident</TH><TH ALIGN=CENTER>=</TH><TH ALIGN=LEFT>$clientuser</TH></TR>\n";
    print "      <TR><TH ALIGN=RIGHT>Client group</TH><TH ALIGN=CENTER>=</TH><TH ALIGN=LEFT>$clientgroup</TH></TR>\n";
    print "      <TR><TH ALIGN=RIGHT>URL</TH><TH ALIGN=CENTER>=</TH><TH ALIGN=LEFT>$url</TH></TR>\n";
    print "      <TR><TH ALIGN=RIGHT>Target class</TH><TH ALIGN=CENTER>=</TH><TH ALIGN=LEFT>$targetgroup</TH></TR>\n";
    print "    </TABLE>\n\n";
    print "    <P ALIGN=CENTER>If this is wrong, contact<BR>\n";
    print "      <A HREF=mailto:$PROXYEMAIL>$PROXYEMAIL</A>\n";
    print "    </P>\n\n";
  }
  print "  </BODY>\n\n</HTML>\n";
}
exit 0;
