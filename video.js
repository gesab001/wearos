var video = (function() {

    this.setFilename = function(source) {
        console.log("source: " + source);
        videoEl = document.getElementById("videoPlayer");
		videoEl.src = source;
		videoEl.load();
    };

    return this;
}());