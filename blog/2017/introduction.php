<?php

$name = "Introduction Blog";
# Write the content of the blog here
$content = "<p>Here we are, my very first blog post. The main objective of
this post is to give a little taste of who I am as a person
and also motivate the existence of this site.</p>

<p>So who am I? Well, at risk of plagiarising my own Linked-In profile, I am a graduate student at the University of Virginia
currently pursuing my Masters in Data Science. I chose to pursue this degree as I saw Data Science as the most cutting-edge manifestation of the subjects I studied as an undergrad
(I double majored in Computer Science and Mathematics with a concentration in Probability and Statistics, also at the University of Virginia). I will complete
this degree in May 2018, so I am also going through the trials
and tribulations of a first-time job seeker. That being said, I do
not want to get into too much more detail about myself here,
because that is what this site is about! Exploring it should give
you a relatively complete picture of who I am and what I am
all about.</p>

<p>So why exactly am I making a site for myself? I've listed
a few compelling reasons on the homepage of this site,
but really the motivation for this site came from enough
people telling me that it would be a good idea to have
a personal site. I put off making one for various reasons,
but once I discovered that I already used (Github), had
a mechanism for hosting static websites for free (Github Pages),
I was officially out of excuses. I can think of a few additional reasons beyond what has already been listed. I think the exercise of publishing content could very well change the way
I interact with the world. Whenever I am undergoing some
interesting or challenging problem in my life, I can view it through the lens of something that can be written up and
posted to the world. I imagine that this will
help me engage with the world around me. Publishing is also
a good mechanism to help hold myself accountable. My next
blog post is going to involve my 2017-2018 New Years resolutions and the hope is that putting them out in a more
permanent way online will help me to actually remember and
follow through on them.</p>

<p>So what exactly do I want this site to be? At the end of the day,
I just it to be the most complete digital picture of myself out
there, and one that I have complete and total control over.
Beyond that, I do not know what this site could become. Most
notably, I do not want to set any sort of goal or theme for this
blog. It will certainly contain updates on my Capstone research
and experience as a first-time job hunter, but I do not want to
limit myself to those things. This is really an outlet to share
anything in my life that I think others might find useful.</p>

<p>Will that in mind, I hope that you will explore the rest of my site and I can't wait to see how this project evolves!</p>";
$date = "12/23/2017";
$path = "blog/2017/introduction.php";
?>


<!DOCTYPE HTML>
<!--
	Hyperspace by HTML5 UP
	html5up.net | @ajlkn
	Free for personal and commercial use under the CCA 3.0 license (html5up.net/license)
-->
<html>
	<head>
		<title>Ben Greenawald</title>
		<meta charset="utf-8" />
		<meta name="viewport" content="width=device-width, initial-scale=1" />
		<!--[if lte IE 8]><script src="assets/js/ie/html5shiv.js"></script><![endif]-->
		<link rel="stylesheet" href="../../assets/css/main.css" />
		<!--[if lte IE 9]><link rel="stylesheet" href="assets/css/ie9.css" /><![endif]-->
		<!--[if lte IE 8]><link rel="stylesheet" href="assets/css/ie8.css" /><![endif]-->
	</head>
	<body>

		<!-- Header -->
			<header id="header">
			</header>

		<!-- Wrapper -->
			<div id="wrapper">

				<!-- Main -->
					<section id="main" class="wrapper style2">
						<div class="inner">
							<h1 class="major">Introduction Blog</h1>
							<p><?php echo $content;?></p>
						</div>
					</section>

			</div>

		<!-- Footer -->
			<footer id="footer" class="wrapper alt">
				<div class="inner">
					<ul class="menu">
						<li><i>Maintained by <a href="mailto:bgreenawald@gmail.com">Ben Greenawald</a>.</li><li>Design: <a href="http://html5up.net">HTML5 UP</a></li>
					</ul>
				</div>
			</footer>

		<!-- Scripts -->
			<script src="../../assets/js/jquery.min.js"></script>
			<script>
                $(function(){$('#header').load('../../header2.html');});
            </script>
			<script src="../../assets/js/jquery.scrollex.min.js"></script>
			<script src="../../assets/js/jquery.scrolly.min.js"></script>
			<script src="../../assets/js/skel.min.js"></script>
			<script src="../../assets/js/util.js"></script>
			<!--[if lte IE 8]><script src="assets/js/ie/respond.min.js"></script><![endif]-->
			<script src="../../assets/js/main.js"></script>

	</body>
</html>