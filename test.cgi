<!DOCTYPE html>
<html>
  <head>
    <!-- meta -->
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1.0,minimum-scale=1.0">
<link rel="icon" type="image/x-icon" href="/images/logo.png">
<link rel="stylesheet" type="text/css" href="/css/common.css">

<title>Title - mysite😄</title>
<meta name="description" content="#!/usr/bin/env perl">
  </head>
  <body>
    <div class="container">
      <div class="header">
        <!-- header -->
<div class="main">
  <h1>
    <a href="/">Giblog Web Site</a>
  </h1>
</div>

      </div>
      <div class="main">
        <div class="content">
          <div class="entry">
  <div class="top">
    <!-- top -->

  </div>
  <div class="middle">
    <p>
  #!/usr/bin/env perl
</p>
<p>
  use strict;
</p>
<p>
  use warnings;
</p>
<p>
  use utf8;
</p>
<p>
  use Encode 'encode';
</p>
<p>
  # Title mail form
</p>
<p>
  my $title = 'Mail form';
</p>
<p>
  # Content mail form
</p>
<p>
  my $content = <<"EOS";
</p>
<h2><a href="/test.cgi">Title</a></h2>
<div>
  Content
</div>
<p>
  EOS
</p>
<p>
  $content = build_html($title, $content);
</p>
<p>
  my $html = <<"EOS";
</p>
<p>
  Content-type: text/html; charset=UTF-8
</p>
<p>
  $content
</p>
<p>
  EOS
</p>
<p>
  print encode('UTF-8', $html);
</p>
<p>
  sub build_html {
</p>
  my ($title, $content) = @_;
  
  local $/;
  my $html = <DATA>;
  
  $html =~ s/\$TITLE/$title/;
  $html =~ s/\$CONTENT/$content/;
  
  return $html;
<p>
  }
</p>
<p>
  __DATA__
</p>

  </div>
  <div class="bottom">
    <!-- bottom -->

  </div>
</div>

        </div>
        <div class="side">
          <!-- side -->
<div class="side-list">
  <div class="side-list-title">
    Side Bar
  </div>
  <ul>
    <li><a href="/list.html">Entries</a></li>
    <li>Bar</li>
    <li>Baz</li>
  </ul>
</div>

        </div>
      </div>
      <div class="footer">
        <div class="perlri_link">
  <a rel="nofollow" href="https://perlclub.net">Perlクラブ</a>
</div>

<script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-4525414114581084"
     crossorigin="anonymous"></script>
     
      </div>
    </div>
  </body>
</html>
