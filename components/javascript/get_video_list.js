returner = getlist()

function getlist() {
    a = document.getElementsByClassName("yt-simple-endpoint style-scope ytd-playlist-video-renderer")
    links = []
    for (items in a) { links.push(a[items].href) }
    return links
}