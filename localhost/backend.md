<?xml version="1.0" encoding="UTF-8"?>
<Server port="50080" shutdown="SHUTDOWN">
  <!--
    Shutdown port: 9005 (custom for dev, change if needed)
    Shutdown command: "SHUTDOWN" (type in console to safely stop Tomcat)
  -->

  <!-- Listener to log Tomcat version at startup -->
  <Listener className="org.apache.catalina.startup.VersionLoggerListener" />

  <Service name="Catalina">
    
    <!-- HTTP Connector (development) -->
    <Connector port="8080" protocol="HTTP/1.1"
               connectionTimeout="20000"
               redirectPort="8443" />
    <!--
      port="8080": HTTP port for your apps
      redirectPort="8443": where HTTP requests redirect for HTTPS
    -->

    <!-- HTTPS Connector (SSL/Dev) -->
    <Connector port="8443" protocol="org.apache.coyote.http11.Http11NioProtocol"
               maxThreads="200"
               SSLEnabled="true"
               scheme="https"
               secure="true"
               clientAuth="false"
               sslProtocol="TLS"
               keystoreFile="conf/keystore.jks"
               keystorePass="changeit" />
    <!--
      keystoreFile: path to your Java Keystore
      keystorePass: password for the keystore
      Adjust for your local SSL setup
    -->

    <!-- Engine to handle requests -->
    <Engine name="Catalina" defaultHost="localhost">

      <!-- Default Host -->
      <Host name="localhost" appBase="webapps"
            unpackWARs="true" autoDeploy="true">
        <!--
          appBase: folder where apps are deployed
          unpackWARs: auto-unpack WAR files
          autoDeploy: watch for changes and auto-reload
        -->
      </Host>

      <!-- Example of adding a custom virtual host -->
      <!--
      <Host name="myapp.local" appBase="webapps/myapp" unpackWARs="true" autoDeploy="true">
        <Alias>www.myapp.local</Alias>
      </Host>
      -->

    </Engine>

  </Service>

</Server>
<!-- Dynamic User Preferences Panel -->
<div id="user-preferences" style="position: fixed; bottom: 20px; right: 20px; 
     background: #222; color: #fff; padding: 15px; border-radius: 8px; z-index: 1000;">
  <h4 style="margin-top:0;">UI Settings</h4>
  <label>
    Theme:
    <select id="theme-select">
      <option value="dark">Dark</option>
      <option value="light">Light</option>
    </select>
  </label>
  <br/><br/>
  
  <label>
    Auto-refresh (seconds):
    <input type="number" id="auto-refresh" min="5" max="120" step="5" value="15"/>
  </label>
  <br/><br/>
  
  <label>
    Show Full Log:
    <input type="checkbox" id="show-full-log"/>
  </label>
</div>

<script>
// --- Cookie helpers ---
function setCookie(name, value, days=365) {
  const date = new Date();
  date.setTime(date.getTime() + (days*24*60*60*1000));
  document.cookie = name + "=" + encodeURIComponent(value) + "; expires=" + date.toUTCString() + "; path=/";
}
function getCookie(name) {
  const ca = document.cookie.split(';');
  for(let i=0;i<ca.length;i++){
    let c = ca[i].trim();
    if(c.indexOf(name+'=')==0) return decodeURIComponent(c.substring(name.length+1));
  }
  return null;
}

// --- Apply UI settings dynamically ---
function applyPreferences() {
  const theme = getCookie("theme") || "dark";
  document.body.dataset.theme = theme;   // Assume CSS handles [data-theme="dark"] / "light"

  const autoRefresh = parseInt(getCookie("autoRefresh") || "15");
  if(window.autoRefreshInterval) clearInterval(window.autoRefreshInterval);
  window.autoRefreshInterval = setInterval(() => location.reload(), autoRefresh * 1000);

  const showFullLog = getCookie("showFullLog") === "true";
  const consoles = document.querySelectorAll(".console"); // Adjust selector for your Buildbot logs
  consoles.forEach(c => {
    c.style.display = showFullLog ? "block" : "none";
  });
}

// --- Initialize controls ---
document.addEventListener("DOMContentLoaded", function() {
  const theme = getCookie("theme") || "dark";
  document.getElementById("theme-select").value = theme;

  const autoRefresh = getCookie("autoRefresh") || "15";
  document.getElementById("auto-refresh").value = autoRefresh;

  const showFullLog = getCookie("showFullLog") === "true";
  document.getElementById("show-full-log").checked = showFullLog;

  applyPreferences();
});

// --- Control event listeners ---
document.getElementById("theme-select").addEventListener("change", e => {
  setCookie("theme", e.target.value);
  applyPreferences();
});

document.getElementById("auto-refresh").addEventListener("change", e => {
  setCookie("autoRefresh", e.target.value);
  applyPreferences();
});

document.getElementById("show-full-log").addEventListener("change", e => {
  setCookie("showFullLog", e.target.checked);
  applyPreferences();
});
</script>
