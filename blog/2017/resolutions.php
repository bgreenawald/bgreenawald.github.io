<?php

$name = "2017 New Years Resolutions";
# Write the content of the blog here
$content = "<p>I'm going to be honest here, I am not the biggest fan of New
Years Resolutions. Don't get me wrong, I think the idea of
identifying areas for self-improvement and working
towards those goals is great, I just think waiting for
a calendar to tell you \"it's time to improve yourself\"
is a bit silly. However, I do think the New Years at least
provides a time to sit back and reflect, especially since
it is around this time that people, myself included, have
some time off and therefore can spend time reflecting.
I've decided this year to publish my New Years Resolutions,
mostly so I have a tangible and public set of goals, so
anyone that reads this and knows me can hold me accountable to these resolutions. Also, I frankly do not remember what
my resolutions last year were, so having them easily accessible
should increase my chances of actually doing them.</p>

<p>Without further ado, let's jump into my New Years Resolutions for 2018.<p>
<ol>
 <li> <strong>Consume less, create more.</strong> I do not
consider myself a procrastinator. In fact, I am pretty good
at getting things done well before they need to be done.
However, I am quite adept at wasting time. Too much of
my day is spent consuming content that adds no real
value to my life. Youtube and Netflix are the worst offenders here, with
Facebook and Snapchat being close runner-ups. A simple
way to achieve this goal would be to remove myself from
those platforms, but I do not see that as realistic. There are
very good things those platforms have to offer, I just need
to be better at practicing moderation. More tangibly, 
I need to not use them just as a means to kill time. What
do I plan on doing with all the time I'll be getting back?
Well, create more, whatever that may look like. This
website is a great start, so maintaining and growing it
out will be a good way to work towards this goal. Getting back
into writing music, and maybe this time actually record some
of it, will also be valuable in achieving this goal.
Continuing to work on the <i>projmanr</i> R package and
<i>Super Smash Bros. SE</i> game mod will also be productive as well.</li>

<li><strong>Invest more in people.</strong> I admit it,
I can be a bit of a workaholic. For easily the past decade
of my life, school has been the most important aspect
of my life, especially my last four years in college.
This emphasis on my education has really led me
to neglect the people in my life, especially my group
of friends.
But I am really starting to see that while learning is
incredibly important, school itself really isn't. Well,
let me rephrase that. Certain very time-consuming
aspects of school, like grades, really aren''t that important.
My time would be much better spent ensuring that I have
learned the material, and not worrying that much about
grades at all. All the time I can save here can be reinvested
in the people around me. And even if I am not 
successful in truly convincing myself to put less time into
my schoolwork, there is still a whole lot of wasted time
in my life (see 1), that I can get a hold of and redirect to
the people that I care about (and even finding new people
to care about!).
</li>
<li><strong>Change the way I eat food.</strong> No, I am not
going on a diet. This resolution has nothing to do with what
or how much I eat, but rather <i>why</i> I eat. I am very happy
with my weight and overall think I have a pretty strong diet. 
But I do, far too often, find myself eating for reasons other than
\"I'm hungry.\" The most sinister of these is eating out of habit.
If I normally get a milkshake from Five Guys on Mondays, then
I often find myself getting a milkshake from Five Guys on Mondays, even if I am not hungry in the least! These patterns
are going to be hard to break, but ultimately it is very important
that I do it now, when my metabolism is still forgiving. There
are other reasons for eating, like stress, boredom, or socializing
that I hope to break, but if I can eradicate habitual eating, I will
consider this resolution a success. </li>
</ol>

<p>So there they are. I intentionally left my resolutions a little bit vague, without too many specific ways to achieve them. This is because my life at the moment can be so sporadic that I
think getting to nitty-gritty with my resolutions will sharply
decrease my chance of attaining them. I intend to post
updates as the year progresses. Happy New Year!";
$date = "12/26/2017";
$path = "blog/2017/resolutions.php";
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
							<h1 class="major"><?php echo $name;?></h1>
							<?php echo $content;?>
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