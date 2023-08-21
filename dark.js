if (window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches) {
	var link = document.createElement( "link" );
    link.href = "/dark.css";
	link.type = "text/css";
	link.rel = "stylesheet";
	link.media = "screen,print";

	document.getElementsByTagName( "head" )[0].appendChild( link );
}