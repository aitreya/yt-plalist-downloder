return timelists();

function timelists() {
  let a = document.getElementsByClassName("yt-simple-endpoint style-scope ytd-playlist-video-renderer")
  let sum = 0;
  for (var i = 0; i < a.length; i++) {
    let timestamp = a[i].getElementsByClassName("style-scope ytd-thumbnail-overlay-time-status-renderer")[1].innerText;
    let aa = convert(timestamp)
    sum += aa
  }
  return secondsToTime(sum)
}

function convert(hms) {
  var a = hms.split(':');
  let len = a.length
  if (len == 1) {
    return a[0]*1
  }
  else if (len == 2) {
    return (a[0]*60) + a[1]*1
  }
  else if (len == 3) {
    return (a[0]*3600) + (a[1]*60) + a[2]*1
  }
  return 0
}

function secondsToTime(secs)
{
    var hours = Math.floor(secs / (60 * 60));

    var divisor_for_minutes = secs % (60 * 60);
    var minutes = Math.floor(divisor_for_minutes / 60);

    var divisor_for_seconds = divisor_for_minutes % 60;
    var seconds = Math.ceil(divisor_for_seconds);

    var obj = `${hours} Hours ${minutes} Minutes ${seconds} Seconds`;
    return obj;
}