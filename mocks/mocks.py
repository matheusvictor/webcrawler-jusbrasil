from bs4 import BeautifulSoup


def create_bs4_object_from_tjal():
    html = """
        <html><head>
    	<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
    	<meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">










        <script language="javascript" type="text/JavaScript" src="https://www2.tjal.jus.br/sajcas/verificarLogin.js?script=1691279960137"></script>

        <script language="javascript">
            if (window.sajcas && window.sajcas.usuarioLogadoNoCasServer) {
                var GATEWAY_TRUE = 'gateway=true', GATEWAY_FALSE = 'gateway=false';
                var urlRetornoSistema = '';
                if (urlRetornoSistema === '') {
                    urlRetornoSistema = window.location.href;
                }

                if (urlRetornoSistema.indexOf(GATEWAY_FALSE) !== -1) {
                    urlRetornoSistema = urlRetornoSistema.replace(GATEWAY_FALSE, GATEWAY_TRUE);
                } else {
                    urlRetornoSistema.lastIndexOf('?') !== -1 ? urlRetornoSistema += '&' : urlRetornoSistema += '?';
                    urlRetornoSistema += GATEWAY_TRUE;
                }

                window.location.href = urlRetornoSistema;
            }
        </script>


    	<title>Portal de Serviços e-SAJ</title>



    <script type="text/javascript">(window.NREUM||(NREUM={})).init={ajax:{deny_list:["bam.nr-data.net"]}};(window.NREUM||(NREUM={})).loader_config={licenseKey:"b61bdf610d",applicationID:"111652883"};;/*! For license information please see nr-loader-rum-1.237.1.min.js.LICENSE.txt */
    (()=>{"use strict";var e,t,n={5763:(e,t,n)=>{n.d(t,{P_:()=>f,Mt:()=>p,C5:()=>s,DL:()=>m,OP:()=>j,lF:()=>E,Yu:()=>y,Dg:()=>g,CX:()=>c,GE:()=>b,sU:()=>_});var r=n(8632),i=n(9567);const a={beacon:r.ce.beacon,errorBeacon:r.ce.errorBeacon,licenseKey:void 0,applicationID:void 0,sa:void 0,queueTime:void 0,applicationTime:void 0,ttGuid:void 0,user:void 0,account:void 0,product:void 0,extra:void 0,jsAttributes:{},userAttributes:void 0,atts:void 0,transactionName:void 0,tNamePlain:void 0},o={};function s(e){if(!e)throw new Error("All info objects require an agent identifier!");if(!o[e])throw new Error("Info for ".concat(e," was never set"));return o[e]}function c(e,t){if(!e)throw new Error("All info objects require an agent identifier!");o[e]=(0,i.D)(t,a),(0,r.Qy)(e,o[e],"info")}var d=n(7056);const u=()=>{const e={blockSelector:"[data-nr-block]",maskInputOptions:{password:!0}};return{allow_bfcache:!0,privacy:{cookies_enabled:!0},ajax:{deny_list:void 0,block_internal:!0,enabled:!0,harvestTimeSeconds:10},distributed_tracing:{enabled:void 0,exclude_newrelic_header:void 0,cors_use_newrelic_header:void 0,cors_use_tracecontext_headers:void 0,allowed_origins:void 0},session:{domain:void 0,expiresMs:d.oD,inactiveMs:d.Hb},ssl:void 0,obfuscate:void 0,jserrors:{enabled:!0,harvestTimeSeconds:10},metrics:{enabled:!0},page_action:{enabled:!0,harvestTimeSeconds:30},page_view_event:{enabled:!0},page_view_timing:{enabled:!0,harvestTimeSeconds:30,long_task:!1},session_trace:{enabled:!0,harvestTimeSeconds:10},harvest:{tooManyRequestsDelay:60},session_replay:{enabled:!1,harvestTimeSeconds:60,sampleRate:.1,errorSampleRate:.1,maskTextSelector:"*",maskAllInputs:!0,get blockClass(){return"nr-block"},get ignoreClass(){return"nr-ignore"},get maskTextClass(){return"nr-mask"},get blockSelector(){return e.blockSelector},set blockSelector(t){e.blockSelector+=",".concat(t)},get maskInputOptions(){return e.maskInputOptions},set maskInputOptions(t){e.maskInputOptions={...t,password:!0}}},spa:{enabled:!0,harvestTimeSeconds:10}}},l={};function f(e){if(!e)throw new Error("All configuration objects require an agent identifier!");if(!l[e])throw new Error("Configuration for ".concat(e," was never set"));return l[e]}function g(e,t){if(!e)throw new Error("All configuration objects require an agent identifier!");l[e]=(0,i.D)(t,u()),(0,r.Qy)(e,l[e],"config")}function p(e,t){if(!e)throw new Error("All configuration objects require an agent identifier!");var n=f(e);if(n){for(var r=t.split("."),i=0;i<r.length-1;i++)if("object"!=typeof(n=n[r[i]]))return;n=n[r[r.length-1]]}return n}const h={accountID:void 0,trustKey:void 0,agentID:void 0,licenseKey:void 0,applicationID:void 0,xpid:void 0},v={};function m(e){if(!e)throw new Error("All loader-config objects require an agent identifier!");if(!v[e])throw new Error("LoaderConfig for ".concat(e," was never set"));return v[e]}function b(e,t){if(!e)throw new Error("All loader-config objects require an agent identifier!");v[e]=(0,i.D)(t,h),(0,r.Qy)(e,v[e],"loader_config")}const y=(0,r.mF)().o;var w=n(385),A=n(6818);const x={buildEnv:A.Re,bytesSent:{},queryBytesSent:{},customTransaction:void 0,disabled:!1,distMethod:A.gF,isolatedBacklog:!1,loaderType:void 0,maxBytes:3e4,offset:Math.floor(w._A?.performance?.timeOrigin||w._A?.performance?.timing?.navigationStart||Date.now()),onerror:void 0,origin:""+w._A.location,ptid:void 0,releaseIds:{},session:void 0,xhrWrappable:"function"==typeof w._A.XMLHttpRequest?.prototype?.addEventListener,version:A.q4,denyList:void 0},D={};function j(e){if(!e)throw new Error("All runtime objects require an agent identifier!");if(!D[e])throw new Error("Runtime for ".concat(e," was never set"));return D[e]}function _(e,t){if(!e)throw new Error("All runtime objects require an agent identifier!");D[e]=(0,i.D)(t,x),(0,r.Qy)(e,D[e],"runtime")}function E(e){return function(e){try{const t=s(e);return!!t.licenseKey&&!!t.errorBeacon&&!!t.applicationID}catch(e){return!1}}(e)}},9567:(e,t,n)=>{n.d(t,{D:()=>i});var r=n(50);function i(e,t){try{if(!e||"object"!=typeof e)return(0,r.Z)("Setting a Configurable requires an object as input");if(!t||"object"!=typeof t)return(0,r.Z)("Setting a Configurable requires a model to set its initial properties");const n=Object.create(Object.getPrototypeOf(t),Object.getOwnPropertyDescriptors(t)),a=0===Object.keys(n).length?e:n;for(let o in a)if(void 0!==e[o])try{"object"==typeof e[o]&&"object"==typeof t[o]?n[o]=i(e[o],t[o]):n[o]=e[o]}catch(e){(0,r.Z)("An error occurred while setting a property of a Configurable",e)}return n}catch(e){(0,r.Z)("An error occured while setting a Configurable",e)}}},6818:(e,t,n)=>{n.d(t,{Re:()=>i,gF:()=>a,q4:()=>r});const r="1.237.1",i="PROD",a="CDN"},385:(e,t,n)=>{n.d(t,{FN:()=>o,IF:()=>d,Nk:()=>l,Tt:()=>s,_A:()=>a,il:()=>r,pL:()=>c,v6:()=>i,w1:()=>u});const r="undefined"!=typeof window&&!!window.document,i="undefined"!=typeof WorkerGlobalScope&&("undefined"!=typeof self&&self instanceof WorkerGlobalScope&&self.navigator instanceof WorkerNavigator||"undefined"!=typeof globalThis&&globalThis instanceof WorkerGlobalScope&&globalThis.navigator instanceof WorkerNavigator),a=r?window:"undefined"!=typeof WorkerGlobalScope&&("undefined"!=typeof self&&self instanceof WorkerGlobalScope&&self||"undefined"!=typeof globalThis&&globalThis instanceof WorkerGlobalScope&&globalThis),o=""+a?.location,s=/iPad|iPhone|iPod/.test(navigator.userAgent),c=s&&"undefined"==typeof SharedWorker,d=(()=>{const e=navigator.userAgent.match(/Firefox[/\s](\d+\.\d+)/);return Array.isArray(e)&&e.length>=2?+e[1]:0})(),u=Boolean(r&&window.document.documentMode),l=!!navigator.sendBeacon},1117:(e,t,n)=>{n.d(t,{w:()=>a});var r=n(50);const i={agentIdentifier:"",ee:void 0};class a{constructor(e){try{if("object"!=typeof e)return(0,r.Z)("shared context requires an object as input");this.sharedContext={},Object.assign(this.sharedContext,i),Object.entries(e).forEach((e=>{let[t,n]=e;Object.keys(i).includes(t)&&(this.sharedContext[t]=n)}))}catch(e){(0,r.Z)("An error occured while setting SharedContext",e)}}}},8e3:(e,t,n)=>{n.d(t,{L:()=>u,R:()=>c});var r=n(2177),i=n(1284),a=n(4322),o=n(3325);const s={};function c(e,t){const n={staged:!1,priority:o.p[t]||0};d(e),s[e].get(t)||s[e].set(t,n)}function d(e){e&&(s[e]||(s[e]=new Map))}function u(){let e=arguments.length>0&&void 0!==arguments[0]?arguments[0]:"",t=arguments.length>1&&void 0!==arguments[1]?arguments[1]:"feature";if(d(e),!e||!s[e].get(t))return o(t);s[e].get(t).staged=!0;const n=[...s[e]];function o(t){const n=e?r.ee.get(e):r.ee,o=a.X.handlers;if(n.backlog&&o){var s=n.backlog[t],c=o[t];if(c){for(var d=0;s&&d<s.length;++d)l(s[d],c);(0,i.D)(c,(function(e,t){(0,i.D)(t,(function(t,n){n[0].on(e,n[1])}))}))}delete o[t],n.backlog[t]=null,n.emit("drain-"+t,[])}}n.every((e=>{let[t,n]=e;return n.staged}))&&(n.sort(((e,t)=>e[1].priority-t[1].priority)),n.forEach((e=>{let[t]=e;o(t)})))}function l(e,t){var n=e[1];(0,i.D)(t[n],(function(t,n){var r=e[0];if(n[0]===r){var i=n[1],a=e[3],o=e[2];i.apply(a,o)}}))}},2177:(e,t,n)=>{n.d(t,{ee:()=>d});var r=n(8632),i=n(2210),a=n(1284),o=n(5763),s="nr@context";let c=(0,r.fP)();var d;function u(){}function l(){return new u}function f(){d.aborted=!0,d.backlog={}}c.ee?d=c.ee:(d=function e(t,n){var r={},c={},g={},p=!1;try{p=16===n.length&&(0,o.OP)(n).isolatedBacklog}catch(e){}var h={on:b,addEventListener:b,removeEventListener:y,emit:m,get:A,listeners:w,context:v,buffer:x,abort:f,aborted:!1,isBuffering:D,debugId:n,backlog:p?{}:t&&"object"==typeof t.backlog?t.backlog:{}};return h;function v(e){return e&&e instanceof u?e:e?(0,i.X)(e,s,l):l()}function m(e,n,r,i,a){if(!1!==a&&(a=!0),!d.aborted||i){t&&a&&t.emit(e,n,r);for(var o=v(r),s=w(e),u=s.length,l=0;l<u;l++)s[l].apply(o,n);var f=j()[c[e]];return f&&f.push([h,e,n,o]),o}}function b(e,t){r[e]=w(e).concat(t)}function y(e,t){var n=r[e];if(n)for(var i=0;i<n.length;i++)n[i]===t&&n.splice(i,1)}function w(e){return r[e]||[]}function A(t){return g[t]=g[t]||e(h,t)}function x(e,t){var n=j();h.aborted||(0,a.D)(e,(function(e,r){t=t||"feature",c[r]=t,t in n||(n[t]=[])}))}function D(e){return!!j()[c[e]]}function j(){return h.backlog}}(void 0,"globalEE"),c.ee=d)},5546:(e,t,n)=>{n.d(t,{E:()=>r,p:()=>i});var r=n(2177).ee.get("handle");function i(e,t,n,i,a){a?(a.buffer([e],i),a.emit(e,t,n)):(r.buffer([e],i),r.emit(e,t,n))}},4322:(e,t,n)=>{n.d(t,{X:()=>a});var r=n(5546);a.on=o;var i=a.handlers={};function a(e,t,n,a){o(a||r.E,i,e,t,n)}function o(e,t,n,i,a){a||(a="feature"),e||(e=r.E);var o=t[a]=t[a]||{};(o[n]=o[n]||[]).push([e,i])}},3239:(e,t,n)=>{n.d(t,{bP:()=>s,iz:()=>c,m$:()=>o});var r=n(385);let i=!1,a=!1;try{const e={get passive(){return i=!0,!1},get signal(){return a=!0,!1}};r._A.addEventListener("test",null,e),r._A.removeEventListener("test",null,e)}catch(e){}function o(e,t){return i||a?{capture:!!e,passive:i,signal:t}:!!e}function s(e,t){let n=arguments.length>2&&void 0!==arguments[2]&&arguments[2],r=arguments.length>3?arguments[3]:void 0;window.addEventListener(e,t,o(n,r))}function c(e,t){let n=arguments.length>2&&void 0!==arguments[2]&&arguments[2],r=arguments.length>3?arguments[3]:void 0;document.addEventListener(e,t,o(n,r))}},4402:(e,t,n)=>{n.d(t,{Rl:()=>o,ky:()=>s});var r=n(385);const i="xxxxxxxx-xxxx-4xxx-yxxx-xxxxxxxxxxxx";function a(e,t){return e?15&e[t]:16*Math.random()|0}function o(){const e=r._A?.crypto||r._A?.msCrypto;let t,n=0;return e&&e.getRandomValues&&(t=e.getRandomValues(new Uint8Array(31))),i.split("").map((e=>"x"===e?a(t,++n).toString(16):"y"===e?(3&a()|8).toString(16):e)).join("")}function s(e){const t=r._A?.crypto||r._A?.msCrypto;let n,i=0;t&&t.getRandomValues&&(n=t.getRandomValues(new Uint8Array(31)));const o=[];for(var s=0;s<e;s++)o.push(a(n,++i).toString(16));return o.join("")}},7056:(e,t,n)=>{n.d(t,{Bq:()=>r,Hb:()=>a,oD:()=>i});const r="NRBA",i=144e5,a=18e5},7894:(e,t,n)=>{function r(){return Math.round(performance.now())}n.d(t,{z:()=>r})},50:(e,t,n)=>{function r(e,t){"function"==typeof console.warn&&(console.warn("New Relic: ".concat(e)),t&&console.warn(t))}n.d(t,{Z:()=>r})},2587:(e,t,n)=>{n.d(t,{N:()=>c,T:()=>d});var r=n(2177),i=n(5546),a=n(8e3),o=n(3325);const s={stn:[o.D.sessionTrace],err:[o.D.jserrors,o.D.metrics],ins:[o.D.pageAction],spa:[o.D.spa],sr:[o.D.sessionReplay,o.D.sessionTrace]};function c(e,t){const n=r.ee.get(t);e&&"object"==typeof e&&(Object.entries(e).forEach((e=>{let[t,r]=e;void 0===d[t]&&(s[t]?s[t].forEach((e=>{r?(0,i.p)("feat-"+t,[],void 0,e,n):(0,i.p)("block-"+t,[],void 0,e,n),(0,i.p)("rumresp-"+t,[Boolean(r)],void 0,e,n)})):r&&(0,i.p)("feat-"+t,[],void 0,void 0,n),d[t]=Boolean(r))})),Object.keys(s).forEach((e=>{void 0===d[e]&&(s[e]?.forEach((t=>(0,i.p)("rumresp-"+e,[!1],void 0,t,n))),d[e]=!1)})),(0,a.L)(t,o.D.pageViewEvent))}const d={}},2210:(e,t,n)=>{n.d(t,{X:()=>i});var r=Object.prototype.hasOwnProperty;function i(e,t,n){if(r.call(e,t))return e[t];var i=n();if(Object.defineProperty&&Object.keys)try{return Object.defineProperty(e,t,{value:i,writable:!0,enumerable:!1}),i}catch(e){}return e[t]=i,i}},1284:(e,t,n)=>{n.d(t,{D:()=>r});const r=(e,t)=>Object.entries(e||{}).map((e=>{let[n,r]=e;return t(n,r)}))},4351:(e,t,n)=>{n.d(t,{P:()=>a});var r=n(2177);const i=()=>{const e=new WeakSet;return(t,n)=>{if("object"==typeof n&&null!==n){if(e.has(n))return;e.add(n)}return n}};function a(e){try{return JSON.stringify(e,i())}catch(e){try{r.ee.emit("internal-error",[e])}catch(e){}}}},3960:(e,t,n)=>{n.d(t,{K:()=>o,b:()=>a});var r=n(3239);function i(){return"undefined"==typeof document||"complete"===document.readyState}function a(e,t){if(i())return e();(0,r.bP)("load",e,t)}function o(e){if(i())return e();(0,r.iz)("DOMContentLoaded",e)}},8632:(e,t,n)=>{n.d(t,{EZ:()=>d,Qy:()=>c,ce:()=>a,fP:()=>o,gG:()=>u,mF:()=>s});var r=n(7894),i=n(385);const a={beacon:"bam.nr-data.net",errorBeacon:"bam.nr-data.net"};function o(){return i._A.NREUM||(i._A.NREUM={}),void 0===i._A.newrelic&&(i._A.newrelic=i._A.NREUM),i._A.NREUM}function s(){let e=o();return e.o||(e.o={ST:i._A.setTimeout,SI:i._A.setImmediate,CT:i._A.clearTimeout,XHR:i._A.XMLHttpRequest,REQ:i._A.Request,EV:i._A.Event,PR:i._A.Promise,MO:i._A.MutationObserver,FETCH:i._A.fetch}),e}function c(e,t,n){let i=o();const a=i.initializedAgents||{},s=a[e]||{};return Object.keys(s).length||(s.initializedAt={ms:(0,r.z)(),date:new Date}),i.initializedAgents={...a,[e]:{...s,[n]:t}},i}function d(e,t){o()[e]=t}function u(){return function(){let e=o();const t=e.info||{};e.info={beacon:a.beacon,errorBeacon:a.errorBeacon,...t}}(),function(){let e=o();const t=e.init||{};e.init={...t}}(),s(),function(){let e=o();const t=e.loader_config||{};e.loader_config={...t}}(),o()}},7956:(e,t,n)=>{n.d(t,{N:()=>i});var r=n(3239);function i(e){let t=arguments.length>1&&void 0!==arguments[1]&&arguments[1],n=arguments.length>2?arguments[2]:void 0,i=arguments.length>3?arguments[3]:void 0;return void(0,r.iz)("visibilitychange",(function(){if(t)return void("hidden"==document.visibilityState&&e());e(document.visibilityState)}),n,i)}},3081:(e,t,n)=>{n.d(t,{gF:()=>a,mY:()=>i,t9:()=>r,vz:()=>s,xS:()=>o});const r=n(3325).D.metrics,i="sm",a="cm",o="storeSupportabilityMetrics",s="storeEventMetrics"},7633:(e,t,n)=>{n.d(t,{Dz:()=>i,OJ:()=>o,qw:()=>a,t9:()=>r});const r=n(3325).D.pageViewEvent,i="firstbyte",a="domcontent",o="windowload"},9251:(e,t,n)=>{n.d(t,{t:()=>r});const r=n(3325).D.pageViewTiming},5938:(e,t,n)=>{n.d(t,{W:()=>a});var r=n(5763),i=n(2177);class a{constructor(e,t,n){this.agentIdentifier=e,this.aggregator=t,this.ee=i.ee.get(e,(0,r.OP)(this.agentIdentifier).isolatedBacklog),this.featureName=n,this.blocked=!1}}},9144:(e,t,n)=>{n.d(t,{j:()=>v});var r=n(3325),i=n(5763),a=n(5546),o=n(2177),s=n(7894),c=n(8e3),d=n(3960),u=n(385),l=n(50),f=n(3081),g=n(8632);function p(){const e=(0,g.gG)();["setErrorHandler","finished","addToTrace","inlineHit","addRelease","addPageAction","setCurrentRouteName","setPageViewName","setCustomAttribute","interaction","noticeError","setUserId"].forEach((t=>{e[t]=function(){for(var n=arguments.length,r=new Array(n),i=0;i<n;i++)r[i]=arguments[i];return function(t){for(var n=arguments.length,r=new Array(n>1?n-1:0),i=1;i<n;i++)r[i-1]=arguments[i];let a=[];return Object.values(e.initializedAgents).forEach((e=>{e.exposed&&e.api[t]&&a.push(e.api[t](...r))})),a.length>1?a:a[0]}(t,...r)}}))}var h=n(2587);function v(e){let t=arguments.length>1&&void 0!==arguments[1]?arguments[1]:{},v=arguments.length>2?arguments[2]:void 0,m=arguments.length>3?arguments[3]:void 0,{init:b,info:y,loader_config:w,runtime:A={loaderType:v},exposed:x=!0}=t;const D=(0,g.gG)();y||(b=D.init,y=D.info,w=D.loader_config),(0,i.Dg)(e,b||{}),(0,i.GE)(e,w||{}),y.jsAttributes??={},u.v6&&(y.jsAttributes.isWorker=!0),(0,i.CX)(e,y);const j=(0,i.P_)(e);A.denyList=[...j.ajax?.deny_list||[],...j.ajax?.block_internal?[y.beacon,y.errorBeacon]:[]],(0,i.sU)(e,A),p();const _=function(e,t){t||(0,c.R)(e,"api");const g={};var p=o.ee.get(e),h=p.get("tracer"),v="api-",m=v+"ixn-";function b(t,n,r,a){const o=(0,i.C5)(e);return null===n?delete o.jsAttributes[t]:(0,i.CX)(e,{...o,jsAttributes:{...o.jsAttributes,[t]:n}}),A(v,r,!0,a||null===n?"session":void 0)(t,n)}function y(){}["setErrorHandler","finished","addToTrace","inlineHit","addRelease"].forEach((e=>g[e]=A(v,e,!0,"api"))),g.addPageAction=A(v,"addPageAction",!0,r.D.pageAction),g.setCurrentRouteName=A(v,"routeName",!0,r.D.spa),g.setPageViewName=function(t,n){if("string"==typeof t)return"/"!==t.charAt(0)&&(t="/"+t),(0,i.OP)(e).customTransaction=(n||"http://custom.transaction")+t,A(v,"setPageViewName",!0)()},g.setCustomAttribute=function(e,t){let n=arguments.length>2&&void 0!==arguments[2]&&arguments[2];if("string"==typeof e){if(["string","number"].includes(typeof t)||null===t)return b(e,t,"setCustomAttribute",n);(0,l.Z)("Failed to execute setCustomAttribute.\nNon-null value must be a string or number type, but a type of <".concat(typeof t,"> was provided."))}else(0,l.Z)("Failed to execute setCustomAttribute.\nName must be a string type, but a type of <".concat(typeof e,"> was provided."))},g.setUserId=function(e){if("string"==typeof e||null===e)return b("enduser.id",e,"setUserId",!0);(0,l.Z)("Failed to execute setUserId.\nNon-null value must be a string type, but a type of <".concat(typeof e,"> was provided."))},g.interaction=function(){return(new y).get()};var w=y.prototype={createTracer:function(e,t){var n={},i=this,o="function"==typeof t;return(0,a.p)(m+"tracer",[(0,s.z)(),e,n],i,r.D.spa,p),function(){if(h.emit((o?"":"no-")+"fn-start",[(0,s.z)(),i,o],n),o)try{return t.apply(this,arguments)}catch(e){throw h.emit("fn-err",[arguments,this,e],n),e}finally{h.emit("fn-end",[(0,s.z)()],n)}}}};function A(e,t,n,i){return function(){return(0,a.p)(f.xS,["API/"+t+"/called"],void 0,r.D.metrics,p),i&&(0,a.p)(e+t,[(0,s.z)(),...arguments],n?null:this,i,p),n?void 0:this}}function x(){n.e(439).then(n.bind(n,7438)).then((t=>{let{setAPI:n}=t;n(e),(0,c.L)(e,"api")})).catch((()=>(0,l.Z)("Downloading runtime APIs failed...")))}return["actionText","setName","setAttribute","save","ignore","onEnd","getContext","end","get"].forEach((e=>{w[e]=A(m,e,void 0,r.D.spa)})),g.noticeError=function(e,t){"string"==typeof e&&(e=new Error(e)),(0,a.p)(f.xS,["API/noticeError/called"],void 0,r.D.metrics,p),(0,a.p)("err",[e,(0,s.z)(),!1,t],void 0,r.D.jserrors,p)},u.il?(0,d.b)((()=>x()),!0):x(),g}(e,m);return(0,g.Qy)(e,_,"api"),(0,g.Qy)(e,x,"exposed"),(0,g.EZ)("activatedFeatures",h.T),_}},3325:(e,t,n)=>{n.d(t,{D:()=>r,p:()=>i});const r={ajax:"ajax",jserrors:"jserrors",metrics:"metrics",pageAction:"page_action",pageViewEvent:"page_view_event",pageViewTiming:"page_view_timing",sessionReplay:"session_replay",sessionTrace:"session_trace",spa:"spa"},i={[r.pageViewEvent]:1,[r.pageViewTiming]:2,[r.metrics]:3,[r.jserrors]:4,[r.ajax]:5,[r.sessionTrace]:6,[r.pageAction]:7,[r.spa]:8,[r.sessionReplay]:9}}},r={};function i(e){var t=r[e];if(void 0!==t)return t.exports;var a=r[e]={exports:{}};return n[e](a,a.exports,i),a.exports}i.m=n,i.d=(e,t)=>{for(var n in t)i.o(t,n)&&!i.o(e,n)&&Object.defineProperty(e,n,{enumerable:!0,get:t[n]})},i.f={},i.e=e=>Promise.all(Object.keys(i.f).reduce(((t,n)=>(i.f[n](e,t),t)),[])),i.u=e=>(({78:"page_action-aggregate",147:"metrics-aggregate",193:"session_trace-aggregate",242:"session-manager",317:"jserrors-aggregate",348:"page_view_timing-aggregate",412:"lazy-feature-loader",439:"async-api",538:"recorder",590:"session_replay-aggregate",675:"compressor",786:"page_view_event-aggregate",873:"spa-aggregate",898:"ajax-aggregate"}[e]||e)+"."+{78:"467f8594",147:"b86cefcf",193:"ac30a1f3",242:"d080e4cc",317:"319b8300",348:"7b2a53ee",412:"c1052c27",439:"e9f77430",538:"9c5c1546",590:"8b420469",646:"9e7a6b8d",675:"9614fd62",786:"4988d952",860:"95a91211",873:"550eec7b",898:"d95c640e"}[e]+"-1.237.1.min.js"),i.o=(e,t)=>Object.prototype.hasOwnProperty.call(e,t),e={},t="NRBA:",i.l=(n,r,a,o)=>{if(e[n])e[n].push(r);else{var s,c;if(void 0!==a)for(var d=document.getElementsByTagName("script"),u=0;u<d.length;u++){var l=d[u];if(l.getAttribute("src")==n||l.getAttribute("data-webpack")==t+a){s=l;break}}s||(c=!0,(s=document.createElement("script")).charset="utf-8",s.timeout=120,i.nc&&s.setAttribute("nonce",i.nc),s.setAttribute("data-webpack",t+a),s.src=n),e[n]=[r];var f=(t,r)=>{s.onerror=s.onload=null,clearTimeout(g);var i=e[n];if(delete e[n],s.parentNode&&s.parentNode.removeChild(s),i&&i.forEach((e=>e(r))),t)return t(r)},g=setTimeout(f.bind(null,void 0,{type:"timeout",target:s}),12e4);s.onerror=f.bind(null,s.onerror),s.onload=f.bind(null,s.onload),c&&document.head.appendChild(s)}},i.r=e=>{"undefined"!=typeof Symbol&&Symbol.toStringTag&&Object.defineProperty(e,Symbol.toStringTag,{value:"Module"}),Object.defineProperty(e,"__esModule",{value:!0})},i.j=4,i.p="https://js-agent.newrelic.com/",(()=>{var e={4:0,465:0};i.f.j=(t,n)=>{var r=i.o(e,t)?e[t]:void 0;if(0!==r)if(r)n.push(r[2]);else{var a=new Promise(((n,i)=>r=e[t]=[n,i]));n.push(r[2]=a);var o=i.p+i.u(t),s=new Error;i.l(o,(n=>{if(i.o(e,t)&&(0!==(r=e[t])&&(e[t]=void 0),r)){var a=n&&("load"===n.type?"missing":n.type),o=n&&n.target&&n.target.src;s.message="Loading chunk "+t+" failed.\n("+a+": "+o+")",s.name="ChunkLoadError",s.type=a,s.request=o,r[1](s)}}),"chunk-"+t,t)}};var t=(t,n)=>{var r,a,[o,s,c]=n,d=0;if(o.some((t=>0!==e[t]))){for(r in s)i.o(s,r)&&(i.m[r]=s[r]);if(c)c(i)}for(t&&t(n);d<o.length;d++)a=o[d],i.o(e,a)&&e[a]&&e[a][0](),e[a]=0},n=window.webpackChunkNRBA=window.webpackChunkNRBA||[];n.forEach(t.bind(null,0)),n.push=t.bind(null,n.push.bind(n))})();var a={};(()=>{i.r(a);var e=i(50);class t{addPageAction(t,n){(0,e.Z)("Call to agent api addPageAction failed. The session trace feature is not currently initialized.")}setPageViewName(t,n){(0,e.Z)("Call to agent api setPageViewName failed. The page view feature is not currently initialized.")}setCustomAttribute(t,n,r){(0,e.Z)("Call to agent api setCustomAttribute failed. The js errors feature is not currently initialized.")}noticeError(t,n){(0,e.Z)("Call to agent api noticeError failed. The js errors feature is not currently initialized.")}setUserId(t){(0,e.Z)("Call to agent api setUserId failed. The js errors feature is not currently initialized.")}setErrorHandler(t){(0,e.Z)("Call to agent api setErrorHandler failed. The js errors feature is not currently initialized.")}finished(t){(0,e.Z)("Call to agent api finished failed. The page action feature is not currently initialized.")}addRelease(t,n){(0,e.Z)("Call to agent api addRelease failed. The agent is not currently initialized.")}}var n=i(3325),r=i(5763);const o=Object.values(n.D);function s(e){const t={};return o.forEach((n=>{t[n]=function(e,t){return!1!==(0,r.Mt)(t,"".concat(e,".enabled"))}(n,e)})),t}var c=i(9144);var d=i(5546),u=i(385),l=i(8e3),f=i(5938),g=i(3960);class p extends f.W{constructor(e,t,n){let r=!(arguments.length>3&&void 0!==arguments[3])||arguments[3];super(e,t,n),this.auto=r,this.abortHandler,this.featAggregate,this.onAggregateImported,r&&(0,l.R)(e,n)}importAggregator(){let t=arguments.length>0&&void 0!==arguments[0]?arguments[0]:{};if(this.featAggregate||!this.auto)return;const n=u.il&&!0===(0,r.Mt)(this.agentIdentifier,"privacy.cookies_enabled");let a;this.onAggregateImported=new Promise((e=>{a=e}));const o=async()=>{let r;try{if(n){const{setupAgentSession:e}=await Promise.all([i.e(860),i.e(242)]).then(i.bind(i,3228));r=e(this.agentIdentifier)}}catch(t){(0,e.Z)("A problem occurred when starting up session manager. This page will not start or extend any session.",t)}try{if(!this.shouldImportAgg(this.featureName,r))return(0,l.L)(this.agentIdentifier,this.featureName),void a(!1);const{lazyFeatureLoader:e}=await i.e(412).then(i.bind(i,8582)),{Aggregate:n}=await e(this.featureName,"aggregate");this.featAggregate=new n(this.agentIdentifier,this.aggregator,t),a(!0)}catch(t){(0,e.Z)("Downloading and initializing ".concat(this.featureName," failed..."),t),this.abortHandler?.(),a(!1)}};u.il?(0,g.b)((()=>o()),!0):o()}shouldImportAgg(e,t){return e!==n.D.sessionReplay||!!r.Yu.MO&&(!1!==(0,r.Mt)(this.agentIdentifier,"session_trace.enabled")&&(!!t?.isNew||!!t?.state.sessionReplay))}}var h=i(7633),v=i(7894);class m extends p{static featureName=h.t9;constructor(e,t){let i=!(arguments.length>2&&void 0!==arguments[2])||arguments[2];if(super(e,t,h.t9,i),("undefined"==typeof PerformanceNavigationTiming||u.Tt)&&"undefined"!=typeof PerformanceTiming){const t=(0,r.OP)(e);t[h.Dz]=Math.max(Date.now()-t.offset,0),(0,g.K)((()=>t[h.qw]=Math.max((0,v.z)()-t[h.Dz],0))),(0,g.b)((()=>{const e=(0,v.z)();t[h.OJ]=Math.max(e-t[h.Dz],0),(0,d.p)("timing",["load",e],void 0,n.D.pageViewTiming,this.ee)}))}this.importAggregator()}}var b=i(1117),y=i(1284);class w extends b.w{constructor(e){super(e),this.aggregatedData={}}store(e,t,n,r,i){var a=this.getBucket(e,t,n,i);return a.metrics=function(e,t){t||(t={count:0});return t.count+=1,(0,y.D)(e,(function(e,n){t[e]=A(n,t[e])})),t}(r,a.metrics),a}merge(e,t,n,r,i){var a=this.getBucket(e,t,r,i);if(a.metrics){var o=a.metrics;o.count+=n.count,(0,y.D)(n,(function(e,t){if("count"!==e){var r=o[e],i=n[e];i&&!i.c?o[e]=A(i.t,r):o[e]=function(e,t){if(!t)return e;t.c||(t=x(t.t));return t.min=Math.min(e.min,t.min),t.max=Math.max(e.max,t.max),t.t+=e.t,t.sos+=e.sos,t.c+=e.c,t}(i,o[e])}}))}else a.metrics=n}storeMetric(e,t,n,r){var i=this.getBucket(e,t,n);return i.stats=A(r,i.stats),i}getBucket(e,t,n,r){this.aggregatedData[e]||(this.aggregatedData[e]={});var i=this.aggregatedData[e][t];return i||(i=this.aggregatedData[e][t]={params:n||{}},r&&(i.custom=r)),i}get(e,t){return t?this.aggregatedData[e]&&this.aggregatedData[e][t]:this.aggregatedData[e]}take(e){for(var t={},n="",r=!1,i=0;i<e.length;i++)t[n=e[i]]=D(this.aggregatedData[n]),t[n].length&&(r=!0),delete this.aggregatedData[n];return r?t:null}}function A(e,t){return null==e?function(e){e?e.c++:e={c:1};return e}(t):t?(t.c||(t=x(t.t)),t.c+=1,t.t+=e,t.sos+=e*e,e>t.max&&(t.max=e),e<t.min&&(t.min=e),t):{t:e}}function x(e){return{t:e,min:e,max:e,sos:e*e,c:1}}function D(e){return"object"!=typeof e?[]:(0,y.D)(e,j)}function j(e,t){return t}var _=i(8632),E=i(4402),T=i(4351);var k=i(7956),N=i(3239),P=i(9251);class C extends p{static featureName=P.t;constructor(e,t){let n=!(arguments.length>2&&void 0!==arguments[2])||arguments[2];super(e,t,P.t,n),u.il&&((0,r.OP)(e).initHidden=Boolean("hidden"===document.visibilityState),(0,k.N)((()=>(0,d.p)("docHidden",[(0,v.z)()],void 0,P.t,this.ee)),!0),(0,N.bP)("pagehide",(()=>(0,d.p)("winPagehide",[(0,v.z)()],void 0,P.t,this.ee))),this.importAggregator())}}var I=i(3081);class S extends p{static featureName=I.t9;constructor(e,t){let n=!(arguments.length>2&&void 0!==arguments[2])||arguments[2];super(e,t,I.t9,n),this.importAggregator()}}new class extends t{constructor(t){let n=arguments.length>1&&void 0!==arguments[1]?arguments[1]:(0,E.ky)(16);super(),u._A?(this.agentIdentifier=n,this.sharedAggregator=new w({agentIdentifier:this.agentIdentifier}),this.features={},this.desiredFeatures=new Set(t.features||[]),this.desiredFeatures.add(m),Object.assign(this,(0,c.j)(this.agentIdentifier,t,t.loaderType||"agent")),this.start()):(0,e.Z)("Failed to initial the agent. Could not determine the runtime environment.")}get config(){return{info:(0,r.C5)(this.agentIdentifier),init:(0,r.P_)(this.agentIdentifier),loader_config:(0,r.DL)(this.agentIdentifier),runtime:(0,r.OP)(this.agentIdentifier)}}start(){const t="features";try{const r=s(this.agentIdentifier),i=[...this.desiredFeatures];i.sort(((e,t)=>n.p[e.featureName]-n.p[t.featureName])),i.forEach((t=>{if(r[t.featureName]||t.featureName===n.D.pageViewEvent){const i=function(e){switch(e){case n.D.ajax:return[n.D.jserrors];case n.D.sessionTrace:return[n.D.ajax,n.D.pageViewEvent];case n.D.sessionReplay:return[n.D.sessionTrace];case n.D.pageViewTiming:return[n.D.pageViewEvent];default:return[]}}(t.featureName);i.every((e=>r[e]))||(0,e.Z)("".concat(t.featureName," is enabled but one or more dependent features has been disabled (").concat((0,T.P)(i),"). This may cause unintended consequences or missing data...")),this.features[t.featureName]=new t(this.agentIdentifier,this.sharedAggregator)}})),(0,_.Qy)(this.agentIdentifier,this.features,t)}catch(n){(0,e.Z)("Failed to initialize all enabled instrument classes (agent aborted) -",n);for(const e in this.features)this.features[e].abortHandler?.();const r=(0,_.fP)();return delete r.initializedAgents[this.agentIdentifier]?.api,delete r.initializedAgents[this.agentIdentifier]?.[t],delete this.sharedAggregator,r.ee?.abort(),delete r.ee?.get(this.agentIdentifier),!1}}addToTrace(t){(0,e.Z)("Call to agent api addToTrace failed. The page action feature is not currently initialized.")}setCurrentRouteName(t){(0,e.Z)("Call to agent api setCurrentRouteName failed. The spa feature is not currently initialized.")}interaction(){(0,e.Z)("Call to agent api interaction failed. The spa feature is not currently initialized.")}}({features:[m,C,S],loaderType:"lite"})})(),window.NRBA=a})();</script><link rel="shortcut icon" href="/favicon.ico" type="image/x-icon">
    	<link rel="stylesheet" href="/cpopg/softheme/src/css/app.css?v=2.8.34-30">
    	<link rel="stylesheet" href="/cpopg/softheme/src/fonts/saj/styles.css?v=2.8.34-30">
    	<link rel="stylesheet" href="/cpopg/css/formulario.css?v=2.8.34-30" type="text/css">


    	<link rel="stylesheet" href="/cpopg/webjars/select2/3.5.4/select2.css?v=2.8.34-30" type="text/css">
    	<link rel="stylesheet" href="/cpopg/webjars/select2/3.5.4/select2-bootstrap.css?v=2.8.34-30" type="text/css">
    	<link rel="stylesheet" href="/cpopg/css/saj/select2/saj-select2.css">



    <script>
    	window.saj = window.saj || {};
    	window.saj.env = window.saj.env || {};
    	window.saj.env.root = '/cpopg';
    	window.saj.env.css = '/cpopg/css';
    	window.saj.env.js = '/cpopg/js';
    	window.saj.env.imagens = '/cpopg/imagens';
    	window.saj.env.queryString = 'processo.codigo=01000O7550000&processo.foro=1&processo.numero=0710802-55.2018.8.02.0001';

    	window.saj.cpo = window.saj.cpo || {};

    	// transfere variavel se cpo esta rodando para totem
    	window.saj.cpo.totem = 'false' == 'true';
    </script>


    	<script language="javascript" type="text/JavaScript" src="/cpopg/js/jquery/jquery.min.js?n=1620728708"></script>
    	<script language="javascript" type="text/JavaScript" src="/cpopg/js/jquery/jquery.func_toggle.js?n=c2c8610b-52c9-45ee-9fc6-21b144a3c821"></script>
    	<script language="javascript" type="text/javascript" src="/cpopg/js/jquery/jquery.blockUI.min.js?n=1824ccde-856e-4d5e-9ada-0c2b59d80a40"></script>
    	<script language="javascript" type="text/javascript" src="/cpopg/js/jquery/jquery.browser.min.js?n=a997f8f5-e934-4124-a7bb-2c7ee532bc68"></script>

    	<script language="javascript" type="text/javascript" src="/cpopg/webjars/lodash/4.17.5/lodash.js?n=72ac9a6d-51ec-4a08-b24c-8eb98aa92f0f"></script>
    	<script language="javascript" type="text/JavaScript" src="/cpopg/js/select2/select2.js?n=b5cbb428-1ac9-4dd8-8be5-2a2463b86430"></script>
    	<script language="javascript" type="text/JavaScript" src="/cpopg/webjars/select2/3.5.4/select2_locale_pt-BR.js?n=8259a0f4-cd76-47d9-95e4-74d643b12c87"></script>
    	<script language="javascript" type="text/JavaScript" src="/cpopg/js/saj/saj-select2.js?n=9b2e9dcc-a470-4c79-878d-83262cf69732"></script>

    	<script language="javascript" type="text/JavaScript" src="/cpopg/js/saj/saj-web-2.2.41-4.js?n=6dfe84d1-0cea-4cf0-bb96-58d06c2f5a0c"></script>
    	<script language="javascript" type="text/JavaScript" src="/cpopg/js/saj/saj-tooltip.js?n=8a362267-a276-408f-a476-2044cbf5c9ed"></script>
    	<script language="javascript" type="text/JavaScript" src="/cpopg/js/saj/saj-popup-modal-1.0.0-1.js?n=d6d20152-8a37-4cb4-8642-df77ae1fcff0"></script>
    	<script language="javascript" type="text/JavaScript" src="/cpopg/js/saj/saj-browser.js?n=58716b24-5047-440e-a7de-d56b20030dbf"></script>
    	<script language="javascript" type="text/JavaScript" src="/cpopg/js/saj/saj-mascara-input.js?n=bd309ca6-2d81-4b66-9df6-d99d43d185af"></script>
    	<script language="javascript" type="text/JavaScript" src="/cpopg/js/saj/saj-numeroProcesso.js?n=0f99e063-1f52-4204-b4c6-598c28f7a922"></script>
    	<script language="javascript" type="text/JavaScript" src="/cpopg/js/saj-cpo-cbpesquisa.js?n=686458821"></script>
    	<script language="javascript" type="text/JavaScript" src="/cpopg/js/saj/acessibilidade/acessibilidade.js?n=cb321e98-4d3c-4666-ab36-3d63c47c3e2e"></script>

    	<script language="javascript" type="text/JavaScript" src="/cpopg/softheme/src/js/app.js?n=789536343"></script>
    	<script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.12.3/umd/popper.min.js?n=cadd3826-5932-4f7a-898c-c41b4efb5114" integrity="sha384-vFJXuSJphROIrBnz7yo7oB41mKfc8JzQZiCq4NCceLEaO4IHwicKwpJf9c9IpFgh" crossorigin="anonymous"></script>
    	<script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0-beta.2/js/bootstrap.min.js?n=1791337263" integrity="sha384-alpBpkh1PFOepccYVYDB4do5UnbKysX5WZXm3XxPqe5iKTfUKjNkCk9SaVuEZflJ" crossorigin="anonymous"></script>






    <script>
    	(function($){
    		$(function(){
    			var intervalo = 1795000;
    			$.saj.manterSessao('/cpopg/manterSessao.do', intervalo);
    		});

    	})(jQuery);
    </script>





        <script language="javascript" type="text/JavaScript">
            $.saj = $.saj || {};
            $.saj.acessoRecurso = {
                abrirPastaDigitalEmPopup: 'true' == 'true',
                idRecursoQueProvocouLiberacaoPorSenha: '',
                popupSenha: {
                    mostrar: 'false' == 'true',
                    titulo: 'Senha do processo',
                    altura: 220 + Number("10"),
                    alturaAdicionalParaMensagemValidacao: Number("0"),
                    largura: 580
                }
            };

            $.saj.getUrlParameter = function getUrlParameter(sParam) {
                var sPageURL = decodeURIComponent(window.location.search.substring(1)), sURLVariables = sPageURL.split('&'), sParameterName, i;
                for (i = 0; i < sURLVariables.length; i++) {
                    sParameterName = sURLVariables[i].split('=');
                    if (sParameterName[0] === sParam) {
                        return sParameterName[1] === undefined ? true : sParameterName[1];
                    }
                }
            };
        </script>
        <script language="javascript" type="text/JavaScript" src="/cpopg/jsp/show-2.8.33-0.js?n=1155165209"></script>

    	<script type="text/javascript">
    		(function($) {
    			$(function(){
    				// Correção temporária do alinhamento do divisor de seção de formulário do SPW
    				$('td[background$="spw/fundo_subtitulo2.gif"]').attr('valign', 'top');


    			})
    		})(jQuery);
    	</script>



































    </head>

    <body>





































    <script type="text/javascript">
        (function ($) {
            $(function () {
                var captcha = $.saj.getUrlParameter('uuidCaptcha');

                if (!captcha) {
                    return;
                }

                if(!captcha){
                    return;
                }
                var $processoPrinc = $('.processoPrinc');
                $processoPrinc.attr('href', $processoPrinc.attr('href') + '&uuidCaptcha=' + captcha);

                var $processoPaiApenso = $('.processoPaiApenso');
                $processoPaiApenso.attr('href', $processoPaiApenso.attr('href') + '&uuidCaptcha=' + captcha);

                $('.incidente').each(function () {
                    var $incidente = $(this);
                    var url = $incidente.attr('href');
                    $incidente.attr('href', url + '&uuidCaptcha=' + captcha);
                });

            })
        })(jQuery);
    </script>

    <!-- HEADER-->
    <div class="unj-entity-header">





    <div class="unj-entity-header__actions">
        <div class="container">
            <div class="row">
                <div class="col-3 col-md-4">
                    <a href="javascript:history.back();" class="unj-link-back">
                        <i id="setaVoltar" class="icon-back"></i>
                    </a>
                </div>
                <div class="col-13 col-md-12 unj-ta-r">
                    <!-- CDAS -->

                    <!-- Custas -->

                        <button class="btn btn-secondary btn-space linkConsultaSG" onclick="location.href = 'https://www2.tjal.jus.br/ccpweb/abrirConsultaCustas.do?cdProcesso=01000O7550000&amp;nuProcesso=0710802-55.2018.8.02.0001', '_blank', 'toolbar=0,location=0,menubar=0'">
                            Visualizar custas
                        </button>

                    <!-- Pasta digital -->










                                <a class="linkPasta btn btn-secondary btn-space" id="linkPasta" aria-hidden="true" title="Pasta digital" href="#liberarAutoPorSenha">
                                    Visualizar autos
                                </a>
                                <!-- link da pasta digital exibido somente para leitores de tela (deficientes visuais), neste caso o link anterior é ignorado pelo leitor
                                Obs: necessário manter a table devido aos atributos de acessibilidade se comportarem adequadamente com a tabela, comportamento que não é possível colocando
                                os atributos somente na tag do link-->
                                <a class="linkPasta btn btn-secondary btn-space" id="linkPastaAcessibilidade" style="font-size:0;height:0;width:0;padding:0;margin:0;border:none" href="#liberarAutoPorSenha&amp;acessibilidade=true">
                                    Visualizar autos
                                </a>






                            <!-- Peticionar -->




                </div>
            </div>
        </div>
    </div>









    <div class="unj-entity-header__summary">
        <div id="containerDadosPrincipaisProcesso" class="container">
            <div class="row">
                <div class="col-lg-12 col-xl-13">
                    <!--principal -->

                        <span id="numeroProcesso" class="unj-larger-1">
                            0710802-55.2018.8.02.0001
                        </span>


                            <span id="labelSituacaoProcesso" class="unj-tag">Julgado Transitado</span>




                    <!-- incidente -->



                        <span class="unj-tag">Há custas pendentes</span>

                </div>

            </div>
            <div class="row">

                    <div class="col-lg-3 col-xl-3 mb-3">
                        <span id="labelClasseProcesso" class="unj-label">Classe</span>
                        <div class="lh-1-1 line-clamp__2"><span id="classeProcesso" title="Procedimento Comum Cível">Procedimento Comum Cível</span></div>
                    </div>


                    <div class="col-lg-2 col-xl-3 mb-3">
                        <span id="labelAssuntoProcesso" class="unj-label">
                            Assunto
                        </span>
                        <div class="lh-1-1 line-clamp__2"> <span id="assuntoProcesso" title="Dano Material">Dano Material</span></div>
                    </div>


                    <div class="col-lg-2 col-xl-2 mb-2">
                        <span id="labelForoProcesso" class="unj-label">
                            Foro
                        </span>
                        <div class="lh-1-1 line-clamp__2"> <span id="foroProcesso" title="Foro de Maceió">Foro de Maceió</span></div>
                    </div>


                    <div class="col-lg-3 col-xl-2 mb-2">
                        <span id="labelVaraProcesso" class="unj-label">
                            Vara
                        </span>
                        <div class="lh-1-1 line-clamp__2"><span id="varaProcesso" title="4ª Vara Cível da Capital">4ª Vara Cível da Capital</span></div>
                    </div>



                    <div class="col-lg-3 mb-2">
                        <span id="labelJuizProcesso" class="unj-label">Juiz</span>
                        <div class="line-clamp__2"> <span id="juizProcesso" title="José Cícero Alves da Silva">José Cícero Alves da Silva</span> </div>
                    </div>


                <!-- Processo principal -->



            </div>
        </div>
    </div>






    <div class="unj-entity-header__details">
        <div class="container">
            <div class="unj-ta-r">

                    <a href="#maisDetalhes" class="unj-link-collapse" data-toggle="collapse" aria-expanded="false" aria-controls="maisDetalhes">
                        <span class="unj-link-collapse__show">
                            <i id="botaoExpandirDadosSecundarios" class="unj-link-collapse__icon glyph glyph-chevron-down"></i>
                            Mais
                        </span>
                        <span class="unj-link-collapse__hide">
                            <i id="botaoRecolherDadosSecundarios" class="unj-link-collapse__icon glyph glyph-chevron-up"></i>
                            Recolher
                        </span>
                    </a>

            </div>
            <div id="maisDetalhes" class="collapse" aria-expanded="false">
                <div class="row unj-row--border-top">

                        <div class="col-lg-3 mb-2">
                            <span id="labelDistribuicaoProcesso" class="unj-label">Distribuição </span>
                            <div id="dataHoraDistribuicaoProcesso">02/05/2018 às 19:01 - Sorteio</div>
                        </div>



                        <div class="col-lg-3 mb-2">
                            <span id="labelControleProcesso" class="unj-label">Controle</span>
                            <div id="numeroControleProcesso">2018/000520</div>
                        </div>


                        <div class="col-lg-2 col-xl-2 mb-2">
                            <span id="labelAreaProcesso" class="unj-label">Área</span>
                            <div id="areaProcesso" class="lh-1-1 line-clamp__2"> <span title="Cível">Cível</span></div>
                        </div>


                        <div class="col-lg-2 mb-2">
                            <span id="lavelValorAcaoProcesso" class="unj-label">Valor da ação</span>
                            <div id="valorAcaoProcesso">R$         281.178,42</div>
                        </div>




                        <div class="col-lg-2 mb-2">
                            <span class="unj-label">Outros assuntos</span>
                            <div class="line-clamp__2"> <span title="Dano Moral">Dano Moral</span></div>
                        </div>



                </div>
            </div>

        </div>
    </div>

    </div>


    <div class="div-conteudo container mb-90">





























    <aside class="aside-nav aside-nav--left">
        <div class="aside-nav__inner">
            <header class="aside-nav__main-menu__header"><span class="aside-nav__main-menu__header__text">  Menu e-SAJ</span>
                <a href="#" class="aside-nav__user__close-button close-offcanvas">
                    <img src="https://www2.tjal.jus.br/esaj/img/icons/icon-close--light.png" alt="">
                </a>
            </header>
            <nav class="aside-nav__main-menu">
                <ul class="aside-nav__main-menu__list" id="conteudoMenuEsaj"><li class="aside-nav__main-menu__list__item has__menu__children"><a href="#" class="aside-nav__main-menu__list__item__link">Consultas</a>
    <ul class="aside-nav__main-menu__list__item menu__children"><li class="aside-nav__main-menu__list__item"><a href="https://www2.tjal.jus.br/cpopg/open.do" class="aside-nav__main-menu__list__item__link">Processos de 1º Grau</a>
    </li>
    <li class="aside-nav__main-menu__list__item has__menu__children"><a href="#" class="aside-nav__main-menu__list__item__link">Ordem de Processos</a>
    <ul class="aside-nav__main-menu__list__item menu__children"><li class="aside-nav__main-menu__list__item"><a href="https://www2.tjal.jus.br/cop/abrirConsultaDeOrdemDeJulgamentoPg.do" class="aside-nav__main-menu__list__item__link">Julgamento do 1º Grau</a>
    </li>
    <li class="aside-nav__main-menu__list__item"><a href="https://www2.tjal.jus.br/cop/abrirConsultaDeOrdemDeAtoPg.do" class="aside-nav__main-menu__list__item__link">Publicação e Cumprimento de Atos de 1º Grau</a>
    </li>
    </ul></li>
    <li class="aside-nav__main-menu__list__item"><a href="https://www2.tjal.jus.br/cposg5/open.do" class="aside-nav__main-menu__list__item__link">Processos de 2º Grau</a>
    </li>
    </ul></li>
    <li class="aside-nav__main-menu__list__item has__menu__children"><a href="#" class="aside-nav__main-menu__list__item__link">Recolhimento de Custas</a>
    <ul class="aside-nav__main-menu__list__item menu__children"><li class="aside-nav__main-menu__list__item has__menu__children"><a href="#" class="aside-nav__main-menu__list__item__link">Custas de 1º Grau</a>
    <ul class="aside-nav__main-menu__list__item menu__children"><li class="aside-nav__main-menu__list__item"><a href="https://www2.tjal.jus.br/ccpweb/abrirConsultaCustas.do" class="aside-nav__main-menu__list__item__link">Consulta de Custas de 1º Grau</a>
    </li>
    <li class="aside-nav__main-menu__list__item"><a href="https://www2.tjal.jus.br/ccpweb/iniciarCalculoDeCustas.do?cdTipoCusta=1&amp;flTipoCusta=0&amp;cdServicoCalculoCusta=690003" class="aside-nav__main-menu__list__item__link">Custas Iniciais de 1º Grau</a>
    </li>
    <li class="aside-nav__main-menu__list__item"><a href="https://www2.tjal.jus.br/ccpweb/iniciarCalculoDeCustas.do?cdTipoCusta=15&amp;flTipoCusta=5&amp;cdServicoCalculoCusta=690004" class="aside-nav__main-menu__list__item__link">Atos Avulsos de 1º Grau</a>
    </li>
    <li class="aside-nav__main-menu__list__item"><a href="https://www2.tjal.jus.br/ccpweb/iniciarCalculoDeCustas.do?cdTipoCusta=10&amp;flTipoCusta=1&amp;cdServicoCalculoCusta=690005" class="aside-nav__main-menu__list__item__link">Custas de Preparo de 1º Grau</a>
    </li>
    <li class="aside-nav__main-menu__list__item"><a href="https://www2.tjal.jus.br/ccpweb/iniciarCalculoDeCustas.do?cdTipoCusta=14&amp;flTipoCusta=0&amp;cdServicoCalculoCusta=690006" class="aside-nav__main-menu__list__item__link">Custas Juizado Especial - Recurso Inominado</a>
    </li>
    <li class="aside-nav__main-menu__list__item"><a href="https://www2.tjal.jus.br/ccpweb/iniciarCalculoDeCustas.do?cdTipoCusta=3&amp;flTipoCusta=1&amp;cdServicoCalculoCusta=690009" class="aside-nav__main-menu__list__item__link">Custas Intermediárias de 1º Grau</a>
    </li>
    </ul></li>
    <li class="aside-nav__main-menu__list__item has__menu__children"><a href="#" class="aside-nav__main-menu__list__item__link">Custas de 2º Grau</a>
    <ul class="aside-nav__main-menu__list__item menu__children"><li class="aside-nav__main-menu__list__item"><a href="https://www2.tjal.jus.br/ccpweb/abrirConsultaCustasSg.do" class="aside-nav__main-menu__list__item__link">Consulta de Custas de 2º Grau</a>
    </li>
    <li class="aside-nav__main-menu__list__item"><a href="https://www2.tjal.jus.br/ccpweb/iniciarCalculoDeCustasSg.do?cdServicoCalculoCusta=690205&amp;flTipoCusta=0&amp;cdTipoCusta=1" class="aside-nav__main-menu__list__item__link">Custas iniciais de 2º Grau</a>
    </li>
    </ul></li>
    </ul></li>
    <li class="aside-nav__main-menu__list__item has__menu__children"><a href="#" class="aside-nav__main-menu__list__item__link">Jurisprudência</a>
    <ul class="aside-nav__main-menu__list__item menu__children"><li class="aside-nav__main-menu__list__item"><a href="https://www2.tjal.jus.br/cjsg/consultaSimples.do" class="aside-nav__main-menu__list__item__link">Simples</a>
    </li>
    <li class="aside-nav__main-menu__list__item"><a href="https://www2.tjal.jus.br/cjsg/consultaCompleta.do" class="aside-nav__main-menu__list__item__link">Completa</a>
    </li>
    </ul></li>
    <li class="aside-nav__main-menu__list__item"><a href="https://www2.tjal.jus.br/cdje" class="aside-nav__main-menu__list__item__link">Diário da Justiça Eletrônico</a>
    </li>
    <li class="aside-nav__main-menu__list__item has__menu__children"><a href="#" class="aside-nav__main-menu__list__item__link">Push</a>
    <ul class="aside-nav__main-menu__list__item menu__children"><li class="aside-nav__main-menu__list__item"><a href="https://www2.tjal.jus.br/pushpg" class="aside-nav__main-menu__list__item__link">1º Grau</a>
    </li>
    <li class="aside-nav__main-menu__list__item"><a href="https://www2.tjal.jus.br/pushsg5" class="aside-nav__main-menu__list__item__link">2º Grau</a>
    </li>
    </ul></li>
    <li class="aside-nav__main-menu__list__item has__menu__children"><a href="#" class="aside-nav__main-menu__list__item__link">Pauta de Julgamento</a>
    <ul class="aside-nav__main-menu__list__item menu__children"><li class="aside-nav__main-menu__list__item"><a href="https://www2.tjal.jus.br/pauta-julgamento/consulta" class="aside-nav__main-menu__list__item__link">Consulta da Pauta de Julgamento</a>
    </li>
    </ul></li>
    <li class="aside-nav__main-menu__list__item has__menu__children"><a href="#" class="aside-nav__main-menu__list__item__link">Certidões</a>
    <ul class="aside-nav__main-menu__list__item menu__children"><li class="aside-nav__main-menu__list__item has__menu__children"><a href="#" class="aside-nav__main-menu__list__item__link">Certidões de 1º grau</a>
    <ul class="aside-nav__main-menu__list__item menu__children"><li class="aside-nav__main-menu__list__item"><a href="https://www2.tjal.jus.br/sco/abrirCadastro.do" class="aside-nav__main-menu__list__item__link">Pedido de Certidão de 1º Grau</a>
    </li>
    <li class="aside-nav__main-menu__list__item"><a href="https://www2.tjal.jus.br/sco/abrirConferencia.do" class="aside-nav__main-menu__list__item__link">Conferência de Certidão de 1º Grau</a>
    </li>
    <li class="aside-nav__main-menu__list__item"><a href="https://www2.tjal.jus.br/sco/abrirDownload.do" class="aside-nav__main-menu__list__item__link">Baixar Certidão de 1º Grau</a>
    </li>
    </ul></li>
    </ul></li>
    <li class="aside-nav__main-menu__list__item has__menu__children"><a href="#" class="aside-nav__main-menu__list__item__link">Conferência de Documentos</a>
    <ul class="aside-nav__main-menu__list__item menu__children"><li class="aside-nav__main-menu__list__item"><a href="https://www2.tjal.jus.br/pastadigital/pg/abrirConferenciaDocumento.do" class="aside-nav__main-menu__list__item__link">Documento Digital do 1º Grau</a>
    </li>
    <li class="aside-nav__main-menu__list__item"><a href="https://www2.tjal.jus.br/pastadigital/sg/abrirConferenciaDocumento.do" class="aside-nav__main-menu__list__item__link">Documento Digital do 2º Grau</a>
    </li>
    </ul></li>
    <li class="aside-nav__main-menu__list__item has__menu__children"><a href="#" class="aside-nav__main-menu__list__item__link">Intimação e Citação Eletrônica</a>
    <ul class="aside-nav__main-menu__list__item menu__children"><li class="aside-nav__main-menu__list__item"><a href="https://www2.tjal.jus.br/intimacoesweb/abrirConsultaAtosRecebidos.do" class="aside-nav__main-menu__list__item__link">Consulta de Recebidas</a>
    </li>
    <li class="aside-nav__main-menu__list__item"><a href="https://www2.tjal.jus.br/intimacoesweb/abrirConsultaAtosNaoRecebidos.do" class="aside-nav__main-menu__list__item__link">Recebimento</a>
    </li>
    </ul></li>
    <li class="aside-nav__main-menu__list__item has__menu__children"><a href="#" class="aside-nav__main-menu__list__item__link">Peticionamento Eletrônico</a>
    <ul class="aside-nav__main-menu__list__item menu__children"><li class="aside-nav__main-menu__list__item has__menu__children"><a href="#" class="aside-nav__main-menu__list__item__link">Peticionamento Eletrônico de 1º Grau</a>
    <ul class="aside-nav__main-menu__list__item menu__children"><li class="aside-nav__main-menu__list__item"><a href="https://www2.tjal.jus.br/petpg/abrirNovaPeticaoInicial.do?instancia=PG" class="aside-nav__main-menu__list__item__link">Peticionamento Inicial de 1º Grau</a>
    </li>
    <li class="aside-nav__main-menu__list__item"><a href="https://www2.tjal.jus.br/petpg/abrirNovaPeticaoIntermediaria.do?instancia=PG" class="aside-nav__main-menu__list__item__link">Peticionamento Intermediário de 1º Grau</a>
    </li>
    <li class="aside-nav__main-menu__list__item"><a href="https://www2.tjal.jus.br/petpg/abrirConsultaPeticoes.do" class="aside-nav__main-menu__list__item__link">Consulta de Petições de 1º Grau</a>
    </li>
    </ul></li>
    <li class="aside-nav__main-menu__list__item has__menu__children"><a href="#" class="aside-nav__main-menu__list__item__link">Peticionamento Eletrônico de 2º Grau</a>
    <ul class="aside-nav__main-menu__list__item menu__children"><li class="aside-nav__main-menu__list__item"><a href="https://www2.tjal.jus.br/petsg/abrirNovaPeticaoInicial.do?instancia=SG" class="aside-nav__main-menu__list__item__link">Peticionamento Inicial de 2º Grau</a>
    </li>
    <li class="aside-nav__main-menu__list__item"><a href="https://www2.tjal.jus.br/petsg/abrirNovaPeticaoIntermediaria.do?instancia=SG" class="aside-nav__main-menu__list__item__link">Peticionamento Intermediário de 2º Grau</a>
    </li>
    <li class="aside-nav__main-menu__list__item"><a href="https://www2.tjal.jus.br/petsg/abrirConsultaPeticoes.do" class="aside-nav__main-menu__list__item__link">Consulta de Petições de 2º Grau</a>
    </li>
    </ul></li>
    <li class="aside-nav__main-menu__list__item has__menu__children"><a href="#" class="aside-nav__main-menu__list__item__link">Peticionamento Eletrônico de Turmas Recursais / Plantão (2º Grau)/ Precatórios</a>
    <ul class="aside-nav__main-menu__list__item menu__children"><li class="aside-nav__main-menu__list__item"><a href="https://www2.tjal.jus.br/petcr/abrirNovaPeticaoInicial.do?instancia=CR" class="aside-nav__main-menu__list__item__link">Peticionamento Inicial - TR/ Plantão TJ/ Precat.</a>
    </li>
    <li class="aside-nav__main-menu__list__item"><a href="https://www2.tjal.jus.br/petcr/abrirNovaPeticaoIntermediaria.do?instancia=CR" class="aside-nav__main-menu__list__item__link">Peticionamento Intermediário - TR/ Plantão TJ/ Precat.</a>
    </li>
    <li class="aside-nav__main-menu__list__item"><a href="https://www2.tjal.jus.br/petcr/abrirConsultaPeticoes.do" class="aside-nav__main-menu__list__item__link">Consulta de Petições - TR/ Plantão TJ/ Precat.</a>
    </li>
    </ul></li>
    </ul></li></ul>
            </nav>
            <div id="esaj-beta-switcher-placeholder"></div>
        </div>
    </aside>
    <aside class="aside-nav aside-nav--right aside-nav__user">
        <div class="aside-nav__inner">
            <div class="aside-nav__user__sign">
                <div class="aside-nav__user__sign__brand">
                    <img src="https://www2.tjal.jus.br/esaj/img/aside/brasoes/br-tjal.jpg" alt="">
                </div>
                <ul class="aside-nav__user__sign__list">
                    <li><span class="aside-nav__user__sign__place">Tribunal de Justiça do Estado de Alagoas</span></li>
                </ul>
                <a href="#" class="aside-nav__user__close-button close-offcanvas">
                    <img src="https://www2.tjal.jus.br/esaj/img/icons/icon-close--dark.png" alt="">
                </a>
            </div>
            <hr>
            <div class="aside-nav__user__info">
                <h4 class="aside-nav__user__title">Minha conta</h4>
                <ul class="aside-nav__user__info__list">
                    <li class="aside-nav__user__info__list__item"><span class="aside-nav__user__info__name" id="menuNmUsuarioLogado"></span></li>
                    <li class="aside-nav__user__info__list__item"><span class="aside-nav__user__info__oab" id="menuUsuarioOabs">OAB: </span></li>
                </ul>
                <ul class="aside-nav__user__info__list-access">
                    <li class="aside-nav__user__info__list-access__item"><a class="aside-nav__user__info__list-access__item__link" href="https://www2.tjal.jus.br/esaj/cadastro.do">Meu perfil</a></li>

                        <li class="aside-nav__user__info__list-access__item"><a class="aside-nav__user__info__list-access__item__link" href="https://www2.tjal.jus.br/caixapostal">Caixa Postal</a></li>

                    <li class="aside-nav__user__info__list-access__item"><a class="aside-nav__user__info__list-access__item__link" id="logoutLink" href="#">Sair</a></li>
                </ul>
            </div>
        </div>
    </aside>
    <header>
        <link rel="shortcut icon" href="https://www2.tjal.jus.br/esaj/tema/padrao/clientes/AL/imagens/favicon.ico" type="image/x-icon">
        <link href="https://www2.tjal.jus.br/esaj/app.css" rel="stylesheet" type="text/css">
        <nav class="header__navbar">
            <a class="header__navbar__menu-hamburger open__aside-nav--left navbar-menu-hamburger__item__link">
                <span class="menu-hamburger__alert" style="display:none;"></span>
                <span class="glyph glyph-hamburger"></span>
            </a>

            <h1 class="header__navbar__title" href=""><a class="linkLogo" href="https://www2.tjal.jus.br/esaj/redirecionarNovoEsaj.do"><strong>e-SAJ</strong></a> | Consulta de Processos de 1º Grau</h1>

            <ul class="header__navbar__menu header__navbar__menu--right">
                <li class="header__navbar__menu__item header__navbar__menu__item--initials">
                    <a class="header__navbar__brand__initials" href="http://www.tjal.jus.br"> TJAL </a>
                </li>
                <li class="header__navbar__menu__item header__navbar__menu__item--user">
                   <span class="header__navbar__name open__aside-nav--right">
                         <span id="headerNmUsuarioLogado" class="header__navbar__name__text">Identificar-se </span>
                         <span class="glyph glyph-contact header__navbar__name__icon"></span>
                   </span>
                </li>
            </ul>
        </nav>
    </header>
    <div class="offcanvas-backdrop"></div>


    <script>
        var dict = {
            'certificado.tituloCertificadoDigital': 'Certificado digital',
            'certificado.msgCarregandoCertificado': 'Carregando certificados...',
            'certificado.msgNenhumCertificadoEncontrado': 'Nenhum certificado encontrado',
            'certificado.msgErroCarregarCertificado': 'Erro ao carregar certificados',
            'certificado.msgCertificadoExpirado': '[Expirado]',
            'certificado.msgCertificadoNaoValido': '[Ainda não válido]',
            'certificado.msgCertificadoNaoIcpBrasil': '[Não ICP-Brasil]',
            'certificado.tituloProblemasAoAssinar': 'Falha de comunicação com o dispositivo de assinatura digital',

            'label.contato': 'Contato',
            'label.identificarSe': 'Identificar-se ',

            'mensagem.aguarde': 'Por favor, aguarde.',
            'mensagem.paginaNaoCarregada': 'Não foi possível carregar a página.',
            'mensagem.marcarLido': 'Marcar como lido',
            'mensagem.registrosSelecionados': 'Registros selecionados',
            'mensagem.registroJaSelecionado': 'Este registro já está selecionado',

            'mensagem.data.invalida': 'A data digitada é inválida.',
            'mensagem.data.anoInvalido': 'O ano informado deve ser maior que',
            'mensagem.data.mesInvalido': 'O mês não pode ser maior que 12.',
            'mensagem.data.mes': 'O mês',
            'mensagem.data.mesMaior29dias': 'não pode ter mais que 29 dias.',
            'mensagem.data.mesMaior28dias': 'não pode ter mais que 28 dias.',
            'mensagem.data.mesMaior31dias': 'não pode ter mais que 31 dias.',
            'mensagem.data.mesMaior30dias': 'não pode ter mais que 30 dias.',

            'mensagem.email.invalido': 'O formato do endereço de e-mail não é válido. Verifique se ele tem o formato "usuario@dominio".',
            'mensagem.email.caracteresInvalidos': 'O endereço de e-mail possui caracteres inválidos',
            'mensagem.email.usuarioInvalido': 'O formato do usuário informado no endereço de e-mail não é válido.',
            'mensagem.email.ipInvalido': 'O endereço IP informado no endereço de e-mail não é válido.',
            'mensagem.email.dominioInvalido': 'O formato do domínio informado no endereço de e-mail não é válido.',
            'mensagem.email.dominioIncompleto': 'O domínio informado no endereço de e-mail deve possuir pelo menos duas partes. Por exemplo: "usuario@empresa.com.br".',

            'mensagem.texto.tamanhoInvalido': 'O tamanho do texto digitado é maior do que o tamanho permitido. Tamanho permitido:',
            'mensagem.texto.caracter': 'O caracter',
            'mensagem.texto.caracterPosicaoInvalida': 'não está permitido na posição',

            'mensagem.numero.numeroInvalido': 'O valor digitado não é um número válido.',
            'mensagem.numero.numeroNaoPodeCasasDecimais': 'O número não pode conter casas decimais',
            'mensagem.numero.numeroCasaDecimaisInvalidas': 'O número de casas decimais é inválido. O número pode conter apenas',
            'mensagem.numero.casaDecimais': 'casas decimais',
            'mensagem.numero.numeroInteiroInvalido': 'O número de dígitos inteiros é inválido. O número pode conter apenas',
            'mensagem.numero.digitosInteiros': 'dígitos inteiros',
            'mensagem.numero.numeroTamanhoInvalido': 'O número digitado não pode ser maior que',
            'mensagem.numero.numeroZeroInvalido': 'O número digitado deve ser diferente de zero.'
        }
    </script>



    <script>
        var appEsajLayout = appEsajLayout || {};
        appEsajLayout.urlNovoMenuHtml = 'https://www2.tjal.jus.br/esaj/menuPortalV2Html.do?servico=190101';

        var appEsajCas = appEsajCas || {};
        appEsajCas.urlServicoConteudoIdentificacao = 'https://www2.tjal.jus.br/sajcas/conteudoIdentificacaoJson?script=1691218965774&retorno=' + encodeURIComponent(location.href);
    </script>
    <script src="https://www2.tjal.jus.br/esaj/js/portalV2-bundle.js?n=806192629"></script>

    <script src="https://www2.tjal.jus.br/sajcas/seletorVersaoBeta.js?n=cf11148e-e81a-405e-9a9a-d6579880c0c7&amp;versao=2"></script>

















































































    <div style="padding-top: 10px;">




    			<h2 class="subtitle tituloDoBloco">Partes do processo</h2>


    </div>

    <!--  cabecalho da tabela de lista (partes) -->


    <!--  dados da lista partes principais (partes) -->
    <table id="tablePartesPrincipais" style="margin-left:15px; margin-top:1px;" align="center" border="0" cellpadding="0" cellspacing="0" width="98%">











    <tbody><tr class="fundoClaro">
    	<td valign="top" width="141" style="padding-bottom: 5px" class="label">
    		<span class="mensagemExibindo tipoDeParticipacao">Autor&nbsp;</span>
    	</td>
    	<td class="nomeParteEAdvogado" width="*" align="left" style="padding-bottom: 5px">




    					José Carlos Cerqueira Souza Filho







    				<br>
    				<span class="mensagemExibindo">Advogado:&nbsp;</span>



    						Vinicius Faria de Cerqueira

    				&nbsp;




    	</td>
    </tr>












    <tr class="fundoClaro">
    	<td valign="top" width="141" style="padding-bottom: 5px" class="label">
    		<span class="mensagemExibindo tipoDeParticipacao">Ré&nbsp;</span>
    	</td>
    	<td class="nomeParteEAdvogado" width="*" align="left" style="padding-bottom: 5px">




    					Cony Engenharia Ltda.







    				<br>
    				<span class="mensagemExibindo">Advogado:&nbsp;</span>



    						Carlos Henrique de Mendonça Brandão

    				&nbsp;


    				<br>
    				<span class="mensagemExibindo">Advogado:&nbsp;</span>



    						Guilherme Freire Furtado

    				&nbsp;


    				<br>
    				<span class="mensagemExibindo">Advogada:&nbsp;</span>



    						Maria Eugênia Barreiros de Mello

    				&nbsp;


    				<br>
    				<span class="mensagemExibindo">Advogado:&nbsp;</span>



    						Vítor Reis de Araujo Carvalho

    				&nbsp;




    	</td>
    </tr>


    </tbody></table>



    	<!--  dados da lista todas as partes (partes) -->
    	<table id="tableTodasPartes" style="margin-left:15px; margin-top:1px; display: none; " align="center" width="98%" border="0" cellspacing="0" cellpadding="0">











    <tbody><tr class="fundoClaro">
    	<td valign="top" width="141" style="padding-bottom: 5px" class="label">
    		<span class="mensagemExibindo tipoDeParticipacao">Autor&nbsp;</span>
    	</td>
    	<td class="nomeParteEAdvogado" width="*" align="left" style="padding-bottom: 5px">




    					José Carlos Cerqueira Souza Filho







    				<br>
    				<span class="mensagemExibindo">Advogado:&nbsp;</span>



    						Vinicius Faria de Cerqueira

    				&nbsp;




    	</td>
    </tr>












    <tr class="fundoClaro">
    	<td valign="top" width="141" style="padding-bottom: 5px" class="label">
    		<span class="mensagemExibindo tipoDeParticipacao">Autora&nbsp;</span>
    	</td>
    	<td class="nomeParteEAdvogado" width="*" align="left" style="padding-bottom: 5px">




    					Livia Nascimento da Rocha







    				<br>
    				<span class="mensagemExibindo">Advogado:&nbsp;</span>



    						Vinicius Faria de Cerqueira

    				&nbsp;




    	</td>
    </tr>












    <tr class="fundoClaro">
    	<td valign="top" width="141" style="padding-bottom: 5px" class="label">
    		<span class="mensagemExibindo tipoDeParticipacao">Ré&nbsp;</span>
    	</td>
    	<td class="nomeParteEAdvogado" width="*" align="left" style="padding-bottom: 5px">




    					Cony Engenharia Ltda.







    				<br>
    				<span class="mensagemExibindo">Advogado:&nbsp;</span>



    						Carlos Henrique de Mendonça Brandão

    				&nbsp;


    				<br>
    				<span class="mensagemExibindo">Advogado:&nbsp;</span>



    						Guilherme Freire Furtado

    				&nbsp;


    				<br>
    				<span class="mensagemExibindo">Advogada:&nbsp;</span>



    						Maria Eugênia Barreiros de Mello

    				&nbsp;


    				<br>
    				<span class="mensagemExibindo">Advogado:&nbsp;</span>



    						Vítor Reis de Araujo Carvalho

    				&nbsp;




    	</td>
    </tr>












    <tr class="fundoClaro">
    	<td valign="top" width="141" style="padding-bottom: 5px" class="label">
    		<span class="mensagemExibindo tipoDeParticipacao">Réu&nbsp;</span>
    	</td>
    	<td class="nomeParteEAdvogado" width="*" align="left" style="padding-bottom: 5px">




    					Banco do Brasil S A







    				<br>
    				<span class="mensagemExibindo">Advogado:&nbsp;</span>



    						Nelson Wilians Fratoni Rodrigues

    				&nbsp;




    	</td>
    </tr>


    	</tbody></table>
        <div id="divLinksTituloBlocoPartes" style="text-align:right">










    <input id="mensagemNaoExibidapartes" type="hidden" value="">

        <input id="linkNaoExibidopartes" type="hidden" value="<span id=&quot;setasDireitapartes&quot; class=&quot;setasDireita&quot;><i class=&quot;unj-link-collapse__icon glyph glyph-chevron-up&quot;></i></span>Recolher">

    <span id="mensagensExibindopartes" class="mensagemExibindo">

    </span> &nbsp;

        <a id="linkpartes" href="javascript:" class="linkNaoSelecionado unj-link-collapse">
            <span id="setasDireitapartes" class="setasDireita">
                <i class="unj-link-collapse__icon glyph glyph-chevron-down"></i>
            </span>
            Mais
        </a>

    <script>
    	$(function() {
    		var controlarLink = function() {
    			var $linkNaoExibido = $('input#linkNaoExibidopartes');
    			var conteudoLinkNaoApresentado = $linkNaoExibido.val();
    			var $link = $('a#linkpartes');

    			$linkNaoExibido.val($link.html());
    			$link.html(conteudoLinkNaoApresentado);
    		};

    		var controlarMensagem = function() {
    			var $mensagemNaoExibida = $('input#mensagemNaoExibidapartes');
    			var $spanMensagem = $('span#mensagensExibindopartes');
    			var mensagemExibida = $spanMensagem.html();
    			var mensagemNaoExibida = $mensagemNaoExibida.val();

    			$spanMensagem.html(mensagemNaoExibida);
    			$mensagemNaoExibida.val(mensagemExibida);
    		};

    		var controlarMensagemLink = function() {
    			controlarMensagem();
    			controlarLink();
    		};

    		var esconderElementosExtrasMostrarDefault = function() {
    			$('#tableTodasPartes').hide();
    			$('#tablePartesPrincipais').show();
    		};

    		var mostrarElementosExtrasEsconderDefault = function() {
    			$('#tablePartesPrincipais').hide();
    			$('#tableTodasPartes').show();
    		};

    		var initPagina = function() {
                var setasDireita = '<span id="setasDireitapartes" class="setasDireita"><i class="unj-link-collapse__icon glyph glyph-chevron-up"></i></span>';
    			var $linkEscondido = $('input#linkNaoExibidopartes');
    			$linkEscondido.val(setasDireita+$linkEscondido.val());
    		};

    		var bindLink = function() {
    			var $link = $('a#linkpartes');
    			$link.funcToggle('click', mostrarElementosExtrasEsconderDefault, esconderElementosExtrasMostrarDefault);
    			$link.bind('click', controlarMensagemLink);
    		};

    		initPagina();
    		bindLink();
    		esconderElementosExtrasMostrarDefault();
    	});
    </script>

        </div>














































    <div style="padding-top: 10px;">











    			<h2 class="subtitle tituloDoBloco">Movimentações</h2>


    </div>





    <table style="margin-left:15px; margin-top:1px;" align="center" border="0" cellpadding="0" cellspacing="0" width="98%">


    			<thead>
    				<tr>
    				  <th width="120" class="label" style="vertical-align: bottom">Data</th>
    				  <th valign="middle" width="20" aria-hidden="true">&nbsp;</th>
    				  <th valign="middle" class="label">Movimento</th>
    				</tr>
    				<tr class="fundoEscuro" height="2" aria-hidden="true">
    					<td></td>
    					<td></td>
    					<td></td>
    				</tr>
    			</thead>


    			<tbody id="tabelaUltimasMovimentacoes">



















    	<tr class="fundoClaro containerMovimentacao" style="">
    		<td class="dataMovimentacao" width="120" style="vertical-align: top">
    			21/07/2023
    		</td>
    		<td width="20" valign="top" aria-hidden="true">

    		</td>
    		<td class="descricaoMovimentacao" style="vertical-align: top; padding-bottom: 5px">




    					Ato Publicado



    			<br>
    			<span style="font-style: italic;">
    				Relação: 0450/2023
    Data da Publicação: 24/07/2023
    Número do Diário: 3349
    			</span>

    		</td>
    	</tr>






















    	<tr class="fundoEscuro containerMovimentacao" style="">
    		<td class="dataMovimentacao" width="120" style="vertical-align: top">
    			20/07/2023
    		</td>
    		<td width="20" valign="top" aria-hidden="true">

    		</td>
    		<td class="descricaoMovimentacao" style="vertical-align: top; padding-bottom: 5px">




    					Disponibilização no Diário da Justiça Eletrônico



    			<br>
    			<span style="font-style: italic;">
    				Relação: 0450/2023
    Teor do ato: Autos n°: 0710802-55.2018.8.02.0001 Ação: Procedimento Comum Cível Autor: José Carlos Cerqueira Souza Filho e outro Réu: Cony Engenharia Ltda. e outro ATO ORDINATÓRIO Em cumprimento ao disposto no Provimento nº 15/2019, da Corregedoria Geral da Justiça do Estado de Alagoas, fica(m) a(s) parte(s) ré intimada(s), na pessoa do seu advogado, para, no prazo de 15 (quinze) dias, providenciar(em) o recolhimento das custas processuais, sob pena de expedição de certidão ao FUNJURIS (Resolução TJ/AL nº 19/2007) para inscrição na divida ativa estadual, após o que será arquivado o processo. Ocorrendo o pagamento, devidamente atualizado, após a emissão da supracitada certidão de débito, deverá o interessado entregar a ficha de compensação bancária quitada na sede do FUNJURIS, que se responsabilizará pela devida baixa, além de oficiar à secretaria de onde se originou o débito acerca do referido pagamento (Resolução nº 19/2007, art. 33, § 6º). Maceió, 20 de julho de 2023 Marcelo Rodrigo Falcão Vieira Analista(escrivão substituto)
    Advogados(s): Nelson Wilians Fratoni Rodrigues (OAB 9395AAL/), Carlos Henrique de Mendonça Brandão (OAB 6770AL /), Vinicius Faria de Cerqueira (OAB 9008/AL), Maria Eugênia Barreiros de Mello (OAB 14717AL/), Guilherme Freire Furtado (OAB 14781/AL), Vítor Reis de Araujo Carvalho (OAB 14928/AL)
    			</span>

    		</td>
    	</tr>






















    	<tr class="fundoClaro containerMovimentacao" style="">
    		<td class="dataMovimentacao" width="120" style="vertical-align: top">
    			20/07/2023
    		</td>
    		<td width="20" valign="top" aria-hidden="true">








    				<a class="linkMovVincProc" id="linkMovVincProc-49454402" title="Visualizar documento em inteiro teor" href="#liberarAutoPorSenha">
    					<img width="16" height="16" border="0" src="/cpopg/imagens/doc.png">
    				</a>

    		</td>
    		<td class="descricaoMovimentacao" style="vertical-align: top; padding-bottom: 5px">



    					<a class="linkMovVincProc" id="linkMovVincProc-2-49454402" title="Visualizar documento em inteiro teor" href="#liberarAutoPorSenha"> Ato ordinatório praticado
    					</a>




    			<br>
    			<span style="font-style: italic;">
    				Autos n°: 0710802-55.2018.8.02.0001 Ação: Procedimento Comum Cível Autor: José Carlos Cerqueira Souza Filho e outro Réu: Cony Engenharia Ltda. e outro ATO ORDINATÓRIO Em cumprimento ao disposto no Provimento nº 15/2019, da Corregedoria Geral da Justiça do Estado de Alagoas, fica(m) a(s) parte(s) ré intimada(s), na pessoa do seu advogado, para, no prazo de 15 (quinze) dias, providenciar(em) o recolhimento das custas processuais, sob pena de expedição de certidão ao FUNJURIS (Resolução TJ/AL nº 19/2007) para inscrição na divida ativa estadual, após o que será arquivado o processo. Ocorrendo o pagamento, devidamente atualizado, após a emissão da supracitada certidão de débito, deverá o interessado entregar a ficha de compensação bancária quitada na sede do FUNJURIS, que se responsabilizará pela devida baixa, além de oficiar à secretaria de onde se originou o débito acerca do referido pagamento (Resolução nº 19/2007, art. 33, § 6º). Maceió, 20 de julho de 2023 Marcelo Rodrigo Falcão Vieira Analista(escrivão substituto)<br><b>Vencimento: </b>10/08/2023
    			</span>

    		</td>
    	</tr>






















    	<tr class="fundoEscuro containerMovimentacao" style="">
    		<td class="dataMovimentacao" width="120" style="vertical-align: top">
    			20/07/2023
    		</td>
    		<td width="20" valign="top" aria-hidden="true">








    				<a class="linkMovVincProc" id="linkMovVincProc-49453649" title="Visualizar documento em inteiro teor" href="#liberarAutoPorSenha">
    					<img width="16" height="16" border="0" src="/cpopg/imagens/doc.png">
    				</a>

    		</td>
    		<td class="descricaoMovimentacao" style="vertical-align: top; padding-bottom: 5px">



    					<a class="linkMovVincProc" id="linkMovVincProc-2-49453649" title="Visualizar documento em inteiro teor" href="#liberarAutoPorSenha"> Devolvido CJU - Cálculo de Custas Finais Realizado
    					</a>




    			<br>
    			<span style="font-style: italic;">
    				Devolvido CJU - Cálculo de Custas Finais Realizado
    			</span>

    		</td>
    	</tr>






















    	<tr class="fundoClaro containerMovimentacao" style="">
    		<td class="dataMovimentacao" width="120" style="vertical-align: top">
    			20/07/2023
    		</td>
    		<td width="20" valign="top" aria-hidden="true">

    		</td>
    		<td class="descricaoMovimentacao" style="vertical-align: top; padding-bottom: 5px">




    					Realizado cálculo de custas



    			<br>
    			<span style="font-style: italic;">

    			</span>

    		</td>
    	</tr>




    			</tbody>


    			<tbody style="display: none;" id="tabelaTodasMovimentacoes">



















    	<tr class="fundoClaro containerMovimentacao" style="">
    		<td class="dataMovimentacao" width="120" style="vertical-align: top">
    			21/07/2023
    		</td>
    		<td width="20" valign="top" aria-hidden="true">

    		</td>
    		<td class="descricaoMovimentacao" style="vertical-align: top; padding-bottom: 5px">




    					Ato Publicado



    			<br>
    			<span style="font-style: italic;">
    				Relação: 0450/2023
    Data da Publicação: 24/07/2023
    Número do Diário: 3349
    			</span>

    		</td>
    	</tr>






















    	<tr class="fundoEscuro containerMovimentacao" style="">
    		<td class="dataMovimentacao" width="120" style="vertical-align: top">
    			20/07/2023
    		</td>
    		<td width="20" valign="top" aria-hidden="true">

    		</td>
    		<td class="descricaoMovimentacao" style="vertical-align: top; padding-bottom: 5px">




    					Disponibilização no Diário da Justiça Eletrônico



    			<br>
    			<span style="font-style: italic;">
    				Relação: 0450/2023
    Teor do ato: Autos n°: 0710802-55.2018.8.02.0001 Ação: Procedimento Comum Cível Autor: José Carlos Cerqueira Souza Filho e outro Réu: Cony Engenharia Ltda. e outro ATO ORDINATÓRIO Em cumprimento ao disposto no Provimento nº 15/2019, da Corregedoria Geral da Justiça do Estado de Alagoas, fica(m) a(s) parte(s) ré intimada(s), na pessoa do seu advogado, para, no prazo de 15 (quinze) dias, providenciar(em) o recolhimento das custas processuais, sob pena de expedição de certidão ao FUNJURIS (Resolução TJ/AL nº 19/2007) para inscrição na divida ativa estadual, após o que será arquivado o processo. Ocorrendo o pagamento, devidamente atualizado, após a emissão da supracitada certidão de débito, deverá o interessado entregar a ficha de compensação bancária quitada na sede do FUNJURIS, que se responsabilizará pela devida baixa, além de oficiar à secretaria de onde se originou o débito acerca do referido pagamento (Resolução nº 19/2007, art. 33, § 6º). Maceió, 20 de julho de 2023 Marcelo Rodrigo Falcão Vieira Analista(escrivão substituto)
    Advogados(s): Nelson Wilians Fratoni Rodrigues (OAB 9395AAL/), Carlos Henrique de Mendonça Brandão (OAB 6770AL /), Vinicius Faria de Cerqueira (OAB 9008/AL), Maria Eugênia Barreiros de Mello (OAB 14717AL/), Guilherme Freire Furtado (OAB 14781/AL), Vítor Reis de Araujo Carvalho (OAB 14928/AL)
    			</span>

    		</td>
    	</tr>






















    	<tr class="fundoClaro containerMovimentacao" style="">
    		<td class="dataMovimentacao" width="120" style="vertical-align: top">
    			20/07/2023
    		</td>
    		<td width="20" valign="top" aria-hidden="true">








    				<a class="linkMovVincProc" id="linkMovVincProc-49454402" title="Visualizar documento em inteiro teor" href="#liberarAutoPorSenha">
    					<img width="16" height="16" border="0" src="/cpopg/imagens/doc.png">
    				</a>

    		</td>
    		<td class="descricaoMovimentacao" style="vertical-align: top; padding-bottom: 5px">



    					<a class="linkMovVincProc" id="linkMovVincProc-2-49454402" title="Visualizar documento em inteiro teor" href="#liberarAutoPorSenha"> Ato ordinatório praticado
    					</a>




    			<br>
    			<span style="font-style: italic;">
    				Autos n°: 0710802-55.2018.8.02.0001 Ação: Procedimento Comum Cível Autor: José Carlos Cerqueira Souza Filho e outro Réu: Cony Engenharia Ltda. e outro ATO ORDINATÓRIO Em cumprimento ao disposto no Provimento nº 15/2019, da Corregedoria Geral da Justiça do Estado de Alagoas, fica(m) a(s) parte(s) ré intimada(s), na pessoa do seu advogado, para, no prazo de 15 (quinze) dias, providenciar(em) o recolhimento das custas processuais, sob pena de expedição de certidão ao FUNJURIS (Resolução TJ/AL nº 19/2007) para inscrição na divida ativa estadual, após o que será arquivado o processo. Ocorrendo o pagamento, devidamente atualizado, após a emissão da supracitada certidão de débito, deverá o interessado entregar a ficha de compensação bancária quitada na sede do FUNJURIS, que se responsabilizará pela devida baixa, além de oficiar à secretaria de onde se originou o débito acerca do referido pagamento (Resolução nº 19/2007, art. 33, § 6º). Maceió, 20 de julho de 2023 Marcelo Rodrigo Falcão Vieira Analista(escrivão substituto)<br><b>Vencimento: </b>10/08/2023
    			</span>

    		</td>
    	</tr>






















    	<tr class="fundoEscuro containerMovimentacao" style="">
    		<td class="dataMovimentacao" width="120" style="vertical-align: top">
    			20/07/2023
    		</td>
    		<td width="20" valign="top" aria-hidden="true">








    				<a class="linkMovVincProc" id="linkMovVincProc-49453649" title="Visualizar documento em inteiro teor" href="#liberarAutoPorSenha">
    					<img width="16" height="16" border="0" src="/cpopg/imagens/doc.png">
    				</a>

    		</td>
    		<td class="descricaoMovimentacao" style="vertical-align: top; padding-bottom: 5px">



    					<a class="linkMovVincProc" id="linkMovVincProc-2-49453649" title="Visualizar documento em inteiro teor" href="#liberarAutoPorSenha"> Devolvido CJU - Cálculo de Custas Finais Realizado
    					</a>




    			<br>
    			<span style="font-style: italic;">
    				Devolvido CJU - Cálculo de Custas Finais Realizado
    			</span>

    		</td>
    	</tr>






















    	<tr class="fundoClaro containerMovimentacao" style="">
    		<td class="dataMovimentacao" width="120" style="vertical-align: top">
    			20/07/2023
    		</td>
    		<td width="20" valign="top" aria-hidden="true">

    		</td>
    		<td class="descricaoMovimentacao" style="vertical-align: top; padding-bottom: 5px">




    					Realizado cálculo de custas



    			<br>
    			<span style="font-style: italic;">

    			</span>

    		</td>
    	</tr>






















    	<tr class="fundoEscuro containerMovimentacao" style="">
    		<td class="dataMovimentacao" width="120" style="vertical-align: top">
    			20/07/2023
    		</td>
    		<td width="20" valign="top" aria-hidden="true">

    		</td>
    		<td class="descricaoMovimentacao" style="vertical-align: top; padding-bottom: 5px">




    					Juntada de Documento



    			<br>
    			<span style="font-style: italic;">

    			</span>

    		</td>
    	</tr>






















    	<tr class="fundoClaro containerMovimentacao" style="">
    		<td class="dataMovimentacao" width="120" style="vertical-align: top">
    			05/05/2023
    		</td>
    		<td width="20" valign="top" aria-hidden="true">

    		</td>
    		<td class="descricaoMovimentacao" style="vertical-align: top; padding-bottom: 5px">




    					Execução de Sentença Iniciada



    			<br>
    			<span style="font-style: italic;">
    				Seq.: 01 - Cumprimento de sentença
    			</span>

    		</td>
    	</tr>






















    	<tr class="fundoEscuro containerMovimentacao" style="">
    		<td class="dataMovimentacao" width="120" style="vertical-align: top">
    			05/05/2023
    		</td>
    		<td width="20" valign="top" aria-hidden="true">

    		</td>
    		<td class="descricaoMovimentacao" style="vertical-align: top; padding-bottom: 5px">




    					Ato Publicado



    			<br>
    			<span style="font-style: italic;">
    				Relação: 0282/2023
    Data da Publicação: 08/05/2023
    Número do Diário: 3296
    			</span>

    		</td>
    	</tr>






















    	<tr class="fundoClaro containerMovimentacao" style="">
    		<td class="dataMovimentacao" width="120" style="vertical-align: top">
    			04/05/2023
    		</td>
    		<td width="20" valign="top" aria-hidden="true">

    		</td>
    		<td class="descricaoMovimentacao" style="vertical-align: top; padding-bottom: 5px">




    					Disponibilização no Diário da Justiça Eletrônico



    			<br>
    			<span style="font-style: italic;">
    				Relação: 0282/2023
    Teor do ato: Autos n°: 0710802-55.2018.8.02.0001 Ação: Procedimento Comum Cível Autor: José Carlos Cerqueira Souza Filho e outro Réu: Cony Engenharia Ltda. e outro ATO ORDINATÓRIO Em cumprimento ao Provimento nº 15/2019, da Corregedoria-Geral da Justiça do Estado de Alagoas, em virtude do retorno dos autos da instância superior, manifestem-se as partes, em 15 (quinze) dias, requerendo o que de direito. Maceió, 04 de maio de 2023 Marcelo Rodrigo Falcão Vieira Analista(escrivão substituto)
    Advogados(s): Nelson Wilians Fratoni Rodrigues (OAB 9395A/AL), Carlos Henrique de Mendonça Brandão (OAB 6770/AL), Vinicius Faria de Cerqueira (OAB 9008/AL), Maria Eugênia Barreiros de Mello (OAB 14717/AL), Guilherme Freire Furtado (OAB 14781/AL), Vítor Reis de Araujo Carvalho (OAB 14928/AL)
    			</span>

    		</td>
    	</tr>






















    	<tr class="fundoEscuro containerMovimentacao" style="">
    		<td class="dataMovimentacao" width="120" style="vertical-align: top">
    			04/05/2023
    		</td>
    		<td width="20" valign="top" aria-hidden="true">

    		</td>
    		<td class="descricaoMovimentacao" style="vertical-align: top; padding-bottom: 5px">




    					Recebido pela Contadoria UNIFICADA



    			<br>
    			<span style="font-style: italic;">

    			</span>

    		</td>
    	</tr>






















    	<tr class="fundoClaro containerMovimentacao" style="">
    		<td class="dataMovimentacao" width="120" style="vertical-align: top">
    			04/05/2023
    		</td>
    		<td width="20" valign="top" aria-hidden="true">








    				<a class="linkMovVincProc" id="linkMovVincProc-48258011" title="Visualizar documento em inteiro teor" href="#liberarAutoPorSenha">
    					<img width="16" height="16" border="0" src="/cpopg/imagens/doc.png">
    				</a>

    		</td>
    		<td class="descricaoMovimentacao" style="vertical-align: top; padding-bottom: 5px">



    					<a class="linkMovVincProc" id="linkMovVincProc-2-48258011" title="Visualizar documento em inteiro teor" href="#liberarAutoPorSenha"> Ato Ordinatório - Artigo 162, §4º, CPC
    					</a>




    			<br>
    			<span style="font-style: italic;">
    				Ato Ordinatório- Remessa à contadoria
    			</span>

    		</td>
    	</tr>






















    	<tr class="fundoEscuro containerMovimentacao" style="">
    		<td class="dataMovimentacao" width="120" style="vertical-align: top">
    			04/05/2023
    		</td>
    		<td width="20" valign="top" aria-hidden="true">








    				<a class="linkMovVincProc" id="linkMovVincProc-48258006" title="Visualizar documento em inteiro teor" href="#liberarAutoPorSenha">
    					<img width="16" height="16" border="0" src="/cpopg/imagens/doc.png">
    				</a>

    		</td>
    		<td class="descricaoMovimentacao" style="vertical-align: top; padding-bottom: 5px">



    					<a class="linkMovVincProc" id="linkMovVincProc-2-48258006" title="Visualizar documento em inteiro teor" href="#liberarAutoPorSenha"> Ato ordinatório praticado
    					</a>




    			<br>
    			<span style="font-style: italic;">
    				Autos n°: 0710802-55.2018.8.02.0001 Ação: Procedimento Comum Cível Autor: José Carlos Cerqueira Souza Filho e outro Réu: Cony Engenharia Ltda. e outro ATO ORDINATÓRIO Em cumprimento ao Provimento nº 15/2019, da Corregedoria-Geral da Justiça do Estado de Alagoas, em virtude do retorno dos autos da instância superior, manifestem-se as partes, em 15 (quinze) dias, requerendo o que de direito. Maceió, 04 de maio de 2023 Marcelo Rodrigo Falcão Vieira Analista(escrivão substituto)<br><b>Vencimento: </b>25/05/2023
    			</span>

    		</td>
    	</tr>






















    	<tr class="fundoClaro containerMovimentacao" style="">
    		<td class="dataMovimentacao" width="120" style="vertical-align: top">
    			03/05/2023
    		</td>
    		<td width="20" valign="top" aria-hidden="true">

    		</td>
    		<td class="descricaoMovimentacao" style="vertical-align: top; padding-bottom: 5px">




    					Transitado em Julgado



    			<br>
    			<span style="font-style: italic;">

    			</span>

    		</td>
    	</tr>






















    	<tr class="fundoEscuro containerMovimentacao" style="">
    		<td class="dataMovimentacao" width="120" style="vertical-align: top">
    			03/05/2023
    		</td>
    		<td width="20" valign="top" aria-hidden="true">

    		</td>
    		<td class="descricaoMovimentacao" style="vertical-align: top; padding-bottom: 5px">




    					Recebimento da Instância Superior -  Altera situação para "Julgado"



    			<br>
    			<span style="font-style: italic;">

    			</span>

    		</td>
    	</tr>






















    	<tr class="fundoClaro containerMovimentacao" style="">
    		<td class="dataMovimentacao" width="120" style="vertical-align: top">
    			26/04/2023
    		</td>
    		<td width="20" valign="top" aria-hidden="true">

    		</td>
    		<td class="descricaoMovimentacao" style="vertical-align: top; padding-bottom: 5px">




    					Recebido recurso eletrônico



    			<br>
    			<span style="font-style: italic;">
    				Data do julgamento: 07/10/2021
    Trânsito em julgado:
    Tipo de julgamento: Acórdão
    Decisão: à unanimidade de votos, em CONHECER de ambos os recursos de Apelação Cível; e, no mérito, por idêntica votação, NEGAR-LHES PROVIMENTO, mantendo incólume a Sentença proferida pelo Juízo de Direito de Primeiro Grau. Acordam, ainda, em majorar os honorários advocatícios sucumbenciais para 17% sobre o valor da condenação, nos termos do voto do Relator.
    Situação do provimento:
    Relator: Des. Otávio Leão Praxedes
    			</span>

    		</td>
    	</tr>






















    	<tr class="fundoEscuro containerMovimentacao" style="">
    		<td class="dataMovimentacao" width="120" style="vertical-align: top">
    			22/02/2021
    		</td>
    		<td width="20" valign="top" aria-hidden="true">

    		</td>
    		<td class="descricaoMovimentacao" style="vertical-align: top; padding-bottom: 5px">




    					Remetido recurso eletrônico ao Tribunal de Justiça/Turma de recurso



    			<br>
    			<span style="font-style: italic;">

    			</span>

    		</td>
    	</tr>






















    	<tr class="fundoClaro containerMovimentacao" style="">
    		<td class="dataMovimentacao" width="120" style="vertical-align: top">
    			10/02/2021
    		</td>
    		<td width="20" valign="top" aria-hidden="true">

    		</td>
    		<td class="descricaoMovimentacao" style="vertical-align: top; padding-bottom: 5px">




    					Juntada de Documento



    			<br>
    			<span style="font-style: italic;">
    				Nº Protocolo: WMAC.21.70031538-2
    Tipo da Petição: Contrarrazões
    Data: 10/02/2021 19:27

    			</span>

    		</td>
    	</tr>






















    	<tr class="fundoEscuro containerMovimentacao" style="">
    		<td class="dataMovimentacao" width="120" style="vertical-align: top">
    			06/01/2021
    		</td>
    		<td width="20" valign="top" aria-hidden="true">

    		</td>
    		<td class="descricaoMovimentacao" style="vertical-align: top; padding-bottom: 5px">




    					Ato Publicado



    			<br>
    			<span style="font-style: italic;">
    				Relação :0003/2021
    Data da Publicação: 21/01/2021
    Número do Diário: 2738
    			</span>

    		</td>
    	</tr>






















    	<tr class="fundoClaro containerMovimentacao" style="">
    		<td class="dataMovimentacao" width="120" style="vertical-align: top">
    			06/01/2021
    		</td>
    		<td width="20" valign="top" aria-hidden="true">

    		</td>
    		<td class="descricaoMovimentacao" style="vertical-align: top; padding-bottom: 5px">




    					Ato Publicado



    			<br>
    			<span style="font-style: italic;">
    				Relação :0003/2021
    Data da Publicação: 21/01/2021
    Número do Diário: 2738
    			</span>

    		</td>
    	</tr>






















    	<tr class="fundoEscuro containerMovimentacao" style="">
    		<td class="dataMovimentacao" width="120" style="vertical-align: top">
    			06/01/2021
    		</td>
    		<td width="20" valign="top" aria-hidden="true">

    		</td>
    		<td class="descricaoMovimentacao" style="vertical-align: top; padding-bottom: 5px">




    					Ato Publicado



    			<br>
    			<span style="font-style: italic;">
    				Relação :0003/2021
    Data da Publicação: 21/01/2021
    Número do Diário: 2738
    			</span>

    		</td>
    	</tr>






















    	<tr class="fundoClaro containerMovimentacao" style="">
    		<td class="dataMovimentacao" width="120" style="vertical-align: top">
    			06/01/2021
    		</td>
    		<td width="20" valign="top" aria-hidden="true">

    		</td>
    		<td class="descricaoMovimentacao" style="vertical-align: top; padding-bottom: 5px">




    					Ato Publicado



    			<br>
    			<span style="font-style: italic;">
    				Relação :0003/2021
    Data da Publicação: 21/01/2021
    Número do Diário: 2738
    			</span>

    		</td>
    	</tr>






















    	<tr class="fundoEscuro containerMovimentacao" style="">
    		<td class="dataMovimentacao" width="120" style="vertical-align: top">
    			06/01/2021
    		</td>
    		<td width="20" valign="top" aria-hidden="true">

    		</td>
    		<td class="descricaoMovimentacao" style="vertical-align: top; padding-bottom: 5px">




    					Ato Publicado



    			<br>
    			<span style="font-style: italic;">
    				Relação :0003/2021
    Data da Publicação: 21/01/2021
    Número do Diário: 2738
    			</span>

    		</td>
    	</tr>






















    	<tr class="fundoClaro containerMovimentacao" style="">
    		<td class="dataMovimentacao" width="120" style="vertical-align: top">
    			06/01/2021
    		</td>
    		<td width="20" valign="top" aria-hidden="true">

    		</td>
    		<td class="descricaoMovimentacao" style="vertical-align: top; padding-bottom: 5px">




    					Ato Publicado



    			<br>
    			<span style="font-style: italic;">
    				Relação :0003/2021
    Data da Publicação: 21/01/2021
    Número do Diário: 2738
    			</span>

    		</td>
    	</tr>






















    	<tr class="fundoEscuro containerMovimentacao" style="">
    		<td class="dataMovimentacao" width="120" style="vertical-align: top">
    			05/01/2021
    		</td>
    		<td width="20" valign="top" aria-hidden="true">

    		</td>
    		<td class="descricaoMovimentacao" style="vertical-align: top; padding-bottom: 5px">




    					Disponibilização no Diário da Justiça Eletrônico



    			<br>
    			<span style="font-style: italic;">
    				Relação: 0003/2021
    Teor do ato: Ato Ordinatório: Interposto recurso de apelação pelos réus (Banco do Brasil e Cony Engenharia), intime-se a parte recorrida para apresentar contrarrazões, no prazo de 15 (quinze) dias, conforme o art. 1010,§ 1º do CPC. Se apresentada Apelação Adesiva pela parte recorrida (art.997, §2º do CPC), intime-se a parte contrária para contrarrazões, no prazo de 15 (quinze) dias, nos termos do Art. 1010, §2º do CPC. Caso as contrarrazões do recurso principal ou do adesivo ventilem matérias elencadas no art.1009, §1º do CPC, intime-se o recorrente para se manifestar sobre elas no prazo de 15(quinze) dias, conforme o art. 1009, § 2º, do CPC. Após as providências acima, remetam-se os autos ao Egrégio Tribunal de Justiça. Maceió, 04 de janeiro de 2021. Fernanda Patrícia Belo Marques Técnico Judiciário
    Advogados(s): Carlos Henrique de Mendonça Brandão (OAB 6770/AL), Vinicius Faria de Cerqueira (OAB 9008/AL), Nelson Wilians Fratoni Rodrigues (OAB 9395A/AL), Maria Eugênia Barreiros de Mello (OAB 14717/AL), Guilherme Freire Furtado (OAB 14781/AL), Vítor Reis de Araujo Carvalho (OAB 14928/AL)
    			</span>

    		</td>
    	</tr>






















    	<tr class="fundoClaro containerMovimentacao" style="">
    		<td class="dataMovimentacao" width="120" style="vertical-align: top">
    			04/01/2021
    		</td>
    		<td width="20" valign="top" aria-hidden="true">








    				<a class="linkMovVincProc" id="linkMovVincProc-36544373" title="Visualizar documento em inteiro teor" href="#liberarAutoPorSenha">
    					<img width="16" height="16" border="0" src="/cpopg/imagens/doc.png">
    				</a>

    		</td>
    		<td class="descricaoMovimentacao" style="vertical-align: top; padding-bottom: 5px">



    					<a class="linkMovVincProc" id="linkMovVincProc-2-36544373" title="Visualizar documento em inteiro teor" href="#liberarAutoPorSenha"> Ato Ordinatório - Artigo 162, §4º, CPC
    					</a>




    			<br>
    			<span style="font-style: italic;">
    				Ato Ordinatório: Interposto recurso de apelação pelos réus (Banco do Brasil e Cony Engenharia), intime-se a parte recorrida para apresentar contrarrazões, no prazo de 15 (quinze) dias, conforme o art. 1010,§ 1º do CPC. Se apresentada Apelação Adesiva pela parte recorrida (art.997, §2º do CPC), intime-se a parte contrária para contrarrazões, no prazo de 15 (quinze) dias, nos termos do Art. 1010, §2º do CPC. Caso as contrarrazões do recurso principal ou do adesivo ventilem matérias elencadas no art.1009, §1º do CPC, intime-se o recorrente para se manifestar sobre elas no prazo de 15(quinze) dias, conforme o art. 1009, § 2º, do CPC. Após as providências acima, remetam-se os autos ao Egrégio Tribunal de Justiça. Maceió, 04 de janeiro de 2021. Fernanda Patrícia Belo Marques Técnico Judiciário
    			</span>

    		</td>
    	</tr>






















    	<tr class="fundoEscuro containerMovimentacao" style="">
    		<td class="dataMovimentacao" width="120" style="vertical-align: top">
    			18/12/2020
    		</td>
    		<td width="20" valign="top" aria-hidden="true">

    		</td>
    		<td class="descricaoMovimentacao" style="vertical-align: top; padding-bottom: 5px">




    					Juntada de Documento



    			<br>
    			<span style="font-style: italic;">
    				Nº Protocolo: WMAC.20.70269584-0
    Tipo da Petição: Juntada de Instrumento de Procuração
    Data: 18/12/2020 17:23

    			</span>

    		</td>
    	</tr>






















    	<tr class="fundoClaro containerMovimentacao" style="">
    		<td class="dataMovimentacao" width="120" style="vertical-align: top">
    			18/12/2020
    		</td>
    		<td width="20" valign="top" aria-hidden="true">

    		</td>
    		<td class="descricaoMovimentacao" style="vertical-align: top; padding-bottom: 5px">




    					Juntada de Documento



    			<br>
    			<span style="font-style: italic;">
    				Nº Protocolo: WMAC.20.70269581-5
    Tipo da Petição: Recurso de Apelação
    Data: 18/12/2020 17:18

    			</span>

    		</td>
    	</tr>






















    	<tr class="fundoEscuro containerMovimentacao" style="">
    		<td class="dataMovimentacao" width="120" style="vertical-align: top">
    			15/12/2020
    		</td>
    		<td width="20" valign="top" aria-hidden="true">

    		</td>
    		<td class="descricaoMovimentacao" style="vertical-align: top; padding-bottom: 5px">




    					Juntada de Documento



    			<br>
    			<span style="font-style: italic;">
    				Nº Protocolo: WMAC.20.70265228-8
    Tipo da Petição: Recurso de Apelação
    Data: 15/12/2020 13:26

    			</span>

    		</td>
    	</tr>






















    	<tr class="fundoClaro containerMovimentacao" style="">
    		<td class="dataMovimentacao" width="120" style="vertical-align: top">
    			24/11/2020
    		</td>
    		<td width="20" valign="top" aria-hidden="true">

    		</td>
    		<td class="descricaoMovimentacao" style="vertical-align: top; padding-bottom: 5px">




    					Ato Publicado



    			<br>
    			<span style="font-style: italic;">
    				Relação :0912/2020
    Data da Publicação: 25/11/2020
    Número do Diário: 2711
    			</span>

    		</td>
    	</tr>






















    	<tr class="fundoEscuro containerMovimentacao" style="">
    		<td class="dataMovimentacao" width="120" style="vertical-align: top">
    			24/11/2020
    		</td>
    		<td width="20" valign="top" aria-hidden="true">

    		</td>
    		<td class="descricaoMovimentacao" style="vertical-align: top; padding-bottom: 5px">




    					Ato Publicado



    			<br>
    			<span style="font-style: italic;">
    				Relação :0912/2020
    Data da Publicação: 25/11/2020
    Número do Diário: 2711
    			</span>

    		</td>
    	</tr>






















    	<tr class="fundoClaro containerMovimentacao" style="">
    		<td class="dataMovimentacao" width="120" style="vertical-align: top">
    			24/11/2020
    		</td>
    		<td width="20" valign="top" aria-hidden="true">

    		</td>
    		<td class="descricaoMovimentacao" style="vertical-align: top; padding-bottom: 5px">




    					Ato Publicado



    			<br>
    			<span style="font-style: italic;">
    				Relação :0912/2020
    Data da Publicação: 25/11/2020
    Número do Diário: 2711
    			</span>

    		</td>
    	</tr>






















    	<tr class="fundoEscuro containerMovimentacao" style="">
    		<td class="dataMovimentacao" width="120" style="vertical-align: top">
    			24/11/2020
    		</td>
    		<td width="20" valign="top" aria-hidden="true">

    		</td>
    		<td class="descricaoMovimentacao" style="vertical-align: top; padding-bottom: 5px">




    					Ato Publicado



    			<br>
    			<span style="font-style: italic;">
    				Relação :0912/2020
    Data da Publicação: 25/11/2020
    Número do Diário: 2711
    			</span>

    		</td>
    	</tr>






















    	<tr class="fundoClaro containerMovimentacao" style="">
    		<td class="dataMovimentacao" width="120" style="vertical-align: top">
    			23/11/2020
    		</td>
    		<td width="20" valign="top" aria-hidden="true">

    		</td>
    		<td class="descricaoMovimentacao" style="vertical-align: top; padding-bottom: 5px">




    					Disponibilização no Diário da Justiça Eletrônico



    			<br>
    			<span style="font-style: italic;">
    				Relação: 0912/2020
    Teor do ato: Forte nessas razões, JULGO PARCIALMENTE PROCEDENTES os pedidos da proemial, julgando extinto o processo com resolução de mérito, nos termos do art. 487, inciso I, do Estatuto Processual emergente, para o fim de CONDENAR AS DEMANDADAS, solidariamente: a) a ressarcir os danos materiais promovidos (lucros cessantes), cujo valor fixo em R$ 1.500,00 (três mil e quinhentos reais), por cada mês de atraso na entrega do imóvel , a incidir desde o dia 1 de agosto de 2017 até a data da efetiva entrega do imóvel, a ser apurada na fase de liquidação da sentença. Ressalto que esses valores deverão ser atualizados monetariamente pelo INPC desde a data em que cada aluguel seria devido, e acrescidos de juros de mora de 1% (um por cento) ao mês, contados da citação (art. 405 do Código Substantivo Civil). Para aqueles que venceram após a data da propositura da demanda, o juros de mora deverá incidir a partir da data de cada inadimplemento, para obstar o enriquecimento sem causa; b) em donos morais de R$ 5.000,00 (cinco mil reais), com juros de mora de 1% (um por cento) ao mês, a partir do dia 1 de agosto de 2017 (art. 397). Correção monetária, pelo INPC, desde a data do arbitramento; c) determino a substituição do índice INCC pelo IGP-M, a partir de 01 de agosto de 2017, e, como colorário, a devolução dos valores pagos a maior, com suas respectivas atualizações, nas mesmas condições do item a, deste dispositivo. Rejeito o pedido de restituição em dobro, por não vislumbrar má-fé dos beneficiários dos pagamentos indevidos. Oportunamente, condeno as demandada ao pagamento das custas e despesas processuais e dos honorários do advogado da parte adversa, que fixo, nos termos do art. 85, §2º, do Código de Processo Civil, e considerada a complexidade da demanda e as intervenções que exigiu, em 15% (quinze por cento) sobre o valor atualizado da condenação. Por fim, de modo a evitar o ajuizamento de embargos de declaração meramente protelatórios, registre-se que, ficam preteridas as demais alegações, por incompatíveis com a linha de raciocínio adotada, observando que os pedidos de ambas as partes foram apreciados nos limites em que foram formulados. Com efeito, ficam as partes advertidas, desde logo, que a oposição de embargos de declaração fora das hipóteses legais e/ou com postulação meramente infringente lhes sujeitará a imposição da multa prevista pelo artigo 1026, §2º, do Código de Processo Civil. Publique-se. Registre-se. Intimem-se.
    Advogados(s): Orlando de Moura Cavalcante Neto (OAB 7313/AL), Thiago Maia Nobre Rocha (OAB 6213/AL), Vinicius Faria de Cerqueira (OAB 9008/AL), Marcus Vinicius Cavalcante Lins Filho (OAB 10871/AL)
    			</span>

    		</td>
    	</tr>






















    	<tr class="fundoEscuro containerMovimentacao" style="">
    		<td class="dataMovimentacao" width="120" style="vertical-align: top">
    			23/11/2020
    		</td>
    		<td width="20" valign="top" aria-hidden="true">








    				<a class="linkMovVincProc" id="linkMovVincProc-36008611" title="Visualizar documento em inteiro teor" href="/cpopg/abrirDocumentoVinculadoMovimentacao.do?processo.codigo=01000O7550000&amp;cdDocumento=36008611&amp;nmRecursoAcessado=Julgado+procedente+em+parte+do+pedido" target="_blank">
    					<img width="16" height="16" border="0" src="/cpopg/imagens/doc.png">
    				</a>

    		</td>
    		<td class="descricaoMovimentacao" style="vertical-align: top; padding-bottom: 5px">



    					<a class="linkMovVincProc" id="linkMovVincProc-2-36008611" title="Visualizar documento em inteiro teor" href="/cpopg/abrirDocumentoVinculadoMovimentacao.do?processo.codigo=01000O7550000&amp;cdDocumento=36008611&amp;nmRecursoAcessado=Julgado+procedente+em+parte+do+pedido" target="_blank"> Julgado procedente em parte do pedido
    					</a>




    			<br>
    			<span style="font-style: italic;">
    				Forte nessas razões, JULGO PARCIALMENTE PROCEDENTES os pedidos da proemial, julgando extinto o processo com resolução de mérito, nos termos do art. 487, inciso I, do Estatuto Processual emergente, para o fim de CONDENAR AS DEMANDADAS, solidariamente: a) a ressarcir os danos materiais promovidos (lucros cessantes), cujo valor fixo em R$ 1.500,00 (três mil e quinhentos reais), por cada mês de atraso na entrega do imóvel , a incidir desde o dia 1 de agosto de 2017 até a data da efetiva entrega do imóvel, a ser apurada na fase de liquidação da sentença. Ressalto que esses valores deverão ser atualizados monetariamente pelo INPC desde a data em que cada aluguel seria devido, e acrescidos de juros de mora de 1% (um por cento) ao mês, contados da citação (art. 405 do Código Substantivo Civil). Para aqueles que venceram após a data da propositura da demanda, o juros de mora deverá incidir a partir da data de cada inadimplemento, para obstar o enriquecimento sem causa; b) em donos morais de R$ 5.000,00 (cinco mil reais), com juros de mora de 1% (um por cento) ao mês, a partir do dia 1 de agosto de 2017 (art. 397). Correção monetária, pelo INPC, desde a data do arbitramento; c) determino a substituição do índice INCC pelo IGP-M, a partir de 01 de agosto de 2017, e, como colorário, a devolução dos valores pagos a maior, com suas respectivas atualizações, nas mesmas condições do item a, deste dispositivo. Rejeito o pedido de restituição em dobro, por não vislumbrar má-fé dos beneficiários dos pagamentos indevidos. Oportunamente, condeno as demandada ao pagamento das custas e despesas processuais e dos honorários do advogado da parte adversa, que fixo, nos termos do art. 85, §2º, do Código de Processo Civil, e considerada a complexidade da demanda e as intervenções que exigiu, em 15% (quinze por cento) sobre o valor atualizado da condenação. Por fim, de modo a evitar o ajuizamento de embargos de declaração meramente protelatórios, registre-se que, ficam preteridas as demais alegações, por incompatíveis com a linha de raciocínio adotada, observando que os pedidos de ambas as partes foram apreciados nos limites em que foram formulados. Com efeito, ficam as partes advertidas, desde logo, que a oposição de embargos de declaração fora das hipóteses legais e/ou com postulação meramente infringente lhes sujeitará a imposição da multa prevista pelo artigo 1026, §2º, do Código de Processo Civil. Publique-se. Registre-se. Intimem-se.<br><b>Vencimento: </b>16/12/2020
    			</span>

    		</td>
    	</tr>






















    	<tr class="fundoClaro containerMovimentacao" style="">
    		<td class="dataMovimentacao" width="120" style="vertical-align: top">
    			23/09/2020
    		</td>
    		<td width="20" valign="top" aria-hidden="true">

    		</td>
    		<td class="descricaoMovimentacao" style="vertical-align: top; padding-bottom: 5px">




    					Conclusos



    			<br>
    			<span style="font-style: italic;">

    			</span>

    		</td>
    	</tr>






















    	<tr class="fundoEscuro containerMovimentacao" style="">
    		<td class="dataMovimentacao" width="120" style="vertical-align: top">
    			16/08/2020
    		</td>
    		<td width="20" valign="top" aria-hidden="true">








    				<a class="linkMovVincProc" id="linkMovVincProc-34722317" title="Visualizar documento em inteiro teor" href="/cpopg/abrirDocumentoVinculadoMovimentacao.do?processo.codigo=01000O7550000&amp;cdDocumento=34722317&amp;nmRecursoAcessado=Visto+em+Autoinspe%C3%A7%C3%A3o" target="_blank">
    					<img width="16" height="16" border="0" src="/cpopg/imagens/doc.png">
    				</a>

    		</td>
    		<td class="descricaoMovimentacao" style="vertical-align: top; padding-bottom: 5px">



    					<a class="linkMovVincProc" id="linkMovVincProc-2-34722317" title="Visualizar documento em inteiro teor" href="/cpopg/abrirDocumentoVinculadoMovimentacao.do?processo.codigo=01000O7550000&amp;cdDocumento=34722317&amp;nmRecursoAcessado=Visto+em+Autoinspe%C3%A7%C3%A3o" target="_blank"> Visto em Autoinspeção
    					</a>




    			<br>
    			<span style="font-style: italic;">
    				Despacho Visto em Autoinspeção
    			</span>

    		</td>
    	</tr>






















    	<tr class="fundoClaro containerMovimentacao" style="">
    		<td class="dataMovimentacao" width="120" style="vertical-align: top">
    			11/05/2020
    		</td>
    		<td width="20" valign="top" aria-hidden="true">

    		</td>
    		<td class="descricaoMovimentacao" style="vertical-align: top; padding-bottom: 5px">




    					Juntada de Documento



    			<br>
    			<span style="font-style: italic;">
    				Nº Protocolo: WMAC.20.70092549-0
    Tipo da Petição: Pedido de Andamento do proc./sent./decisões/desp.
    Data: 11/05/2020 13:28

    			</span>

    		</td>
    	</tr>






















    	<tr class="fundoEscuro containerMovimentacao" style="">
    		<td class="dataMovimentacao" width="120" style="vertical-align: top">
    			10/12/2019
    		</td>
    		<td width="20" valign="top" aria-hidden="true">

    		</td>
    		<td class="descricaoMovimentacao" style="vertical-align: top; padding-bottom: 5px">




    					Conclusos



    			<br>
    			<span style="font-style: italic;">

    			</span>

    		</td>
    	</tr>






















    	<tr class="fundoClaro containerMovimentacao" style="">
    		<td class="dataMovimentacao" width="120" style="vertical-align: top">
    			11/11/2019
    		</td>
    		<td width="20" valign="top" aria-hidden="true">








    				<a class="linkMovVincProc" id="linkMovVincProc-31112627" title="Visualizar documento em inteiro teor" href="/cpopg/abrirDocumentoVinculadoMovimentacao.do?processo.codigo=01000O7550000&amp;cdDocumento=31112627&amp;nmRecursoAcessado=Despacho+de+Mero+Expediente" target="_blank">
    					<img width="16" height="16" border="0" src="/cpopg/imagens/doc.png">
    				</a>

    		</td>
    		<td class="descricaoMovimentacao" style="vertical-align: top; padding-bottom: 5px">



    					<a class="linkMovVincProc" id="linkMovVincProc-2-31112627" title="Visualizar documento em inteiro teor" href="/cpopg/abrirDocumentoVinculadoMovimentacao.do?processo.codigo=01000O7550000&amp;cdDocumento=31112627&amp;nmRecursoAcessado=Despacho+de+Mero+Expediente" target="_blank"> Despacho de Mero Expediente
    					</a>




    			<br>
    			<span style="font-style: italic;">
    				DESPACHO Compulsando detidamente o feito, verifico que este inclui-se nos processos com prioridade de impulsionamento, consoante recomendação exarada pelo Conselho Nacional de Justiça, a qual determina a priorização de andamento das demandas paralisadas há mais de 100 (dias). Destarte, considerando que cada uma desses processos exige análise acurada por este magistrado a fim de que lhe seja dado efetivo provimento, determino a conclusão de todos os autos que se amoldem à hipótese alhures delineada - de competência do gabinete - para análise e devido impulsionamento, este especificamente, na fila concluso - impulso ao feito. Cumpra-se. Maceió(AL), 11 de novembro de 2019. José Cícero Alves da Silva Juiz de Direito
    			</span>

    		</td>
    	</tr>






















    	<tr class="fundoEscuro containerMovimentacao" style="">
    		<td class="dataMovimentacao" width="120" style="vertical-align: top">
    			12/07/2019
    		</td>
    		<td width="20" valign="top" aria-hidden="true">

    		</td>
    		<td class="descricaoMovimentacao" style="vertical-align: top; padding-bottom: 5px">




    					Juntada de Petição



    			<br>
    			<span style="font-style: italic;">
    				Nº Protocolo: WMAC.19.70150828-9
    Tipo da Petição: Petição
    Data: 11/07/2019 23:50

    			</span>

    		</td>
    	</tr>






















    	<tr class="fundoClaro containerMovimentacao" style="">
    		<td class="dataMovimentacao" width="120" style="vertical-align: top">
    			12/02/2019
    		</td>
    		<td width="20" valign="top" aria-hidden="true">

    		</td>
    		<td class="descricaoMovimentacao" style="vertical-align: top; padding-bottom: 5px">




    					Juntada de Petição



    			<br>
    			<span style="font-style: italic;">
    				Nº Protocolo: WMAC.19.70034823-7
    Tipo da Petição: Petição
    Data: 12/02/2019 14:58

    			</span>

    		</td>
    	</tr>






















    	<tr class="fundoEscuro containerMovimentacao" style="">
    		<td class="dataMovimentacao" width="120" style="vertical-align: top">
    			11/02/2019
    		</td>
    		<td width="20" valign="top" aria-hidden="true">

    		</td>
    		<td class="descricaoMovimentacao" style="vertical-align: top; padding-bottom: 5px">




    					Juntada de Petição



    			<br>
    			<span style="font-style: italic;">
    				Nº Protocolo: WMAC.19.70032532-6
    Tipo da Petição: Petição
    Data: 11/02/2019 09:13

    			</span>

    		</td>
    	</tr>






















    	<tr class="fundoClaro containerMovimentacao" style="">
    		<td class="dataMovimentacao" width="120" style="vertical-align: top">
    			06/12/2018
    		</td>
    		<td width="20" valign="top" aria-hidden="true">

    		</td>
    		<td class="descricaoMovimentacao" style="vertical-align: top; padding-bottom: 5px">




    					Conclusos



    			<br>
    			<span style="font-style: italic;">

    			</span>

    		</td>
    	</tr>






















    	<tr class="fundoEscuro containerMovimentacao" style="">
    		<td class="dataMovimentacao" width="120" style="vertical-align: top">
    			05/12/2018
    		</td>
    		<td width="20" valign="top" aria-hidden="true">

    		</td>
    		<td class="descricaoMovimentacao" style="vertical-align: top; padding-bottom: 5px">




    					Juntada de Petição



    			<br>
    			<span style="font-style: italic;">
    				Nº Protocolo: WMAC.18.70259903-1
    Tipo da Petição: Petição
    Data: 05/12/2018 16:46

    			</span>

    		</td>
    	</tr>






















    	<tr class="fundoClaro containerMovimentacao" style="">
    		<td class="dataMovimentacao" width="120" style="vertical-align: top">
    			29/11/2018
    		</td>
    		<td width="20" valign="top" aria-hidden="true">

    		</td>
    		<td class="descricaoMovimentacao" style="vertical-align: top; padding-bottom: 5px">




    					Juntada de Petição



    			<br>
    			<span style="font-style: italic;">
    				Nº Protocolo: WMAC.18.70255192-6
    Tipo da Petição: Petição
    Data: 29/11/2018 15:07

    			</span>

    		</td>
    	</tr>






















    	<tr class="fundoEscuro containerMovimentacao" style="">
    		<td class="dataMovimentacao" width="120" style="vertical-align: top">
    			28/11/2018
    		</td>
    		<td width="20" valign="top" aria-hidden="true">

    		</td>
    		<td class="descricaoMovimentacao" style="vertical-align: top; padding-bottom: 5px">




    					Ato Publicado



    			<br>
    			<span style="font-style: italic;">
    				Relação :0499/2018
    Data da Publicação: 29/11/2018
    Número do Diário: 2233
    			</span>

    		</td>
    	</tr>






















    	<tr class="fundoClaro containerMovimentacao" style="">
    		<td class="dataMovimentacao" width="120" style="vertical-align: top">
    			27/11/2018
    		</td>
    		<td width="20" valign="top" aria-hidden="true">

    		</td>
    		<td class="descricaoMovimentacao" style="vertical-align: top; padding-bottom: 5px">




    					Disponibilização no Diário da Justiça Eletrônico



    			<br>
    			<span style="font-style: italic;">
    				Relação: 0499/2018
    Teor do ato: ATO ORDINATÓRIO Em cumprimento ao disposto no art. 152,VI do CPC, procedo à intimação das partes para especificarem e justificarem as provas que ainda pretendem produzir, fundamentamente, pelo prazo comum de 5(cinco) dias. Maceió, 27 de novembro de 2018
    Advogados(s): Orlando de Moura Cavalcante Neto (OAB 7313/AL), Thiago Maia Nobre Rocha (OAB 6213/AL), Vinicius Faria de Cerqueira (OAB 9008/AL), Rafael Sganzerla Durand (OAB 10132A/AL), Marcus Vinicius Cavalcante Lins Filho (OAB 10871/AL)
    			</span>

    		</td>
    	</tr>






















    	<tr class="fundoEscuro containerMovimentacao" style="">
    		<td class="dataMovimentacao" width="120" style="vertical-align: top">
    			27/11/2018
    		</td>
    		<td width="20" valign="top" aria-hidden="true">








    				<a class="linkMovVincProc" id="linkMovVincProc-26689702" title="Visualizar documento em inteiro teor" href="#liberarAutoPorSenha">
    					<img width="16" height="16" border="0" src="/cpopg/imagens/doc.png">
    				</a>

    		</td>
    		<td class="descricaoMovimentacao" style="vertical-align: top; padding-bottom: 5px">



    					<a class="linkMovVincProc" id="linkMovVincProc-2-26689702" title="Visualizar documento em inteiro teor" href="#liberarAutoPorSenha"> Ato ordinatório praticado
    					</a>




    			<br>
    			<span style="font-style: italic;">
    				ATO ORDINATÓRIO Em cumprimento ao disposto no art. 152,VI do CPC, procedo à intimação das partes para especificarem e justificarem as provas que ainda pretendem produzir, fundamentamente, pelo prazo comum de 5(cinco) dias. Maceió, 27 de novembro de 2018
    			</span>

    		</td>
    	</tr>






















    	<tr class="fundoClaro containerMovimentacao" style="">
    		<td class="dataMovimentacao" width="120" style="vertical-align: top">
    			26/11/2018
    		</td>
    		<td width="20" valign="top" aria-hidden="true">

    		</td>
    		<td class="descricaoMovimentacao" style="vertical-align: top; padding-bottom: 5px">




    					Juntada de Documento



    			<br>
    			<span style="font-style: italic;">
    				Nº Protocolo: WMAC.18.70251514-8
    Tipo da Petição: Impugnação à Contestação
    Data: 26/11/2018 15:37

    			</span>

    		</td>
    	</tr>






















    	<tr class="fundoEscuro containerMovimentacao" style="">
    		<td class="dataMovimentacao" width="120" style="vertical-align: top">
    			26/11/2018
    		</td>
    		<td width="20" valign="top" aria-hidden="true">

    		</td>
    		<td class="descricaoMovimentacao" style="vertical-align: top; padding-bottom: 5px">




    					Juntada de Documento



    			<br>
    			<span style="font-style: italic;">
    				Nº Protocolo: WMAC.18.70251511-3
    Tipo da Petição: Impugnação à Contestação
    Data: 26/11/2018 15:35

    			</span>

    		</td>
    	</tr>






















    	<tr class="fundoClaro containerMovimentacao" style="">
    		<td class="dataMovimentacao" width="120" style="vertical-align: top">
    			09/11/2018
    		</td>
    		<td width="20" valign="top" aria-hidden="true">

    		</td>
    		<td class="descricaoMovimentacao" style="vertical-align: top; padding-bottom: 5px">




    					Ato Publicado



    			<br>
    			<span style="font-style: italic;">
    				Relação :0456/2018
    Data da Publicação: 12/11/2018
    Número do Diário: 2222
    			</span>

    		</td>
    	</tr>






















    	<tr class="fundoEscuro containerMovimentacao" style="">
    		<td class="dataMovimentacao" width="120" style="vertical-align: top">
    			08/11/2018
    		</td>
    		<td width="20" valign="top" aria-hidden="true">

    		</td>
    		<td class="descricaoMovimentacao" style="vertical-align: top; padding-bottom: 5px">




    					Disponibilização no Diário da Justiça Eletrônico



    			<br>
    			<span style="font-style: italic;">
    				Relação: 0456/2018
    Teor do ato: Autos n°: 0710802-55.2018.8.02.0001 Ação: Procedimento Ordinário Autor: José Carlos Cerqueira Souza Filho e outro Réu: Conaço Engenharia Ltda. e outro ATO ORDINATÓRIO Intimo a parte autora a apresentar, querendo, no prazo de 15 (quinze) dias, impugnação às contestações. Maceió, 06 de novembro de 2018 Hallph Sá de Araújo Analista Judiciário
    Advogados(s): Vinicius Faria de Cerqueira (OAB 9008/AL)
    			</span>

    		</td>
    	</tr>






















    	<tr class="fundoClaro containerMovimentacao" style="">
    		<td class="dataMovimentacao" width="120" style="vertical-align: top">
    			06/11/2018
    		</td>
    		<td width="20" valign="top" aria-hidden="true">








    				<a class="linkMovVincProc" id="linkMovVincProc-26414651" title="Visualizar documento em inteiro teor" href="#liberarAutoPorSenha">
    					<img width="16" height="16" border="0" src="/cpopg/imagens/doc.png">
    				</a>

    		</td>
    		<td class="descricaoMovimentacao" style="vertical-align: top; padding-bottom: 5px">



    					<a class="linkMovVincProc" id="linkMovVincProc-2-26414651" title="Visualizar documento em inteiro teor" href="#liberarAutoPorSenha"> Ato ordinatório praticado
    					</a>




    			<br>
    			<span style="font-style: italic;">
    				Autos n°: 0710802-55.2018.8.02.0001 Ação: Procedimento Ordinário Autor: José Carlos Cerqueira Souza Filho e outro Réu: Conaço Engenharia Ltda. e outro ATO ORDINATÓRIO Intimo a parte autora a apresentar, querendo, no prazo de 15 (quinze) dias, impugnação às contestações. Maceió, 06 de novembro de 2018 Hallph Sá de Araújo Analista Judiciário<br><b>Vencimento: </b>29/11/2018
    			</span>

    		</td>
    	</tr>






















    	<tr class="fundoEscuro containerMovimentacao" style="">
    		<td class="dataMovimentacao" width="120" style="vertical-align: top">
    			16/10/2018
    		</td>
    		<td width="20" valign="top" aria-hidden="true">

    		</td>
    		<td class="descricaoMovimentacao" style="vertical-align: top; padding-bottom: 5px">




    					Juntada de Documentos



    			<br>
    			<span style="font-style: italic;">
    				Nº Protocolo: WMAC.18.70221617-5
    Tipo da Petição: Contestação
    Data: 16/10/2018 14:43

    			</span>

    		</td>
    	</tr>






















    	<tr class="fundoClaro containerMovimentacao" style="">
    		<td class="dataMovimentacao" width="120" style="vertical-align: top">
    			10/10/2018
    		</td>
    		<td width="20" valign="top" aria-hidden="true">

    		</td>
    		<td class="descricaoMovimentacao" style="vertical-align: top; padding-bottom: 5px">




    					Juntada de Documentos



    			<br>
    			<span style="font-style: italic;">
    				Nº Protocolo: WMAC.18.70218154-1
    Tipo da Petição: Contestação
    Data: 10/10/2018 14:04

    			</span>

    		</td>
    	</tr>






















    	<tr class="fundoEscuro containerMovimentacao" style="">
    		<td class="dataMovimentacao" width="120" style="vertical-align: top">
    			24/09/2018
    		</td>
    		<td width="20" valign="top" aria-hidden="true">

    		</td>
    		<td class="descricaoMovimentacao" style="vertical-align: top; padding-bottom: 5px">




    					Juntada de Documento



    			<br>
    			<span style="font-style: italic;">

    			</span>

    		</td>
    	</tr>






















    	<tr class="fundoClaro containerMovimentacao" style="">
    		<td class="dataMovimentacao" width="120" style="vertical-align: top">
    			24/09/2018
    		</td>
    		<td width="20" valign="top" aria-hidden="true">

    		</td>
    		<td class="descricaoMovimentacao" style="vertical-align: top; padding-bottom: 5px">




    					Juntada de Documento



    			<br>
    			<span style="font-style: italic;">

    			</span>

    		</td>
    	</tr>






















    	<tr class="fundoEscuro containerMovimentacao" style="">
    		<td class="dataMovimentacao" width="120" style="vertical-align: top">
    			24/09/2018
    		</td>
    		<td width="20" valign="top" aria-hidden="true">








    				<a class="linkMovVincProc" id="linkMovVincProc-25822019" title="Visualizar documento em inteiro teor" href="#liberarAutoPorSenha">
    					<img width="16" height="16" border="0" src="/cpopg/imagens/doc.png">
    				</a>

    		</td>
    		<td class="descricaoMovimentacao" style="vertical-align: top; padding-bottom: 5px">



    					<a class="linkMovVincProc" id="linkMovVincProc-2-25822019" title="Visualizar documento em inteiro teor" href="#liberarAutoPorSenha"> Audiência Realizada
    					</a>




    			<br>
    			<span style="font-style: italic;">
    				Assentada - Genérico
    			</span>

    		</td>
    	</tr>






















    	<tr class="fundoClaro containerMovimentacao" style="">
    		<td class="dataMovimentacao" width="120" style="vertical-align: top">
    			24/09/2018
    		</td>
    		<td width="20" valign="top" aria-hidden="true">

    		</td>
    		<td class="descricaoMovimentacao" style="vertical-align: top; padding-bottom: 5px">




    					Juntada de Petição



    			<br>
    			<span style="font-style: italic;">
    				Nº Protocolo: WMAC.18.70203989-3
    Tipo da Petição: Petição
    Data: 24/09/2018 10:09

    			</span>

    		</td>
    	</tr>






















    	<tr class="fundoEscuro containerMovimentacao" style="">
    		<td class="dataMovimentacao" width="120" style="vertical-align: top">
    			21/09/2018
    		</td>
    		<td width="20" valign="top" aria-hidden="true">

    		</td>
    		<td class="descricaoMovimentacao" style="vertical-align: top; padding-bottom: 5px">




    					Juntada de Petição



    			<br>
    			<span style="font-style: italic;">
    				Nº Protocolo: WMAC.18.70203544-8
    Tipo da Petição: Petição
    Data: 21/09/2018 18:07

    			</span>

    		</td>
    	</tr>






















    	<tr class="fundoClaro containerMovimentacao" style="">
    		<td class="dataMovimentacao" width="120" style="vertical-align: top">
    			21/09/2018
    		</td>
    		<td width="20" valign="top" aria-hidden="true">

    		</td>
    		<td class="descricaoMovimentacao" style="vertical-align: top; padding-bottom: 5px">




    					Juntada de Petição



    			<br>
    			<span style="font-style: italic;">
    				Nº Protocolo: WMAC.18.70203528-6
    Tipo da Petição: Petição
    Data: 21/09/2018 17:42

    			</span>

    		</td>
    	</tr>






















    	<tr class="fundoEscuro containerMovimentacao" style="">
    		<td class="dataMovimentacao" width="120" style="vertical-align: top">
    			21/09/2018
    		</td>
    		<td width="20" valign="top" aria-hidden="true">

    		</td>
    		<td class="descricaoMovimentacao" style="vertical-align: top; padding-bottom: 5px">




    					Juntada de Petição



    			<br>
    			<span style="font-style: italic;">
    				Nº Protocolo: WMAC.18.70203260-0
    Tipo da Petição: Petição
    Data: 21/09/2018 13:58

    			</span>

    		</td>
    	</tr>






















    	<tr class="fundoClaro containerMovimentacao" style="">
    		<td class="dataMovimentacao" width="120" style="vertical-align: top">
    			20/09/2018
    		</td>
    		<td width="20" valign="top" aria-hidden="true">








    				<a class="linkMovVincProc" id="linkMovVincProc-25787004" title="Visualizar documento em inteiro teor" href="/cpopg/abrirDocumentoVinculadoMovimentacao.do?processo.codigo=01000O7550000&amp;cdDocumento=25787004&amp;nmRecursoAcessado=Visto+em+correi%C3%A7%C3%A3o" target="_blank">
    					<img width="16" height="16" border="0" src="/cpopg/imagens/doc.png">
    				</a>

    		</td>
    		<td class="descricaoMovimentacao" style="vertical-align: top; padding-bottom: 5px">



    					<a class="linkMovVincProc" id="linkMovVincProc-2-25787004" title="Visualizar documento em inteiro teor" href="/cpopg/abrirDocumentoVinculadoMovimentacao.do?processo.codigo=01000O7550000&amp;cdDocumento=25787004&amp;nmRecursoAcessado=Visto+em+correi%C3%A7%C3%A3o" target="_blank"> Visto em correição
    					</a>




    			<br>
    			<span style="font-style: italic;">
    				DESPACHO VISTO EM CORREIÇÃO
    			</span>

    		</td>
    	</tr>






















    	<tr class="fundoEscuro containerMovimentacao" style="">
    		<td class="dataMovimentacao" width="120" style="vertical-align: top">
    			06/06/2018
    		</td>
    		<td width="20" valign="top" aria-hidden="true">

    		</td>
    		<td class="descricaoMovimentacao" style="vertical-align: top; padding-bottom: 5px">




    					Juntada de AR - Cumprido



    			<br>
    			<span style="font-style: italic;">
    				Em 06  de  junho  de  2018 é juntado a estes autos o aviso de recebimento (AR803969759TJ - Cumprido), referente  ao  ofício  n. 0710802-55.2018.8.02.0001-0002, emitido para Conaço Engenharia Ltda.. Usuário:
    			</span>

    		</td>
    	</tr>






















    	<tr class="fundoClaro containerMovimentacao" style="">
    		<td class="dataMovimentacao" width="120" style="vertical-align: top">
    			06/06/2018
    		</td>
    		<td width="20" valign="top" aria-hidden="true">

    		</td>
    		<td class="descricaoMovimentacao" style="vertical-align: top; padding-bottom: 5px">




    					Juntada de AR - Cumprido



    			<br>
    			<span style="font-style: italic;">
    				Em 06  de  junho  de  2018 é juntado a estes autos o aviso de recebimento (AR803969745TJ - Cumprido), referente  ao  ofício  n. 0710802-55.2018.8.02.0001-0001, emitido para Banco do Brasil S A. Usuário:
    			</span>

    		</td>
    	</tr>






















    	<tr class="fundoEscuro containerMovimentacao" style="">
    		<td class="dataMovimentacao" width="120" style="vertical-align: top">
    			15/05/2018
    		</td>
    		<td width="20" valign="top" aria-hidden="true">

    		</td>
    		<td class="descricaoMovimentacao" style="vertical-align: top; padding-bottom: 5px">




    					Ato Publicado



    			<br>
    			<span style="font-style: italic;">
    				Relação :0220/2018
    Data da Publicação: 16/05/2018
    Número do Diário: 2105
    			</span>

    		</td>
    	</tr>






















    	<tr class="fundoClaro containerMovimentacao" style="">
    		<td class="dataMovimentacao" width="120" style="vertical-align: top">
    			15/05/2018
    		</td>
    		<td width="20" valign="top" aria-hidden="true">

    		</td>
    		<td class="descricaoMovimentacao" style="vertical-align: top; padding-bottom: 5px">




    					Ato Publicado



    			<br>
    			<span style="font-style: italic;">
    				Relação :0220/2018
    Data da Publicação: 16/05/2018
    Número do Diário: 2105
    			</span>

    		</td>
    	</tr>






















    	<tr class="fundoEscuro containerMovimentacao" style="">
    		<td class="dataMovimentacao" width="120" style="vertical-align: top">
    			11/05/2018
    		</td>
    		<td width="20" valign="top" aria-hidden="true">

    		</td>
    		<td class="descricaoMovimentacao" style="vertical-align: top; padding-bottom: 5px">




    					Disponibilização no Diário da Justiça Eletrônico



    			<br>
    			<span style="font-style: italic;">
    				Relação: 0220/2018
    Teor do ato: DECISÃOTrata-se de ação ordinária de indenização por danos morais e materias c/c obrigação de fazer c/c declaração de nulidade de contrato de financiamento bancário c/c pedido de tutela antecipada proposta por JOSÉ CARLOS CERQUEIRA SOUZA FILHO e LIVIA NASCIMENTO DA ROCHA, qualificados na inicial, em face de a CONY ENGENHARIA LTDA. e BANCO DO BRASIL, igualmente qualificados.Narra a exordial que os autores adquiriram o apartamento residencial de nº 502, da Torre I, do Empreendimento Residencial Dellavia Park Club, situado na Ladeira Murilo Monteiro Valente, n.º 375, no bairro do Barro Duro, Maceió/AL, cuja vendedora foi a ré CONY ENGENHARIA LTDA., pelo valor de R$ 232.000,00 (duzentos e trinta e dois mil reais).Segue narrando que o instrumento celebrado em 02/12/2013 previa a entrega do imóvel no prazo de 36 (trinta e seis) meses contados do início da obra, sendo admitida uma tolerância de no máximo 18 (dezoito) meses. Dentro dessa perspectiva, foi prometido que a obra seria iniciada em no máximo 60 (sessenta) dias da assinatura do contrato, ou seja seria iniciada em 02/02/2014 com previsão de entrega para 02/02/2017, porém, até a presente data a obra não foi concluída.Aduz que os demandantes ainda sendo cobrados ilegalmente pelo BANCO DO BRASIL, também réu da ação, numa suposta "taxa de obra", que decorre de financiamento bancário.Requer, em sede de tutela de urgência, que seja determinado ao BANCO DO BRASIL a SUSPENSÃO da cobrança de taxa de Obra.É o relatório. Decido.Ab initio, concedo aos Demandantes as benesses da assistência judiciária gratuita, em respeito as determinações contidas no art. 98 e art. 99 da Lei nº. 13.105/2015 (Código de Processo Civil - CPC/2015).O Código de Defesa do Consumidor, em seu art. 6.º, VIII, assegura como direito básico do consumidor a facilitação da defesa de seus direitos, inclusive com a inversão do ônus da prova, a seu favor, quando, a critério do juiz, for verossímil a alegação ou quando for ele hipossuficiente, segundo as regras ordinárias de experiência. Busca-se, assim assegurar a igualdade material.Em que pese bastar apenas um dos requisitos para a inversão, o caso em tela preenche as duas condições. Assim com fulcro no art. 6.º, VIII, do CDC DECIDO POR INVERTER O ÔNUS DA PROVA.Passo a apreciar o pedido de tutela provisória de urgência.Segundo o art. 300 do CPC/15, a tutela de urgência será concedida quando houver elementos que evidenciem a probabilidade do direito e o perigo de dano ou o risco ao resultado útil do processo. O dispositivo deixa evidentes os requisitos da tutela antecipada de urgência, quais sejam, a probabilidade do direito, doutrinariamente conhecida como fumus boni iuris, e o perigo de dano ou risco ao resultado útil do processo, chamado periculum in mora.Nesse trilhar, importa esclarecer que a tutela de urgência antecipada se funda em um Juízo de cognição sumária, de modo que a medida, quando concedida, será precária, haja vista ser fundamental a necessidade de ser reversível (300, §3º, do CPC/2015).Portanto, a antecipação provisória dos efeitos finais da tutela definitiva, permite o gozo antecipado e imediato dos efeitos próprios da tutela definitiva pretendida, mas não se funda em um juízo de valor exauriente, de modo que pode ser desconstituída a qualquer tempo.Nessa esteira de pensamento, passa-se a analisar o caso concreto e o preenchimento dos requisitos necessários à concessão da tutela provisória pretendida.No caso em tela, pretende a parte autora a suspensão da cobrança da "taxa de obra", em razão do suposto descumprimento contratual por parte da demandada no tocante ao prazo estabelecido para a entrega do imóvel.Conforme se extrai dos autos, as partes firmaram um contrato de compra e venda de um apartamento, tendo sido estipulada o prazo para sua entrega em 36 (trinta e seis) meses, com um prazo de tolerância de 18 (dezoito) meses, consoante cláusula quarta do contrato (fls.39). Logo o prazo final para entrega do imóvel se encerra em 02/08/2018, levando em consideração o prazo de tolerância estabelecido no contrato.É cediço que a taxa de evolução de obra é devida desde a aprovação do financiamento até o término da obra.&nbsp;Portanto, se a obra atrasar, é devido o pagamento da referida taxa ao banco que financiou o imóvel, no caso, o Banco do Brasil, até a sua conclusão. Sendo certo que ocorrendo a mora da construtora requerida em relação à entrega do imóvel, a parte autora não pode ser penalizada com o pagamento de tal encargo.&nbsp;No entanto, no caso em deslinde, ainda não houve mora da construtora, haja vista que ainda não fora encerrado o prazo estimado para entrega do imóvel. Nesse ponto impende destacar que é legal a cláusula contratual que prevê a prorrogação do prazo razoável para entrega do imóvel, considerando o princípio pacta sunt servanda.&nbsp;Desta feita, verifica-se a ausência de probabilidade do direito da parte autora, haja vista que, consoante dito alhures, a taxa de evolução de obra é devida até a conclusão da obra, bem como que não houve mora por parte da construtora demandada, haja vista que não houve, ainda, atraso na entrega do imóvel, tendo em vista a cláusula que prevê prazo de tolerância para entrega do imóvel.Ante o exposto, por considerar ausente a probabilidade do direito (art. 300 do CPC/15), INDEFIRO o pedido de tutela de urgência requestado.Inclua-se o feito em pauta de audiência de conciliação. Cite-se a parte ré eintime-a desta decisão, bem como para que compareça à audiência na data designada pelo Cartório, o que deve ser feito com antecedência mínima de 20 dias.Intime-se os autores por advogado constituído (art. 334, §3º, CPC/15).Deverá a parte ré ser advertida da possibilidade do art. 334, §5º, bem como do termo inicial do prazo de contestação (art. 335).Fiquem as partes advertidas, ainda, de que o não comparecimento injustificado à audiência de conciliação é considerado ato atentatório à dignidade da justiça e será sancionado com multa de até dois por cento da vantagem econômica pretendida ou do valor da causa (art. 334, §8º).Publique-se. Intime-seMaceió, 10 de maio de 2018.Henrique Gomes de Barros TeixeiraJuiz de Direito
    Advogados(s): Vinicius Faria de Cerqueira (OAB 9008/AL)
    			</span>

    		</td>
    	</tr>






















    	<tr class="fundoClaro containerMovimentacao" style="">
    		<td class="dataMovimentacao" width="120" style="vertical-align: top">
    			11/05/2018
    		</td>
    		<td width="20" valign="top" aria-hidden="true">

    		</td>
    		<td class="descricaoMovimentacao" style="vertical-align: top; padding-bottom: 5px">




    					Disponibilização no Diário da Justiça Eletrônico



    			<br>
    			<span style="font-style: italic;">
    				Relação: 0220/2018
    Teor do ato: Conciliação
    Data: 24/09/2018 Hora 14:00
    Local: Sala de Audiência
    Situacão: Pendente
    Advogados(s): Vinicius Faria de Cerqueira (OAB 9008/AL)
    			</span>

    		</td>
    	</tr>






















    	<tr class="fundoEscuro containerMovimentacao" style="">
    		<td class="dataMovimentacao" width="120" style="vertical-align: top">
    			11/05/2018
    		</td>
    		<td width="20" valign="top" aria-hidden="true">








    				<a class="linkMovVincProc" id="linkMovVincProc-24228218" title="Visualizar documento em inteiro teor" href="#liberarAutoPorSenha">
    					<img width="16" height="16" border="0" src="/cpopg/imagens/doc.png">
    				</a>

    		</td>
    		<td class="descricaoMovimentacao" style="vertical-align: top; padding-bottom: 5px">



    					<a class="linkMovVincProc" id="linkMovVincProc-2-24228218" title="Visualizar documento em inteiro teor" href="#liberarAutoPorSenha"> Carta Expedida
    					</a>




    			<br>
    			<span style="font-style: italic;">
    				AR DIGITAL - Citação e Intimação - Audiência de Instrução e Julgamento - Juizado
    			</span>

    		</td>
    	</tr>






















    	<tr class="fundoClaro containerMovimentacao" style="">
    		<td class="dataMovimentacao" width="120" style="vertical-align: top">
    			11/05/2018
    		</td>
    		<td width="20" valign="top" aria-hidden="true">








    				<a class="linkMovVincProc" id="linkMovVincProc-24228179" title="Visualizar documento em inteiro teor" href="#liberarAutoPorSenha">
    					<img width="16" height="16" border="0" src="/cpopg/imagens/doc.png">
    				</a>

    		</td>
    		<td class="descricaoMovimentacao" style="vertical-align: top; padding-bottom: 5px">



    					<a class="linkMovVincProc" id="linkMovVincProc-2-24228179" title="Visualizar documento em inteiro teor" href="#liberarAutoPorSenha"> Carta Expedida
    					</a>




    			<br>
    			<span style="font-style: italic;">
    				AR DIGITAL - Citação e Intimação - Audiência de Instrução e Julgamento - Juizado
    			</span>

    		</td>
    	</tr>






















    	<tr class="fundoEscuro containerMovimentacao" style="">
    		<td class="dataMovimentacao" width="120" style="vertical-align: top">
    			11/05/2018
    		</td>
    		<td width="20" valign="top" aria-hidden="true">

    		</td>
    		<td class="descricaoMovimentacao" style="vertical-align: top; padding-bottom: 5px">




    					Audiência Designada



    			<br>
    			<span style="font-style: italic;">
    				Conciliação
    Data: 24/09/2018 Hora 14:00
    Local: Sala de Audiência
    Situacão: Realizada
    			</span>

    		</td>
    	</tr>






















    	<tr class="fundoClaro containerMovimentacao" style="">
    		<td class="dataMovimentacao" width="120" style="vertical-align: top">
    			10/05/2018
    		</td>
    		<td width="20" valign="top" aria-hidden="true">








    				<a class="linkMovVincProc" id="linkMovVincProc-24187801" title="Visualizar documento em inteiro teor" href="/cpopg/abrirDocumentoVinculadoMovimentacao.do?processo.codigo=01000O7550000&amp;cdDocumento=24187801&amp;nmRecursoAcessado=N%C3%A3o+Concedida+a+Antecipa%C3%A7%C3%A3o+de+tutela" target="_blank">
    					<img width="16" height="16" border="0" src="/cpopg/imagens/doc.png">
    				</a>

    		</td>
    		<td class="descricaoMovimentacao" style="vertical-align: top; padding-bottom: 5px">



    					<a class="linkMovVincProc" id="linkMovVincProc-2-24187801" title="Visualizar documento em inteiro teor" href="/cpopg/abrirDocumentoVinculadoMovimentacao.do?processo.codigo=01000O7550000&amp;cdDocumento=24187801&amp;nmRecursoAcessado=N%C3%A3o+Concedida+a+Antecipa%C3%A7%C3%A3o+de+tutela" target="_blank"> Não Concedida a Antecipação de tutela
    					</a>




    			<br>
    			<span style="font-style: italic;">
    				DECISÃOTrata-se de ação ordinária de indenização por danos morais e materias c/c obrigação de fazer c/c declaração de nulidade de contrato de financiamento bancário c/c pedido de tutela antecipada proposta por JOSÉ CARLOS CERQUEIRA SOUZA FILHO e LIVIA NASCIMENTO DA ROCHA, qualificados na inicial, em face de a CONY ENGENHARIA LTDA. e BANCO DO BRASIL, igualmente qualificados.Narra a exordial que os autores adquiriram o apartamento residencial de nº 502, da Torre I, do Empreendimento Residencial Dellavia Park Club, situado na Ladeira Murilo Monteiro Valente, n.º 375, no bairro do Barro Duro, Maceió/AL, cuja vendedora foi a ré CONY ENGENHARIA LTDA., pelo valor de R$ 232.000,00 (duzentos e trinta e dois mil reais).Segue narrando que o instrumento celebrado em 02/12/2013 previa a entrega do imóvel no prazo de 36 (trinta e seis) meses contados do início da obra, sendo admitida uma tolerância de no máximo 18 (dezoito) meses. Dentro dessa perspectiva, foi prometido que a obra seria iniciada em no máximo 60 (sessenta) dias da assinatura do contrato, ou seja seria iniciada em 02/02/2014 com previsão de entrega para 02/02/2017, porém, até a presente data a obra não foi concluída.Aduz que os demandantes ainda sendo cobrados ilegalmente pelo BANCO DO BRASIL, também réu da ação, numa suposta "taxa de obra", que decorre de financiamento bancário.Requer, em sede de tutela de urgência, que seja determinado ao BANCO DO BRASIL a SUSPENSÃO da cobrança de taxa de Obra.É o relatório. Decido.Ab initio, concedo aos Demandantes as benesses da assistência judiciária gratuita, em respeito as determinações contidas no art. 98 e art. 99 da Lei nº. 13.105/2015 (Código de Processo Civil - CPC/2015).O Código de Defesa do Consumidor, em seu art. 6.º, VIII, assegura como direito básico do consumidor a facilitação da defesa de seus direitos, inclusive com a inversão do ônus da prova, a seu favor, quando, a critério do juiz, for verossímil a alegação ou quando for ele hipossuficiente, segundo as regras ordinárias de experiência. Busca-se, assim assegurar a igualdade material.Em que pese bastar apenas um dos requisitos para a inversão, o caso em tela preenche as duas condições. Assim com fulcro no art. 6.º, VIII, do CDC DECIDO POR INVERTER O ÔNUS DA PROVA.Passo a apreciar o pedido de tutela provisória de urgência.Segundo o art. 300 do CPC/15, a tutela de urgência será concedida quando houver elementos que evidenciem a probabilidade do direito e o perigo de dano ou o risco ao resultado útil do processo. O dispositivo deixa evidentes os requisitos da tutela antecipada de urgência, quais sejam, a probabilidade do direito, doutrinariamente conhecida como fumus boni iuris, e o perigo de dano ou risco ao resultado útil do processo, chamado periculum in mora.Nesse trilhar, importa esclarecer que a tutela de urgência antecipada se funda em um Juízo de cognição sumária, de modo que a medida, quando concedida, será precária, haja vista ser fundamental a necessidade de ser reversível (300, §3º, do CPC/2015).Portanto, a antecipação provisória dos efeitos finais da tutela definitiva, permite o gozo antecipado e imediato dos efeitos próprios da tutela definitiva pretendida, mas não se funda em um juízo de valor exauriente, de modo que pode ser desconstituída a qualquer tempo.Nessa esteira de pensamento, passa-se a analisar o caso concreto e o preenchimento dos requisitos necessários à concessão da tutela provisória pretendida.No caso em tela, pretende a parte autora a suspensão da cobrança da "taxa de obra", em razão do suposto descumprimento contratual por parte da demandada no tocante ao prazo estabelecido para a entrega do imóvel.Conforme se extrai dos autos, as partes firmaram um contrato de compra e venda de um apartamento, tendo sido estipulada o prazo para sua entrega em 36 (trinta e seis) meses, com um prazo de tolerância de 18 (dezoito) meses, consoante cláusula quarta do contrato (fls.39). Logo o prazo final para entrega do imóvel se encerra em 02/08/2018, levando em consideração o prazo de tolerância estabelecido no contrato.É cediço que a taxa de evolução de obra é devida desde a aprovação do financiamento até o término da obra.&nbsp;Portanto, se a obra atrasar, é devido o pagamento da referida taxa ao banco que financiou o imóvel, no caso, o Banco do Brasil, até a sua conclusão. Sendo certo que ocorrendo a mora da construtora requerida em relação à entrega do imóvel, a parte autora não pode ser penalizada com o pagamento de tal encargo.&nbsp;No entanto, no caso em deslinde, ainda não houve mora da construtora, haja vista que ainda não fora encerrado o prazo estimado para entrega do imóvel. Nesse ponto impende destacar que é legal a cláusula contratual que prevê a prorrogação do prazo razoável para entrega do imóvel, considerando o princípio pacta sunt servanda.&nbsp;Desta feita, verifica-se a ausência de probabilidade do direito da parte autora, haja vista que, consoante dito alhures, a taxa de evolução de obra é devida até a conclusão da obra, bem como que não houve mora por parte da construtora demandada, haja vista que não houve, ainda, atraso na entrega do imóvel, tendo em vista a cláusula que prevê prazo de tolerância para entrega do imóvel.Ante o exposto, por considerar ausente a probabilidade do direito (art. 300 do CPC/15), INDEFIRO o pedido de tutela de urgência requestado.Inclua-se o feito em pauta de audiência de conciliação. Cite-se a parte ré eintime-a desta decisão, bem como para que compareça à audiência na data designada pelo Cartório, o que deve ser feito com antecedência mínima de 20 dias.Intime-se os autores por advogado constituído (art. 334, §3º, CPC/15).Deverá a parte ré ser advertida da possibilidade do art. 334, §5º, bem como do termo inicial do prazo de contestação (art. 335).Fiquem as partes advertidas, ainda, de que o não comparecimento injustificado à audiência de conciliação é considerado ato atentatório à dignidade da justiça e será sancionado com multa de até dois por cento da vantagem econômica pretendida ou do valor da causa (art. 334, §8º).Publique-se. Intime-seMaceió, 10 de maio de 2018.Henrique Gomes de Barros TeixeiraJuiz de Direito<br><b>Vencimento: </b>01/06/2018
    			</span>

    		</td>
    	</tr>






















    	<tr class="fundoEscuro containerMovimentacao" style="">
    		<td class="dataMovimentacao" width="120" style="vertical-align: top">
    			03/05/2018
    		</td>
    		<td width="20" valign="top" aria-hidden="true">

    		</td>
    		<td class="descricaoMovimentacao" style="vertical-align: top; padding-bottom: 5px">




    					Conclusos



    			<br>
    			<span style="font-style: italic;">

    			</span>

    		</td>
    	</tr>






















    	<tr class="fundoClaro containerMovimentacao" style="">
    		<td class="dataMovimentacao" width="120" style="vertical-align: top">
    			02/05/2018
    		</td>
    		<td width="20" valign="top" aria-hidden="true">

    		</td>
    		<td class="descricaoMovimentacao" style="vertical-align: top; padding-bottom: 5px">




    					Conclusos



    			<br>
    			<span style="font-style: italic;">

    			</span>

    		</td>
    	</tr>






















    	<tr class="fundoEscuro containerMovimentacao" style="">
    		<td class="dataMovimentacao" width="120" style="vertical-align: top">
    			02/05/2018
    		</td>
    		<td width="20" valign="top" aria-hidden="true">

    		</td>
    		<td class="descricaoMovimentacao" style="vertical-align: top; padding-bottom: 5px">




    					Distribuído por Sorteio



    			<br>
    			<span style="font-style: italic;">

    			</span>

    		</td>
    	</tr>




    			</tbody>




    </table>

    	<div id="divLinksTituloBlocoMovimentacoes" style="text-align:right">










    <input id="mensagemNaoExibidamovimentacoes" type="hidden" value="">

        <input id="linkNaoExibidomovimentacoes" type="hidden" value="<span id=&quot;setasDireitamovimentacoes&quot; class=&quot;setasDireita&quot;><i class=&quot;unj-link-collapse__icon glyph glyph-chevron-up&quot;></i></span>Recolher">

    <span id="mensagensExibindomovimentacoes" class="mensagemExibindo">

    </span> &nbsp;

        <a id="linkmovimentacoes" href="javascript:" class="linkNaoSelecionado unj-link-collapse">
            <span id="setasDireitamovimentacoes" class="setasDireita">
                <i class="unj-link-collapse__icon glyph glyph-chevron-down"></i>
            </span>
            Mais
        </a>

    <script>
    	$(function() {
    		var controlarLink = function() {
    			var $linkNaoExibido = $('input#linkNaoExibidomovimentacoes');
    			var conteudoLinkNaoApresentado = $linkNaoExibido.val();
    			var $link = $('a#linkmovimentacoes');

    			$linkNaoExibido.val($link.html());
    			$link.html(conteudoLinkNaoApresentado);
    		};

    		var controlarMensagem = function() {
    			var $mensagemNaoExibida = $('input#mensagemNaoExibidamovimentacoes');
    			var $spanMensagem = $('span#mensagensExibindomovimentacoes');
    			var mensagemExibida = $spanMensagem.html();
    			var mensagemNaoExibida = $mensagemNaoExibida.val();

    			$spanMensagem.html(mensagemNaoExibida);
    			$mensagemNaoExibida.val(mensagemExibida);
    		};

    		var controlarMensagemLink = function() {
    			controlarMensagem();
    			controlarLink();
    		};

    		var esconderElementosExtrasMostrarDefault = function() {
    			$('#tabelaTodasMovimentacoes').hide();
    			$('#tabelaUltimasMovimentacoes').show();
    		};

    		var mostrarElementosExtrasEsconderDefault = function() {
    			$('#tabelaUltimasMovimentacoes').hide();
    			$('#tabelaTodasMovimentacoes').show();
    		};

    		var initPagina = function() {
                var setasDireita = '<span id="setasDireitamovimentacoes" class="setasDireita"><i class="unj-link-collapse__icon glyph glyph-chevron-up"></i></span>';
    			var $linkEscondido = $('input#linkNaoExibidomovimentacoes');
    			$linkEscondido.val(setasDireita+$linkEscondido.val());
    		};

    		var bindLink = function() {
    			var $link = $('a#linkmovimentacoes');
    			$link.funcToggle('click', mostrarElementosExtrasEsconderDefault, esconderElementosExtrasMostrarDefault);
    			$link.bind('click', controlarMensagemLink);
    		};

    		initPagina();
    		bindLink();
    		esconderElementosExtrasMostrarDefault();
    	});
    </script>

    	</div>







































    <div style="padding-top: 10px;">




    			<h2 class="subtitle tituloDoBloco">Petições diversas</h2>


    </div>

    <!-- Tabela de petições diversas -->
    <table style="margin-left:15px; margin-top:1px;" align="center" width="98%" border="0" cellspacing="0" cellpadding="1">


    			<thead>
    			    <tr class="label">
    			      <th width="140" style="text-align:left">Data</th>
    			      <th width="*">Tipo</th>
    			    </tr>
    			    <tr class="fundoEscuro" height="2" aria-hidden="true">
    					<td></td>
    					<td></td>
    				</tr>
    			</thead>
    			<tbody>


    						<tr class="fundoClaro">
    							<td width="140" style="text-align:left">
    								21/09/2018
    							</td>
    							<td width="*">
    								Petição <br>

    							</td>
    						</tr>



    						<tr class="fundoEscuro">
    							<td width="140" style="text-align:left">
    								21/09/2018
    							</td>
    							<td width="*">
    								Petição <br>

    							</td>
    						</tr>



    						<tr class="fundoClaro">
    							<td width="140" style="text-align:left">
    								21/09/2018
    							</td>
    							<td width="*">
    								Petição <br>

    							</td>
    						</tr>



    						<tr class="fundoEscuro">
    							<td width="140" style="text-align:left">
    								24/09/2018
    							</td>
    							<td width="*">
    								Petição <br>

    							</td>
    						</tr>



    						<tr class="fundoClaro">
    							<td width="140" style="text-align:left">
    								10/10/2018
    							</td>
    							<td width="*">
    								Contestação <br>

    							</td>
    						</tr>



    						<tr class="fundoEscuro">
    							<td width="140" style="text-align:left">
    								16/10/2018
    							</td>
    							<td width="*">
    								Contestação <br>

    							</td>
    						</tr>



    						<tr class="fundoClaro">
    							<td width="140" style="text-align:left">
    								26/11/2018
    							</td>
    							<td width="*">
    								Impugnação à Contestação <br>

    							</td>
    						</tr>



    						<tr class="fundoEscuro">
    							<td width="140" style="text-align:left">
    								26/11/2018
    							</td>
    							<td width="*">
    								Impugnação à Contestação <br>

    							</td>
    						</tr>



    						<tr class="fundoClaro">
    							<td width="140" style="text-align:left">
    								29/11/2018
    							</td>
    							<td width="*">
    								Petição <br>

    							</td>
    						</tr>



    						<tr class="fundoEscuro">
    							<td width="140" style="text-align:left">
    								05/12/2018
    							</td>
    							<td width="*">
    								Petição <br>

    							</td>
    						</tr>



    						<tr class="fundoClaro">
    							<td width="140" style="text-align:left">
    								11/02/2019
    							</td>
    							<td width="*">
    								Petição <br>

    							</td>
    						</tr>



    						<tr class="fundoEscuro">
    							<td width="140" style="text-align:left">
    								12/02/2019
    							</td>
    							<td width="*">
    								Petição <br>

    							</td>
    						</tr>



    						<tr class="fundoClaro">
    							<td width="140" style="text-align:left">
    								11/07/2019
    							</td>
    							<td width="*">
    								Petição <br>

    							</td>
    						</tr>



    						<tr class="fundoEscuro">
    							<td width="140" style="text-align:left">
    								11/05/2020
    							</td>
    							<td width="*">
    								Pedido de Andamento do proc./sent./decisões/desp. <br>

    							</td>
    						</tr>



    						<tr class="fundoClaro">
    							<td width="140" style="text-align:left">
    								15/12/2020
    							</td>
    							<td width="*">
    								Recurso de Apelação <br>

    							</td>
    						</tr>



    						<tr class="fundoEscuro">
    							<td width="140" style="text-align:left">
    								18/12/2020
    							</td>
    							<td width="*">
    								Recurso de Apelação <br>

    							</td>
    						</tr>



    						<tr class="fundoClaro">
    							<td width="140" style="text-align:left">
    								18/12/2020
    							</td>
    							<td width="*">
    								Juntada de Instrumento de Procuração <br>

    							</td>
    						</tr>



    						<tr class="fundoEscuro">
    							<td width="140" style="text-align:left">
    								10/02/2021
    							</td>
    							<td width="*">
    								Contrarrazões <br>

    							</td>
    						</tr>


    			</tbody>



    </table>
    <!--  Tabela de petições diversas -->




























    <script type="text/javascript">
    	(function($) {
    		$(function(){
    			var captcha = $.saj.getUrlParameter('uuidCaptcha');
    			if(!captcha){
    				return;
    			}
    			$('.incidente a').each(function(){
    				var $incidente = $(this);
    				var url = $incidente.attr('href');
    				$incidente.attr('href', url+'&uuidCaptcha='+captcha);
    			});
    		})
    	})(jQuery);
    </script>











    <div style="padding-top: 10px;">




    			<h2 class="subtitle tituloDoBloco">Incidentes, ações incidentais, recursos e execuções de sentenças</h2>


    </div>

    <table style="margin-left:15px; margin-top:1px;" align="center" width="98%" border="0" cellspacing="0" cellpadding="1">


    	    <tbody><tr class="label">
    	    	<th width="140">
    				Recebido em
    			</th>
    			<th width="*" class="label">
    				Classe
    			</th>
    	    </tr>
    	    <tr class="fundoEscuro" height="2" aria-hidden="true">
    			<td></td><td></td>
    		</tr>



    			<tr class="fundoClaro">
    			  <td width="140" style="text-align:left">
    			    05/05/2023
    			  </td>
    			<td width="*">


    						<a class="incidente" href="/cpopg/show.do?localPesquisa.cdLocal=1&amp;processo.codigo=01000O7550001&amp;processo.foro=1" target="_top">
    							Cumprimento de sentença

    								 - 00001


    						</a>



    			</td>
    		</tr>




    </tbody></table>
    <!--  Incidentes -->





































    <script type="text/javascript">
        (function ($) {
            $(function () {
                var captcha = $.saj.getUrlParameter('uuidCaptcha');

                if(!captcha){
                    return;
                }
                $.each($('.processoApensado'), function (i, value) {
                    var $link = $(value);
                    $link.attr('href', $link.attr('href') + '&uuidCaptcha=' + captcha);
                })

            })
        })(jQuery);
    </script>









    <div style="padding-top: 10px;">




    			<h2 class="subtitle tituloDoBloco">Apensos, Entranhados e Unificados</h2>


    </div>




            <table style="margin-left:15px; margin-top:1px;" align="center" width="98%" border="0" cellspacing="0" cellpadding="1">
                <tbody id="dadosApensosNaoDisponiveis">
                <tr>
                    <td colspan="3" align="left">Não há processos apensados, entranhados e unificados a este processo.</td>
                </tr>
                </tbody>
            </table>























    <div style="padding-top: 10px;">




    			<h2 class="subtitle tituloDoBloco">Audiências</h2>


    </div>
























    <a name="audienciasPlaceHolder"></a>
    <table style="margin-left:15px; margin-top:1px;" align="center" width="98%" border="0" cellspacing="0" cellpadding="1">


                <tbody><tr class="label">
                    <th align="left" valign="top" width="140">Data</th>
                    <th align="left" valign="top" width="*">Audiência</th>
                    <th align="left" valign="top" width="100">Situação</th>
                    <th align="left" valign="top" width="100">Qt. Pessoas</th>
                </tr>
                <tr class="fundoEscuro" height="2" aria-hidden="true">
                    <td colspan="4"></td>
                </tr>

                    <tr class="fundoClaro">
                        <td valign="top" align="left" width="140">
                            24/09/2018
                        </td>



                                <td valign="top" align="left" width="*">
                                    Conciliação
                                </td>



                        <td align="left" valign="top" width="100">
                            Realizada
                        </td>
                        <td align="left" valign="top" width="100">
                            7
                        </td>
                    </tr>




    </tbody></table>































    <form id="popupCdas" style="display: none;">
    	<!--  dados da lista (CDAs) -->
    	<div style="height:210px; overflow: auto;">
    		<table id="tableCdasPrincipais" style="margin-left:10px; margin-top:1px; width: 98%;">
    			<thead>
    				<tr class="fundoClaro">
    					<th style="text-align:left;">Número CDA</th>
    					<th style="text-align:left;">Valor</th>
    					<th style="text-align:left;">Dt. CDA</th>
    					<th style="text-align:left;">Valor atualizado</th>
    					<th style="text-align:left;">Dt. atualização</th>
    					<th style="text-align:left;">Situação</th>
    				</tr>
    				<tr class="fundoEscuro" height="2" aria-hidden="true">
    					<td colspan="6">
    				</td></tr>
    			</thead>
    			<tbody>

    			</tbody>
    		</table>
    	</div>
    </form>






















    	<form action="/cpopg/show.do?processo.codigo=01000O7550000&amp;processo.foro=1&amp;processo.numero=0710802-55.2018.8.02.0001" id="popupSenha" style="display: none;" method="POST">

    		<table role="document">
    			<tbody><tr>
    				<td colspan="2" style="padding-bottom:20px">Atendendo a resolução 121 do CNJ.</td>
    			</tr>

    				<tr>
    					<td colspan="2" style="padding-bottom:20px">Se for advogado(a) nesse processo, é necessário<span id="identificacao"><strong><a href="https://www2.tjal.jus.br/esaj/identificacao.do?retorno=https%3A//www2.tjal.jus.br/cpopg/show.do%3Fprocesso.codigo%3D01000O7550000%26processo.foro%3D1%26processo.numero%3D0710802-55.2018.8.02.0001">Identificar-se</a></strong></span></td>



    							<script language="javascript" type="text/JavaScript" src="https://www2.tjal.jus.br/sajcas/conteudoIdentificacao?script=1691279960142"></script>


    				</tr>

    			<tr align="center">
    				<td align="left" colspan="2" style="padding-bottom:20px">
    					<div style="float:left; line-height:30px;">Se for uma parte ou interessado, digite a senha do processo</div>
    					<div style="float:left;width: 140px; padding-left:15px">
    						<input type="password" name="senhaProcesso" maxlength="12" value="" rotulo="" class="form-control" id="senhaProcesso">
    						<input type="hidden" name="idRecursoQueProvocouLiberacaoPorSenha" value="">
    					</div>
    					<div class="unj-form-control-group__icon">
    						<div class="dropdown show">
    							<a href="javascript:;" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
    								<span class="glyph glyph-info" aria-hidden="true"></span>
    							</a>
    							<div class="dropdown-menu tooltip-campos" aria-labelledby="dropdownMenuLink">

    									É necessário informar uma senha para acessar processo em segredo de justiça, bem como para acessar autos dos demais processos.<br><br>
    									Se for parte do processo e ainda não possua uma senha, <b>solicite-a no cartório</b>.<br><br>


    							</div>
    						</div>
    					</div>
    				</td>
    			</tr>
    			<tr>
    				<td colspan="2" align="center">





















    	<input type="button" name="btFechar" value="Cancelar" onclick="" onmouseover="B_mOver(this);" onmouseout="B_mOut(this);" class="spwBotao " id="botaoFecharPopupSenha">






















    	<input type="submit" name="btEnviarSenha" value="Continuar" onclick="" onmouseover="B_mOver(this);" onmouseout="B_mOut(this);" class="spwBotaoDefault btn-space" id="btEnviarSenha">




    				</td>
    			</tr>
    		</tbody></table>
    	</form>





    </div>






















    <footer>
        <nav class="navbar__footer">
            <div class="navbar__footer__container">

                <ul class="navbar__footer__list-brand">
                    <li class="navbar__footer__list-brand__item">
                        <a href="https://www.softplan.com.br/solucoes/saj-tribunais/" class="navbar__footer__list-brand__item__link link_softplan_tribunais">
                            <img src="https://www2.tjal.jus.br/esaj/img/brand/icon-saj.png" alt="SAJ">
                        </a>
                    </li>
                    <li class="navbar__footer__list-brand__item">
                        <a href="https://www.softplan.com.br/" class="navbar__footer__list-brand__item__link link_softplan">
                            <img src="https://www2.tjal.jus.br/esaj/img/brand/icon-softplan.png" alt="Softplan">
                        </a>
                    </li>
                </ul>

                <ul class="navbar__footer__list-actions">
                </ul>
            </div>
        </nav>
    </footer>







    <script type="text/javascript">window.NREUM||(NREUM={});NREUM.info={"errorBeacon":"bam.nr-data.net","licenseKey":"b61bdf610d","agent":"","beacon":"bam.nr-data.net","applicationTime":253,"applicationID":"111652883","transactionName":"MlZRN0QECkMAVERZDgscYBdEEBBDIFREWQ4LHFERGAYLXU9EX1YVFV9SDRgWBVpPVEBfTxZHQRZCFkpRAkNZXw9LYFsMQSQHRAhYXg==","queueTime":0}</script>

    <div id="forest-ext-shadow-host"></div></body></html>
        """
    try:
        soup = BeautifulSoup(html, 'html.parser')
        return soup
    except Exception as e:
        print("Erro ao criar o objeto BeautifulSoup:", e)
        return None


def create_bs4_object_from_tjce():
    tjce_html_page = """
    <html><head>
    	<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
    	<meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">	










        <script language="javascript" type="text/JavaScript" src="https://esaj.tjce.jus.br/sajcas/verificarLogin.js?script=1691514670090"></script>

        <script language="javascript">
            if (window.sajcas && window.sajcas.usuarioLogadoNoCasServer) {
                var GATEWAY_TRUE = 'gateway=true', GATEWAY_FALSE = 'gateway=false';
                var urlRetornoSistema = '';
                if (urlRetornoSistema === '') {
                    urlRetornoSistema = window.location.href;
                }

                if (urlRetornoSistema.indexOf(GATEWAY_FALSE) !== -1) {
                    urlRetornoSistema = urlRetornoSistema.replace(GATEWAY_FALSE, GATEWAY_TRUE);
                } else {
                    urlRetornoSistema.lastIndexOf('?') !== -1 ? urlRetornoSistema += '&' : urlRetornoSistema += '?';
                    urlRetornoSistema += GATEWAY_TRUE;
                }

                window.location.href = urlRetornoSistema;
            }
        </script>


    	<title>Portal de Serviços e-SAJ</title>



    <script type="text/javascript">(window.NREUM||(NREUM={})).init={ajax:{deny_list:["bam.nr-data.net"]}};(window.NREUM||(NREUM={})).loader_config={licenseKey:"b61bdf610d",applicationID:"434000584"};;/*! For license information please see nr-loader-rum-1.237.1.min.js.LICENSE.txt */
    (()=>{"use strict";var e,t,n={5763:(e,t,n)=>{n.d(t,{P_:()=>f,Mt:()=>p,C5:()=>s,DL:()=>m,OP:()=>j,lF:()=>E,Yu:()=>y,Dg:()=>g,CX:()=>c,GE:()=>b,sU:()=>_});var r=n(8632),i=n(9567);const a={beacon:r.ce.beacon,errorBeacon:r.ce.errorBeacon,licenseKey:void 0,applicationID:void 0,sa:void 0,queueTime:void 0,applicationTime:void 0,ttGuid:void 0,user:void 0,account:void 0,product:void 0,extra:void 0,jsAttributes:{},userAttributes:void 0,atts:void 0,transactionName:void 0,tNamePlain:void 0},o={};function s(e){if(!e)throw new Error("All info objects require an agent identifier!");if(!o[e])throw new Error("Info for ".concat(e," was never set"));return o[e]}function c(e,t){if(!e)throw new Error("All info objects require an agent identifier!");o[e]=(0,i.D)(t,a),(0,r.Qy)(e,o[e],"info")}var d=n(7056);const u=()=>{const e={blockSelector:"[data-nr-block]",maskInputOptions:{password:!0}};return{allow_bfcache:!0,privacy:{cookies_enabled:!0},ajax:{deny_list:void 0,block_internal:!0,enabled:!0,harvestTimeSeconds:10},distributed_tracing:{enabled:void 0,exclude_newrelic_header:void 0,cors_use_newrelic_header:void 0,cors_use_tracecontext_headers:void 0,allowed_origins:void 0},session:{domain:void 0,expiresMs:d.oD,inactiveMs:d.Hb},ssl:void 0,obfuscate:void 0,jserrors:{enabled:!0,harvestTimeSeconds:10},metrics:{enabled:!0},page_action:{enabled:!0,harvestTimeSeconds:30},page_view_event:{enabled:!0},page_view_timing:{enabled:!0,harvestTimeSeconds:30,long_task:!1},session_trace:{enabled:!0,harvestTimeSeconds:10},harvest:{tooManyRequestsDelay:60},session_replay:{enabled:!1,harvestTimeSeconds:60,sampleRate:.1,errorSampleRate:.1,maskTextSelector:"*",maskAllInputs:!0,get blockClass(){return"nr-block"},get ignoreClass(){return"nr-ignore"},get maskTextClass(){return"nr-mask"},get blockSelector(){return e.blockSelector},set blockSelector(t){e.blockSelector+=",".concat(t)},get maskInputOptions(){return e.maskInputOptions},set maskInputOptions(t){e.maskInputOptions={...t,password:!0}}},spa:{enabled:!0,harvestTimeSeconds:10}}},l={};function f(e){if(!e)throw new Error("All configuration objects require an agent identifier!");if(!l[e])throw new Error("Configuration for ".concat(e," was never set"));return l[e]}function g(e,t){if(!e)throw new Error("All configuration objects require an agent identifier!");l[e]=(0,i.D)(t,u()),(0,r.Qy)(e,l[e],"config")}function p(e,t){if(!e)throw new Error("All configuration objects require an agent identifier!");var n=f(e);if(n){for(var r=t.split("."),i=0;i<r.length-1;i++)if("object"!=typeof(n=n[r[i]]))return;n=n[r[r.length-1]]}return n}const h={accountID:void 0,trustKey:void 0,agentID:void 0,licenseKey:void 0,applicationID:void 0,xpid:void 0},v={};function m(e){if(!e)throw new Error("All loader-config objects require an agent identifier!");if(!v[e])throw new Error("LoaderConfig for ".concat(e," was never set"));return v[e]}function b(e,t){if(!e)throw new Error("All loader-config objects require an agent identifier!");v[e]=(0,i.D)(t,h),(0,r.Qy)(e,v[e],"loader_config")}const y=(0,r.mF)().o;var w=n(385),A=n(6818);const x={buildEnv:A.Re,bytesSent:{},queryBytesSent:{},customTransaction:void 0,disabled:!1,distMethod:A.gF,isolatedBacklog:!1,loaderType:void 0,maxBytes:3e4,offset:Math.floor(w._A?.performance?.timeOrigin||w._A?.performance?.timing?.navigationStart||Date.now()),onerror:void 0,origin:""+w._A.location,ptid:void 0,releaseIds:{},session:void 0,xhrWrappable:"function"==typeof w._A.XMLHttpRequest?.prototype?.addEventListener,version:A.q4,denyList:void 0},D={};function j(e){if(!e)throw new Error("All runtime objects require an agent identifier!");if(!D[e])throw new Error("Runtime for ".concat(e," was never set"));return D[e]}function _(e,t){if(!e)throw new Error("All runtime objects require an agent identifier!");D[e]=(0,i.D)(t,x),(0,r.Qy)(e,D[e],"runtime")}function E(e){return function(e){try{const t=s(e);return!!t.licenseKey&&!!t.errorBeacon&&!!t.applicationID}catch(e){return!1}}(e)}},9567:(e,t,n)=>{n.d(t,{D:()=>i});var r=n(50);function i(e,t){try{if(!e||"object"!=typeof e)return(0,r.Z)("Setting a Configurable requires an object as input");if(!t||"object"!=typeof t)return(0,r.Z)("Setting a Configurable requires a model to set its initial properties");const n=Object.create(Object.getPrototypeOf(t),Object.getOwnPropertyDescriptors(t)),a=0===Object.keys(n).length?e:n;for(let o in a)if(void 0!==e[o])try{"object"==typeof e[o]&&"object"==typeof t[o]?n[o]=i(e[o],t[o]):n[o]=e[o]}catch(e){(0,r.Z)("An error occurred while setting a property of a Configurable",e)}return n}catch(e){(0,r.Z)("An error occured while setting a Configurable",e)}}},6818:(e,t,n)=>{n.d(t,{Re:()=>i,gF:()=>a,q4:()=>r});const r="1.237.1",i="PROD",a="CDN"},385:(e,t,n)=>{n.d(t,{FN:()=>o,IF:()=>d,Nk:()=>l,Tt:()=>s,_A:()=>a,il:()=>r,pL:()=>c,v6:()=>i,w1:()=>u});const r="undefined"!=typeof window&&!!window.document,i="undefined"!=typeof WorkerGlobalScope&&("undefined"!=typeof self&&self instanceof WorkerGlobalScope&&self.navigator instanceof WorkerNavigator||"undefined"!=typeof globalThis&&globalThis instanceof WorkerGlobalScope&&globalThis.navigator instanceof WorkerNavigator),a=r?window:"undefined"!=typeof WorkerGlobalScope&&("undefined"!=typeof self&&self instanceof WorkerGlobalScope&&self||"undefined"!=typeof globalThis&&globalThis instanceof WorkerGlobalScope&&globalThis),o=""+a?.location,s=/iPad|iPhone|iPod/.test(navigator.userAgent),c=s&&"undefined"==typeof SharedWorker,d=(()=>{const e=navigator.userAgent.match(/Firefox[/\s](\d+\.\d+)/);return Array.isArray(e)&&e.length>=2?+e[1]:0})(),u=Boolean(r&&window.document.documentMode),l=!!navigator.sendBeacon},1117:(e,t,n)=>{n.d(t,{w:()=>a});var r=n(50);const i={agentIdentifier:"",ee:void 0};class a{constructor(e){try{if("object"!=typeof e)return(0,r.Z)("shared context requires an object as input");this.sharedContext={},Object.assign(this.sharedContext,i),Object.entries(e).forEach((e=>{let[t,n]=e;Object.keys(i).includes(t)&&(this.sharedContext[t]=n)}))}catch(e){(0,r.Z)("An error occured while setting SharedContext",e)}}}},8e3:(e,t,n)=>{n.d(t,{L:()=>u,R:()=>c});var r=n(2177),i=n(1284),a=n(4322),o=n(3325);const s={};function c(e,t){const n={staged:!1,priority:o.p[t]||0};d(e),s[e].get(t)||s[e].set(t,n)}function d(e){e&&(s[e]||(s[e]=new Map))}function u(){let e=arguments.length>0&&void 0!==arguments[0]?arguments[0]:"",t=arguments.length>1&&void 0!==arguments[1]?arguments[1]:"feature";if(d(e),!e||!s[e].get(t))return o(t);s[e].get(t).staged=!0;const n=[...s[e]];function o(t){const n=e?r.ee.get(e):r.ee,o=a.X.handlers;if(n.backlog&&o){var s=n.backlog[t],c=o[t];if(c){for(var d=0;s&&d<s.length;++d)l(s[d],c);(0,i.D)(c,(function(e,t){(0,i.D)(t,(function(t,n){n[0].on(e,n[1])}))}))}delete o[t],n.backlog[t]=null,n.emit("drain-"+t,[])}}n.every((e=>{let[t,n]=e;return n.staged}))&&(n.sort(((e,t)=>e[1].priority-t[1].priority)),n.forEach((e=>{let[t]=e;o(t)})))}function l(e,t){var n=e[1];(0,i.D)(t[n],(function(t,n){var r=e[0];if(n[0]===r){var i=n[1],a=e[3],o=e[2];i.apply(a,o)}}))}},2177:(e,t,n)=>{n.d(t,{ee:()=>d});var r=n(8632),i=n(2210),a=n(1284),o=n(5763),s="nr@context";let c=(0,r.fP)();var d;function u(){}function l(){return new u}function f(){d.aborted=!0,d.backlog={}}c.ee?d=c.ee:(d=function e(t,n){var r={},c={},g={},p=!1;try{p=16===n.length&&(0,o.OP)(n).isolatedBacklog}catch(e){}var h={on:b,addEventListener:b,removeEventListener:y,emit:m,get:A,listeners:w,context:v,buffer:x,abort:f,aborted:!1,isBuffering:D,debugId:n,backlog:p?{}:t&&"object"==typeof t.backlog?t.backlog:{}};return h;function v(e){return e&&e instanceof u?e:e?(0,i.X)(e,s,l):l()}function m(e,n,r,i,a){if(!1!==a&&(a=!0),!d.aborted||i){t&&a&&t.emit(e,n,r);for(var o=v(r),s=w(e),u=s.length,l=0;l<u;l++)s[l].apply(o,n);var f=j()[c[e]];return f&&f.push([h,e,n,o]),o}}function b(e,t){r[e]=w(e).concat(t)}function y(e,t){var n=r[e];if(n)for(var i=0;i<n.length;i++)n[i]===t&&n.splice(i,1)}function w(e){return r[e]||[]}function A(t){return g[t]=g[t]||e(h,t)}function x(e,t){var n=j();h.aborted||(0,a.D)(e,(function(e,r){t=t||"feature",c[r]=t,t in n||(n[t]=[])}))}function D(e){return!!j()[c[e]]}function j(){return h.backlog}}(void 0,"globalEE"),c.ee=d)},5546:(e,t,n)=>{n.d(t,{E:()=>r,p:()=>i});var r=n(2177).ee.get("handle");function i(e,t,n,i,a){a?(a.buffer([e],i),a.emit(e,t,n)):(r.buffer([e],i),r.emit(e,t,n))}},4322:(e,t,n)=>{n.d(t,{X:()=>a});var r=n(5546);a.on=o;var i=a.handlers={};function a(e,t,n,a){o(a||r.E,i,e,t,n)}function o(e,t,n,i,a){a||(a="feature"),e||(e=r.E);var o=t[a]=t[a]||{};(o[n]=o[n]||[]).push([e,i])}},3239:(e,t,n)=>{n.d(t,{bP:()=>s,iz:()=>c,m$:()=>o});var r=n(385);let i=!1,a=!1;try{const e={get passive(){return i=!0,!1},get signal(){return a=!0,!1}};r._A.addEventListener("test",null,e),r._A.removeEventListener("test",null,e)}catch(e){}function o(e,t){return i||a?{capture:!!e,passive:i,signal:t}:!!e}function s(e,t){let n=arguments.length>2&&void 0!==arguments[2]&&arguments[2],r=arguments.length>3?arguments[3]:void 0;window.addEventListener(e,t,o(n,r))}function c(e,t){let n=arguments.length>2&&void 0!==arguments[2]&&arguments[2],r=arguments.length>3?arguments[3]:void 0;document.addEventListener(e,t,o(n,r))}},4402:(e,t,n)=>{n.d(t,{Rl:()=>o,ky:()=>s});var r=n(385);const i="xxxxxxxx-xxxx-4xxx-yxxx-xxxxxxxxxxxx";function a(e,t){return e?15&e[t]:16*Math.random()|0}function o(){const e=r._A?.crypto||r._A?.msCrypto;let t,n=0;return e&&e.getRandomValues&&(t=e.getRandomValues(new Uint8Array(31))),i.split("").map((e=>"x"===e?a(t,++n).toString(16):"y"===e?(3&a()|8).toString(16):e)).join("")}function s(e){const t=r._A?.crypto||r._A?.msCrypto;let n,i=0;t&&t.getRandomValues&&(n=t.getRandomValues(new Uint8Array(31)));const o=[];for(var s=0;s<e;s++)o.push(a(n,++i).toString(16));return o.join("")}},7056:(e,t,n)=>{n.d(t,{Bq:()=>r,Hb:()=>a,oD:()=>i});const r="NRBA",i=144e5,a=18e5},7894:(e,t,n)=>{function r(){return Math.round(performance.now())}n.d(t,{z:()=>r})},50:(e,t,n)=>{function r(e,t){"function"==typeof console.warn&&(console.warn("New Relic: ".concat(e)),t&&console.warn(t))}n.d(t,{Z:()=>r})},2587:(e,t,n)=>{n.d(t,{N:()=>c,T:()=>d});var r=n(2177),i=n(5546),a=n(8e3),o=n(3325);const s={stn:[o.D.sessionTrace],err:[o.D.jserrors,o.D.metrics],ins:[o.D.pageAction],spa:[o.D.spa],sr:[o.D.sessionReplay,o.D.sessionTrace]};function c(e,t){const n=r.ee.get(t);e&&"object"==typeof e&&(Object.entries(e).forEach((e=>{let[t,r]=e;void 0===d[t]&&(s[t]?s[t].forEach((e=>{r?(0,i.p)("feat-"+t,[],void 0,e,n):(0,i.p)("block-"+t,[],void 0,e,n),(0,i.p)("rumresp-"+t,[Boolean(r)],void 0,e,n)})):r&&(0,i.p)("feat-"+t,[],void 0,void 0,n),d[t]=Boolean(r))})),Object.keys(s).forEach((e=>{void 0===d[e]&&(s[e]?.forEach((t=>(0,i.p)("rumresp-"+e,[!1],void 0,t,n))),d[e]=!1)})),(0,a.L)(t,o.D.pageViewEvent))}const d={}},2210:(e,t,n)=>{n.d(t,{X:()=>i});var r=Object.prototype.hasOwnProperty;function i(e,t,n){if(r.call(e,t))return e[t];var i=n();if(Object.defineProperty&&Object.keys)try{return Object.defineProperty(e,t,{value:i,writable:!0,enumerable:!1}),i}catch(e){}return e[t]=i,i}},1284:(e,t,n)=>{n.d(t,{D:()=>r});const r=(e,t)=>Object.entries(e||{}).map((e=>{let[n,r]=e;return t(n,r)}))},4351:(e,t,n)=>{n.d(t,{P:()=>a});var r=n(2177);const i=()=>{const e=new WeakSet;return(t,n)=>{if("object"==typeof n&&null!==n){if(e.has(n))return;e.add(n)}return n}};function a(e){try{return JSON.stringify(e,i())}catch(e){try{r.ee.emit("internal-error",[e])}catch(e){}}}},3960:(e,t,n)=>{n.d(t,{K:()=>o,b:()=>a});var r=n(3239);function i(){return"undefined"==typeof document||"complete"===document.readyState}function a(e,t){if(i())return e();(0,r.bP)("load",e,t)}function o(e){if(i())return e();(0,r.iz)("DOMContentLoaded",e)}},8632:(e,t,n)=>{n.d(t,{EZ:()=>d,Qy:()=>c,ce:()=>a,fP:()=>o,gG:()=>u,mF:()=>s});var r=n(7894),i=n(385);const a={beacon:"bam.nr-data.net",errorBeacon:"bam.nr-data.net"};function o(){return i._A.NREUM||(i._A.NREUM={}),void 0===i._A.newrelic&&(i._A.newrelic=i._A.NREUM),i._A.NREUM}function s(){let e=o();return e.o||(e.o={ST:i._A.setTimeout,SI:i._A.setImmediate,CT:i._A.clearTimeout,XHR:i._A.XMLHttpRequest,REQ:i._A.Request,EV:i._A.Event,PR:i._A.Promise,MO:i._A.MutationObserver,FETCH:i._A.fetch}),e}function c(e,t,n){let i=o();const a=i.initializedAgents||{},s=a[e]||{};return Object.keys(s).length||(s.initializedAt={ms:(0,r.z)(),date:new Date}),i.initializedAgents={...a,[e]:{...s,[n]:t}},i}function d(e,t){o()[e]=t}function u(){return function(){let e=o();const t=e.info||{};e.info={beacon:a.beacon,errorBeacon:a.errorBeacon,...t}}(),function(){let e=o();const t=e.init||{};e.init={...t}}(),s(),function(){let e=o();const t=e.loader_config||{};e.loader_config={...t}}(),o()}},7956:(e,t,n)=>{n.d(t,{N:()=>i});var r=n(3239);function i(e){let t=arguments.length>1&&void 0!==arguments[1]&&arguments[1],n=arguments.length>2?arguments[2]:void 0,i=arguments.length>3?arguments[3]:void 0;return void(0,r.iz)("visibilitychange",(function(){if(t)return void("hidden"==document.visibilityState&&e());e(document.visibilityState)}),n,i)}},3081:(e,t,n)=>{n.d(t,{gF:()=>a,mY:()=>i,t9:()=>r,vz:()=>s,xS:()=>o});const r=n(3325).D.metrics,i="sm",a="cm",o="storeSupportabilityMetrics",s="storeEventMetrics"},7633:(e,t,n)=>{n.d(t,{Dz:()=>i,OJ:()=>o,qw:()=>a,t9:()=>r});const r=n(3325).D.pageViewEvent,i="firstbyte",a="domcontent",o="windowload"},9251:(e,t,n)=>{n.d(t,{t:()=>r});const r=n(3325).D.pageViewTiming},5938:(e,t,n)=>{n.d(t,{W:()=>a});var r=n(5763),i=n(2177);class a{constructor(e,t,n){this.agentIdentifier=e,this.aggregator=t,this.ee=i.ee.get(e,(0,r.OP)(this.agentIdentifier).isolatedBacklog),this.featureName=n,this.blocked=!1}}},9144:(e,t,n)=>{n.d(t,{j:()=>v});var r=n(3325),i=n(5763),a=n(5546),o=n(2177),s=n(7894),c=n(8e3),d=n(3960),u=n(385),l=n(50),f=n(3081),g=n(8632);function p(){const e=(0,g.gG)();["setErrorHandler","finished","addToTrace","inlineHit","addRelease","addPageAction","setCurrentRouteName","setPageViewName","setCustomAttribute","interaction","noticeError","setUserId"].forEach((t=>{e[t]=function(){for(var n=arguments.length,r=new Array(n),i=0;i<n;i++)r[i]=arguments[i];return function(t){for(var n=arguments.length,r=new Array(n>1?n-1:0),i=1;i<n;i++)r[i-1]=arguments[i];let a=[];return Object.values(e.initializedAgents).forEach((e=>{e.exposed&&e.api[t]&&a.push(e.api[t](...r))})),a.length>1?a:a[0]}(t,...r)}}))}var h=n(2587);function v(e){let t=arguments.length>1&&void 0!==arguments[1]?arguments[1]:{},v=arguments.length>2?arguments[2]:void 0,m=arguments.length>3?arguments[3]:void 0,{init:b,info:y,loader_config:w,runtime:A={loaderType:v},exposed:x=!0}=t;const D=(0,g.gG)();y||(b=D.init,y=D.info,w=D.loader_config),(0,i.Dg)(e,b||{}),(0,i.GE)(e,w||{}),y.jsAttributes??={},u.v6&&(y.jsAttributes.isWorker=!0),(0,i.CX)(e,y);const j=(0,i.P_)(e);A.denyList=[...j.ajax?.deny_list||[],...j.ajax?.block_internal?[y.beacon,y.errorBeacon]:[]],(0,i.sU)(e,A),p();const _=function(e,t){t||(0,c.R)(e,"api");const g={};var p=o.ee.get(e),h=p.get("tracer"),v="api-",m=v+"ixn-";function b(t,n,r,a){const o=(0,i.C5)(e);return null===n?delete o.jsAttributes[t]:(0,i.CX)(e,{...o,jsAttributes:{...o.jsAttributes,[t]:n}}),A(v,r,!0,a||null===n?"session":void 0)(t,n)}function y(){}["setErrorHandler","finished","addToTrace","inlineHit","addRelease"].forEach((e=>g[e]=A(v,e,!0,"api"))),g.addPageAction=A(v,"addPageAction",!0,r.D.pageAction),g.setCurrentRouteName=A(v,"routeName",!0,r.D.spa),g.setPageViewName=function(t,n){if("string"==typeof t)return"/"!==t.charAt(0)&&(t="/"+t),(0,i.OP)(e).customTransaction=(n||"http://custom.transaction")+t,A(v,"setPageViewName",!0)()},g.setCustomAttribute=function(e,t){let n=arguments.length>2&&void 0!==arguments[2]&&arguments[2];if("string"==typeof e){if(["string","number"].includes(typeof t)||null===t)return b(e,t,"setCustomAttribute",n);(0,l.Z)("Failed to execute setCustomAttribute.\nNon-null value must be a string or number type, but a type of <".concat(typeof t,"> was provided."))}else(0,l.Z)("Failed to execute setCustomAttribute.\nName must be a string type, but a type of <".concat(typeof e,"> was provided."))},g.setUserId=function(e){if("string"==typeof e||null===e)return b("enduser.id",e,"setUserId",!0);(0,l.Z)("Failed to execute setUserId.\nNon-null value must be a string type, but a type of <".concat(typeof e,"> was provided."))},g.interaction=function(){return(new y).get()};var w=y.prototype={createTracer:function(e,t){var n={},i=this,o="function"==typeof t;return(0,a.p)(m+"tracer",[(0,s.z)(),e,n],i,r.D.spa,p),function(){if(h.emit((o?"":"no-")+"fn-start",[(0,s.z)(),i,o],n),o)try{return t.apply(this,arguments)}catch(e){throw h.emit("fn-err",[arguments,this,e],n),e}finally{h.emit("fn-end",[(0,s.z)()],n)}}}};function A(e,t,n,i){return function(){return(0,a.p)(f.xS,["API/"+t+"/called"],void 0,r.D.metrics,p),i&&(0,a.p)(e+t,[(0,s.z)(),...arguments],n?null:this,i,p),n?void 0:this}}function x(){n.e(439).then(n.bind(n,7438)).then((t=>{let{setAPI:n}=t;n(e),(0,c.L)(e,"api")})).catch((()=>(0,l.Z)("Downloading runtime APIs failed...")))}return["actionText","setName","setAttribute","save","ignore","onEnd","getContext","end","get"].forEach((e=>{w[e]=A(m,e,void 0,r.D.spa)})),g.noticeError=function(e,t){"string"==typeof e&&(e=new Error(e)),(0,a.p)(f.xS,["API/noticeError/called"],void 0,r.D.metrics,p),(0,a.p)("err",[e,(0,s.z)(),!1,t],void 0,r.D.jserrors,p)},u.il?(0,d.b)((()=>x()),!0):x(),g}(e,m);return(0,g.Qy)(e,_,"api"),(0,g.Qy)(e,x,"exposed"),(0,g.EZ)("activatedFeatures",h.T),_}},3325:(e,t,n)=>{n.d(t,{D:()=>r,p:()=>i});const r={ajax:"ajax",jserrors:"jserrors",metrics:"metrics",pageAction:"page_action",pageViewEvent:"page_view_event",pageViewTiming:"page_view_timing",sessionReplay:"session_replay",sessionTrace:"session_trace",spa:"spa"},i={[r.pageViewEvent]:1,[r.pageViewTiming]:2,[r.metrics]:3,[r.jserrors]:4,[r.ajax]:5,[r.sessionTrace]:6,[r.pageAction]:7,[r.spa]:8,[r.sessionReplay]:9}}},r={};function i(e){var t=r[e];if(void 0!==t)return t.exports;var a=r[e]={exports:{}};return n[e](a,a.exports,i),a.exports}i.m=n,i.d=(e,t)=>{for(var n in t)i.o(t,n)&&!i.o(e,n)&&Object.defineProperty(e,n,{enumerable:!0,get:t[n]})},i.f={},i.e=e=>Promise.all(Object.keys(i.f).reduce(((t,n)=>(i.f[n](e,t),t)),[])),i.u=e=>(({78:"page_action-aggregate",147:"metrics-aggregate",193:"session_trace-aggregate",242:"session-manager",317:"jserrors-aggregate",348:"page_view_timing-aggregate",412:"lazy-feature-loader",439:"async-api",538:"recorder",590:"session_replay-aggregate",675:"compressor",786:"page_view_event-aggregate",873:"spa-aggregate",898:"ajax-aggregate"}[e]||e)+"."+{78:"467f8594",147:"b86cefcf",193:"ac30a1f3",242:"d080e4cc",317:"319b8300",348:"7b2a53ee",412:"c1052c27",439:"e9f77430",538:"9c5c1546",590:"8b420469",646:"9e7a6b8d",675:"9614fd62",786:"4988d952",860:"95a91211",873:"550eec7b",898:"d95c640e"}[e]+"-1.237.1.min.js"),i.o=(e,t)=>Object.prototype.hasOwnProperty.call(e,t),e={},t="NRBA:",i.l=(n,r,a,o)=>{if(e[n])e[n].push(r);else{var s,c;if(void 0!==a)for(var d=document.getElementsByTagName("script"),u=0;u<d.length;u++){var l=d[u];if(l.getAttribute("src")==n||l.getAttribute("data-webpack")==t+a){s=l;break}}s||(c=!0,(s=document.createElement("script")).charset="utf-8",s.timeout=120,i.nc&&s.setAttribute("nonce",i.nc),s.setAttribute("data-webpack",t+a),s.src=n),e[n]=[r];var f=(t,r)=>{s.onerror=s.onload=null,clearTimeout(g);var i=e[n];if(delete e[n],s.parentNode&&s.parentNode.removeChild(s),i&&i.forEach((e=>e(r))),t)return t(r)},g=setTimeout(f.bind(null,void 0,{type:"timeout",target:s}),12e4);s.onerror=f.bind(null,s.onerror),s.onload=f.bind(null,s.onload),c&&document.head.appendChild(s)}},i.r=e=>{"undefined"!=typeof Symbol&&Symbol.toStringTag&&Object.defineProperty(e,Symbol.toStringTag,{value:"Module"}),Object.defineProperty(e,"__esModule",{value:!0})},i.j=4,i.p="https://js-agent.newrelic.com/",(()=>{var e={4:0,465:0};i.f.j=(t,n)=>{var r=i.o(e,t)?e[t]:void 0;if(0!==r)if(r)n.push(r[2]);else{var a=new Promise(((n,i)=>r=e[t]=[n,i]));n.push(r[2]=a);var o=i.p+i.u(t),s=new Error;i.l(o,(n=>{if(i.o(e,t)&&(0!==(r=e[t])&&(e[t]=void 0),r)){var a=n&&("load"===n.type?"missing":n.type),o=n&&n.target&&n.target.src;s.message="Loading chunk "+t+" failed.\n("+a+": "+o+")",s.name="ChunkLoadError",s.type=a,s.request=o,r[1](s)}}),"chunk-"+t,t)}};var t=(t,n)=>{var r,a,[o,s,c]=n,d=0;if(o.some((t=>0!==e[t]))){for(r in s)i.o(s,r)&&(i.m[r]=s[r]);if(c)c(i)}for(t&&t(n);d<o.length;d++)a=o[d],i.o(e,a)&&e[a]&&e[a][0](),e[a]=0},n=window.webpackChunkNRBA=window.webpackChunkNRBA||[];n.forEach(t.bind(null,0)),n.push=t.bind(null,n.push.bind(n))})();var a={};(()=>{i.r(a);var e=i(50);class t{addPageAction(t,n){(0,e.Z)("Call to agent api addPageAction failed. The session trace feature is not currently initialized.")}setPageViewName(t,n){(0,e.Z)("Call to agent api setPageViewName failed. The page view feature is not currently initialized.")}setCustomAttribute(t,n,r){(0,e.Z)("Call to agent api setCustomAttribute failed. The js errors feature is not currently initialized.")}noticeError(t,n){(0,e.Z)("Call to agent api noticeError failed. The js errors feature is not currently initialized.")}setUserId(t){(0,e.Z)("Call to agent api setUserId failed. The js errors feature is not currently initialized.")}setErrorHandler(t){(0,e.Z)("Call to agent api setErrorHandler failed. The js errors feature is not currently initialized.")}finished(t){(0,e.Z)("Call to agent api finished failed. The page action feature is not currently initialized.")}addRelease(t,n){(0,e.Z)("Call to agent api addRelease failed. The agent is not currently initialized.")}}var n=i(3325),r=i(5763);const o=Object.values(n.D);function s(e){const t={};return o.forEach((n=>{t[n]=function(e,t){return!1!==(0,r.Mt)(t,"".concat(e,".enabled"))}(n,e)})),t}var c=i(9144);var d=i(5546),u=i(385),l=i(8e3),f=i(5938),g=i(3960);class p extends f.W{constructor(e,t,n){let r=!(arguments.length>3&&void 0!==arguments[3])||arguments[3];super(e,t,n),this.auto=r,this.abortHandler,this.featAggregate,this.onAggregateImported,r&&(0,l.R)(e,n)}importAggregator(){let t=arguments.length>0&&void 0!==arguments[0]?arguments[0]:{};if(this.featAggregate||!this.auto)return;const n=u.il&&!0===(0,r.Mt)(this.agentIdentifier,"privacy.cookies_enabled");let a;this.onAggregateImported=new Promise((e=>{a=e}));const o=async()=>{let r;try{if(n){const{setupAgentSession:e}=await Promise.all([i.e(860),i.e(242)]).then(i.bind(i,3228));r=e(this.agentIdentifier)}}catch(t){(0,e.Z)("A problem occurred when starting up session manager. This page will not start or extend any session.",t)}try{if(!this.shouldImportAgg(this.featureName,r))return(0,l.L)(this.agentIdentifier,this.featureName),void a(!1);const{lazyFeatureLoader:e}=await i.e(412).then(i.bind(i,8582)),{Aggregate:n}=await e(this.featureName,"aggregate");this.featAggregate=new n(this.agentIdentifier,this.aggregator,t),a(!0)}catch(t){(0,e.Z)("Downloading and initializing ".concat(this.featureName," failed..."),t),this.abortHandler?.(),a(!1)}};u.il?(0,g.b)((()=>o()),!0):o()}shouldImportAgg(e,t){return e!==n.D.sessionReplay||!!r.Yu.MO&&(!1!==(0,r.Mt)(this.agentIdentifier,"session_trace.enabled")&&(!!t?.isNew||!!t?.state.sessionReplay))}}var h=i(7633),v=i(7894);class m extends p{static featureName=h.t9;constructor(e,t){let i=!(arguments.length>2&&void 0!==arguments[2])||arguments[2];if(super(e,t,h.t9,i),("undefined"==typeof PerformanceNavigationTiming||u.Tt)&&"undefined"!=typeof PerformanceTiming){const t=(0,r.OP)(e);t[h.Dz]=Math.max(Date.now()-t.offset,0),(0,g.K)((()=>t[h.qw]=Math.max((0,v.z)()-t[h.Dz],0))),(0,g.b)((()=>{const e=(0,v.z)();t[h.OJ]=Math.max(e-t[h.Dz],0),(0,d.p)("timing",["load",e],void 0,n.D.pageViewTiming,this.ee)}))}this.importAggregator()}}var b=i(1117),y=i(1284);class w extends b.w{constructor(e){super(e),this.aggregatedData={}}store(e,t,n,r,i){var a=this.getBucket(e,t,n,i);return a.metrics=function(e,t){t||(t={count:0});return t.count+=1,(0,y.D)(e,(function(e,n){t[e]=A(n,t[e])})),t}(r,a.metrics),a}merge(e,t,n,r,i){var a=this.getBucket(e,t,r,i);if(a.metrics){var o=a.metrics;o.count+=n.count,(0,y.D)(n,(function(e,t){if("count"!==e){var r=o[e],i=n[e];i&&!i.c?o[e]=A(i.t,r):o[e]=function(e,t){if(!t)return e;t.c||(t=x(t.t));return t.min=Math.min(e.min,t.min),t.max=Math.max(e.max,t.max),t.t+=e.t,t.sos+=e.sos,t.c+=e.c,t}(i,o[e])}}))}else a.metrics=n}storeMetric(e,t,n,r){var i=this.getBucket(e,t,n);return i.stats=A(r,i.stats),i}getBucket(e,t,n,r){this.aggregatedData[e]||(this.aggregatedData[e]={});var i=this.aggregatedData[e][t];return i||(i=this.aggregatedData[e][t]={params:n||{}},r&&(i.custom=r)),i}get(e,t){return t?this.aggregatedData[e]&&this.aggregatedData[e][t]:this.aggregatedData[e]}take(e){for(var t={},n="",r=!1,i=0;i<e.length;i++)t[n=e[i]]=D(this.aggregatedData[n]),t[n].length&&(r=!0),delete this.aggregatedData[n];return r?t:null}}function A(e,t){return null==e?function(e){e?e.c++:e={c:1};return e}(t):t?(t.c||(t=x(t.t)),t.c+=1,t.t+=e,t.sos+=e*e,e>t.max&&(t.max=e),e<t.min&&(t.min=e),t):{t:e}}function x(e){return{t:e,min:e,max:e,sos:e*e,c:1}}function D(e){return"object"!=typeof e?[]:(0,y.D)(e,j)}function j(e,t){return t}var _=i(8632),E=i(4402),T=i(4351);var k=i(7956),N=i(3239),P=i(9251);class C extends p{static featureName=P.t;constructor(e,t){let n=!(arguments.length>2&&void 0!==arguments[2])||arguments[2];super(e,t,P.t,n),u.il&&((0,r.OP)(e).initHidden=Boolean("hidden"===document.visibilityState),(0,k.N)((()=>(0,d.p)("docHidden",[(0,v.z)()],void 0,P.t,this.ee)),!0),(0,N.bP)("pagehide",(()=>(0,d.p)("winPagehide",[(0,v.z)()],void 0,P.t,this.ee))),this.importAggregator())}}var I=i(3081);class S extends p{static featureName=I.t9;constructor(e,t){let n=!(arguments.length>2&&void 0!==arguments[2])||arguments[2];super(e,t,I.t9,n),this.importAggregator()}}new class extends t{constructor(t){let n=arguments.length>1&&void 0!==arguments[1]?arguments[1]:(0,E.ky)(16);super(),u._A?(this.agentIdentifier=n,this.sharedAggregator=new w({agentIdentifier:this.agentIdentifier}),this.features={},this.desiredFeatures=new Set(t.features||[]),this.desiredFeatures.add(m),Object.assign(this,(0,c.j)(this.agentIdentifier,t,t.loaderType||"agent")),this.start()):(0,e.Z)("Failed to initial the agent. Could not determine the runtime environment.")}get config(){return{info:(0,r.C5)(this.agentIdentifier),init:(0,r.P_)(this.agentIdentifier),loader_config:(0,r.DL)(this.agentIdentifier),runtime:(0,r.OP)(this.agentIdentifier)}}start(){const t="features";try{const r=s(this.agentIdentifier),i=[...this.desiredFeatures];i.sort(((e,t)=>n.p[e.featureName]-n.p[t.featureName])),i.forEach((t=>{if(r[t.featureName]||t.featureName===n.D.pageViewEvent){const i=function(e){switch(e){case n.D.ajax:return[n.D.jserrors];case n.D.sessionTrace:return[n.D.ajax,n.D.pageViewEvent];case n.D.sessionReplay:return[n.D.sessionTrace];case n.D.pageViewTiming:return[n.D.pageViewEvent];default:return[]}}(t.featureName);i.every((e=>r[e]))||(0,e.Z)("".concat(t.featureName," is enabled but one or more dependent features has been disabled (").concat((0,T.P)(i),"). This may cause unintended consequences or missing data...")),this.features[t.featureName]=new t(this.agentIdentifier,this.sharedAggregator)}})),(0,_.Qy)(this.agentIdentifier,this.features,t)}catch(n){(0,e.Z)("Failed to initialize all enabled instrument classes (agent aborted) -",n);for(const e in this.features)this.features[e].abortHandler?.();const r=(0,_.fP)();return delete r.initializedAgents[this.agentIdentifier]?.api,delete r.initializedAgents[this.agentIdentifier]?.[t],delete this.sharedAggregator,r.ee?.abort(),delete r.ee?.get(this.agentIdentifier),!1}}addToTrace(t){(0,e.Z)("Call to agent api addToTrace failed. The page action feature is not currently initialized.")}setCurrentRouteName(t){(0,e.Z)("Call to agent api setCurrentRouteName failed. The spa feature is not currently initialized.")}interaction(){(0,e.Z)("Call to agent api interaction failed. The spa feature is not currently initialized.")}}({features:[m,C,S],loaderType:"lite"})})(),window.NRBA=a})();</script><link rel="shortcut icon" href="/favicon.ico" type="image/x-icon">
    	<link rel="stylesheet" href="/cpopg/softheme/src/css/app.css?v=2.8.34-30">
    	<link rel="stylesheet" href="/cpopg/softheme/src/fonts/saj/styles.css?v=2.8.34-30">
    	<link rel="stylesheet" href="/cpopg/css/formulario.css?v=2.8.34-30" type="text/css">


    	<link rel="stylesheet" href="/cpopg/webjars/select2/3.5.4/select2.css?v=2.8.34-30" type="text/css">
    	<link rel="stylesheet" href="/cpopg/webjars/select2/3.5.4/select2-bootstrap.css?v=2.8.34-30" type="text/css">
    	<link rel="stylesheet" href="/cpopg/css/saj/select2/saj-select2.css">



    <script>
    	window.saj = window.saj || {};
    	window.saj.env = window.saj.env || {};
    	window.saj.env.root = '/cpopg';
    	window.saj.env.css = '/cpopg/css';
    	window.saj.env.js = '/cpopg/js';
    	window.saj.env.imagens = '/cpopg/imagens';
    	window.saj.env.queryString = 'processo.codigo=01Z081I9T0000&processo.foro=1&processo.numero=0070337-91.2008.8.06.0001';	

    	window.saj.cpo = window.saj.cpo || {};

    	// transfere variavel se cpo esta rodando para totem
    	window.saj.cpo.totem = 'false' == 'true';
    </script>


    	<script language="javascript" type="text/JavaScript" src="/cpopg/js/jquery/jquery.min.js?n=1620728708"></script>
    	<script language="javascript" type="text/JavaScript" src="/cpopg/js/jquery/jquery.func_toggle.js?n=2520c6ef-c8ce-445d-b188-10db86961595"></script>
    	<script language="javascript" type="text/javascript" src="/cpopg/js/jquery/jquery.blockUI.min.js?n=d12d2801-0746-409e-83a0-78b7440a6df9"></script>
    	<script language="javascript" type="text/javascript" src="/cpopg/js/jquery/jquery.browser.min.js?n=ca422080-8cf6-4721-a182-45ad26251b66"></script>

    	<script language="javascript" type="text/javascript" src="/cpopg/webjars/lodash/4.17.5/lodash.js?n=b47d7493-489d-412a-978e-52578d4eb3d7"></script>
    	<script language="javascript" type="text/JavaScript" src="/cpopg/js/select2/select2.js?n=dfa3ce50-17f3-4f0b-8be3-fecb1f8a9a9f"></script>
    	<script language="javascript" type="text/JavaScript" src="/cpopg/webjars/select2/3.5.4/select2_locale_pt-BR.js?n=576cd59d-4c4d-4cd2-a8bd-2cd95e738c5b"></script>
    	<script language="javascript" type="text/JavaScript" src="/cpopg/js/saj/saj-select2.js?n=def526f2-5175-4d72-a7d8-8b48b6acfefd"></script>

    	<script language="javascript" type="text/JavaScript" src="/cpopg/js/saj/saj-web-2.2.41-4.js?n=8668b9fb-6e34-4d3c-b713-5803542e7ce7"></script>
    	<script language="javascript" type="text/JavaScript" src="/cpopg/js/saj/saj-tooltip.js?n=c4a4bfe9-e1f7-4d45-937a-585f24e07289"></script>
    	<script language="javascript" type="text/JavaScript" src="/cpopg/js/saj/saj-popup-modal-1.0.0-1.js?n=5da1368a-800a-4907-9ff5-efc81c1688c5"></script>
    	<script language="javascript" type="text/JavaScript" src="/cpopg/js/saj/saj-browser.js?n=56481ed8-33e7-4fc7-a364-061e38107dea"></script>
    	<script language="javascript" type="text/JavaScript" src="/cpopg/js/saj/saj-mascara-input.js?n=0f94a020-8dc0-414a-bf18-dd0289fbc342"></script>
    	<script language="javascript" type="text/JavaScript" src="/cpopg/js/saj/saj-numeroProcesso.js?n=cedce065-e837-4ca9-8952-8773f56dda28"></script>
    	<script language="javascript" type="text/JavaScript" src="/cpopg/js/saj-cpo-cbpesquisa.js?n=686458821"></script>
    	<script language="javascript" type="text/JavaScript" src="/cpopg/js/saj/acessibilidade/acessibilidade.js?n=6c86a601-a47e-4a30-a504-931b4bd369fa"></script>

    	<script language="javascript" type="text/JavaScript" src="/cpopg/softheme/src/js/app.js?n=789536343"></script>   
    	<script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.12.3/umd/popper.min.js?n=e5e24f36-91ce-4957-80a3-ffbcc8a971d3" integrity="sha384-vFJXuSJphROIrBnz7yo7oB41mKfc8JzQZiCq4NCceLEaO4IHwicKwpJf9c9IpFgh" crossorigin="anonymous"></script>
    	<script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0-beta.2/js/bootstrap.min.js?n=1791337263" integrity="sha384-alpBpkh1PFOepccYVYDB4do5UnbKysX5WZXm3XxPqe5iKTfUKjNkCk9SaVuEZflJ" crossorigin="anonymous"></script>






    <script>
    	(function($){
    		$(function(){
    			var intervalo = 1795000;
    			$.saj.manterSessao('/cpopg/manterSessao.do', intervalo);
    		});

    	})(jQuery);
    </script>





        <script language="javascript" type="text/JavaScript">
            $.saj = $.saj || {};
            $.saj.acessoRecurso = {
                abrirPastaDigitalEmPopup: 'true' == 'true',
                idRecursoQueProvocouLiberacaoPorSenha: '',
                limitaAcessoPastaDigital: 'false',
                popupSenha: {
                    mostrar: 'false' == 'true',
                    titulo: 'Senha do processo',
                    altura: 220 + Number("10"),
                    alturaAdicionalParaMensagemValidacao: Number("0"),
                    largura: 580
                },
                popupMensagem: {
                    titulo: 'Aviso:',
                    texto: 'Você atingiu o limite diário de acessos à pasta digital em processos que não está vinculado.'
                }
            };

            $.saj.getUrlParameter = function getUrlParameter(sParam) {
                var sPageURL = decodeURIComponent(window.location.search.substring(1)), sURLVariables = sPageURL.split('&'), sParameterName, i;
                for (i = 0; i < sURLVariables.length; i++) {
                    sParameterName = sURLVariables[i].split('=');
                    if (sParameterName[0] === sParam) {
                        return sParameterName[1] === undefined ? true : sParameterName[1];
                    }
                }
            };
        </script>
        <script language="javascript" type="text/JavaScript" src="/cpopg/jsp/show-2.8.33-0.js?n=1814283828"></script>

    	<script type="text/javascript">
    		(function($) {
    			$(function(){
    				// Correção temporária do alinhamento do divisor de seção de formulário do SPW 
    				$('td[background$="spw/fundo_subtitulo2.gif"]').attr('valign', 'top');


    			})
    		})(jQuery);
    	</script>



































    </head>

    <body>





































    <script type="text/javascript">
        (function ($) {
            $(function () {
                var captcha = $.saj.getUrlParameter('uuidCaptcha');

                if (!captcha) {
                    return;
                }

                if(!captcha){
                    return;
                }
                var $processoPrinc = $('.processoPrinc');
                $processoPrinc.attr('href', $processoPrinc.attr('href') + '&uuidCaptcha=' + captcha);

                var $processoPaiApenso = $('.processoPaiApenso');
                $processoPaiApenso.attr('href', $processoPaiApenso.attr('href') + '&uuidCaptcha=' + captcha);

                $('.incidente').each(function () {
                    var $incidente = $(this);
                    var url = $incidente.attr('href');
                    $incidente.attr('href', url + '&uuidCaptcha=' + captcha);
                });

            })
        })(jQuery);
    </script>

    <!-- HEADER-->
    <div class="unj-entity-header">





    <div class="unj-entity-header__actions">
        <div class="container">
            <div class="row">
                <div class="col-3 col-md-4">
                    <a href="javascript:history.back();" class="unj-link-back">
                        <i id="setaVoltar" class="icon-back"></i>
                    </a>
                </div>
                <div class="col-13 col-md-12 unj-ta-r">
                    <!-- CDAS -->

                    <!-- Custas -->

                    <!-- Pasta digital -->










                                <a class="linkPasta btn btn-secondary btn-space" id="linkPasta" aria-hidden="true" title="Pasta digital" href="#liberarAutoPorSenha">
                                    Visualizar autos
                                </a>
                                <!-- link da pasta digital exibido somente para leitores de tela (deficientes visuais), neste caso o link anterior é ignorado pelo leitor
                                Obs: necessário manter a table devido aos atributos de acessibilidade se comportarem adequadamente com a tabela, comportamento que não é possível colocando
                                os atributos somente na tag do link-->
                                <a class="linkPasta btn btn-secondary btn-space" id="linkPastaAcessibilidade" style="font-size:0;height:0;width:0;padding:0;margin:0;border:none" href="#liberarAutoPorSenha&amp;acessibilidade=true">
                                    Visualizar autos
                                </a>






                            <!-- Peticionar -->




                </div>
            </div>
        </div>
    </div>









    <div class="unj-entity-header__summary">
        <div id="containerDadosPrincipaisProcesso" class="container">
            <div class="row">
                <div class="col-lg-12 col-xl-13">
                    <!--principal -->

                        <span id="numeroProcesso" class="unj-larger-1">
                            0070337-91.2008.8.06.0001
                        </span>


                            <span id="labelSituacaoProcesso" class="unj-tag">Arquivado definitivamente</span>




                    <!-- incidente -->



                </div>

            </div>
            <div class="row">

                    <div class="col-lg-3 col-xl-3 mb-3">
                        <span id="labelClasseProcesso" class="unj-label">Classe</span>
                        <div class="lh-1-1 line-clamp__2"><span id="classeProcesso" title="Ação Penal - Procedimento Ordinário">Ação Penal - Procedimento Ordinário</span></div>
                    </div>


                    <div class="col-lg-2 col-xl-3 mb-3">
                        <span id="labelAssuntoProcesso" class="unj-label">
                            Assunto
                        </span>
                        <div class="lh-1-1 line-clamp__2"> <span id="assuntoProcesso" title="Crimes de Trânsito">Crimes de Trânsito</span></div>
                    </div>


                    <div class="col-lg-2 col-xl-2 mb-2">
                        <span id="labelForoProcesso" class="unj-label">
                            Foro
                        </span>
                        <div class="lh-1-1 line-clamp__2"> <span id="foroProcesso" title="Fortaleza - Fórum Clóvis Beviláqua">Fortaleza - Fórum Clóvis Beviláqua</span></div>
                    </div>


                    <div class="col-lg-3 col-xl-2 mb-2">
                        <span id="labelVaraProcesso" class="unj-label">
                            Vara
                        </span>
                        <div class="lh-1-1 line-clamp__2"><span id="varaProcesso" title="1ª Vara Criminal (SEJUD 1º Grau)">1ª Vara Criminal (SEJUD 1º Grau)</span></div>
                    </div>




                <!-- Processo principal -->



            </div>
        </div>
    </div>






    <div class="unj-entity-header__details">
        <div class="container">
            <div class="unj-ta-r">

                    <a href="#maisDetalhes" class="unj-link-collapse" data-toggle="collapse" aria-expanded="false" aria-controls="maisDetalhes">
                        <span class="unj-link-collapse__show">
                            <i id="botaoExpandirDadosSecundarios" class="unj-link-collapse__icon glyph glyph-chevron-down"></i>
                            Mais
                        </span>
                        <span class="unj-link-collapse__hide">
                            <i id="botaoRecolherDadosSecundarios" class="unj-link-collapse__icon glyph glyph-chevron-up"></i>
                            Recolher
                        </span>
                    </a>

            </div>
            <div id="maisDetalhes" class="collapse" aria-expanded="false">
                <div class="row unj-row--border-top">

                        <div class="col-lg-3 mb-2">
                            <span id="labelDistribuicaoProcesso" class="unj-label">Distribuição </span>
                            <div id="dataHoraDistribuicaoProcesso">02/05/2018 às 09:13 - Sorteio</div>
                        </div>



                        <div class="col-lg-3 mb-2">
                            <span id="labelControleProcesso" class="unj-label">Controle</span>
                            <div id="numeroControleProcesso">2018/000296</div>
                        </div>


                        <div class="col-lg-2 col-xl-2 mb-2">
                            <span id="labelAreaProcesso" class="unj-label">Área</span>
                            <div id="areaProcesso" class="lh-1-1 line-clamp__2"> <span title="Criminal">Criminal</span></div>
                        </div>




                        <div class="col-lg-3 mb-2">
                            <span class="unj-label">Outros números</span>
                            <div>2008.0023.6626-2/0, 8000016-71.2021.8.06.0086</div>
                        </div>




                </div>
            </div>

        </div>
    </div>

    </div>


    <div class="div-conteudo container mb-90">





























    <aside class="aside-nav aside-nav--left">
        <div class="aside-nav__inner">
            <header class="aside-nav__main-menu__header"><span class="aside-nav__main-menu__header__text">  Menu e-SAJ</span>
                <a href="#" class="aside-nav__user__close-button close-offcanvas">
                    <img src="https://esaj.tjce.jus.br/esaj/img/icons/icon-close--light.png" alt="">
                </a>
            </header>
            <nav class="aside-nav__main-menu">
                <ul class="aside-nav__main-menu__list" id="conteudoMenuEsaj"><li class="aside-nav__main-menu__list__item has__menu__children"><a href="#" class="aside-nav__main-menu__list__item__link">Consultas Processuais</a>
    <ul class="aside-nav__main-menu__list__item menu__children"><li class="aside-nav__main-menu__list__item"><a href="https://esaj.tjce.jus.br/cpopg/open.do" class="aside-nav__main-menu__list__item__link">Consulta de Processos de 1º Grau</a>
    </li>
    <li class="aside-nav__main-menu__list__item"><a href="https://esaj.tjce.jus.br/cposg5/open.do" class="aside-nav__main-menu__list__item__link">Consulta de Processos de 2º Grau</a>
    </li>
    <li class="aside-nav__main-menu__list__item"><a href="https://esaj.tjce.jus.br/cjpg" class="aside-nav__main-menu__list__item__link">Consulta de Julgados de Primeiro Grau</a>
    </li>
    <li class="aside-nav__main-menu__list__item"><a href="https://esaj.tjce.jus.br/cjsg/consultaCompleta.do" class="aside-nav__main-menu__list__item__link">Consultas de Jurisprudência</a>
    </li>
    <li class="aside-nav__main-menu__list__item"><a href="https://esaj.tjce.jus.br/cdje" class="aside-nav__main-menu__list__item__link">Diário da Justiça Eletrônico</a>
    </li>
    </ul></li>
    <li class="aside-nav__main-menu__list__item has__menu__children"><a href="#" class="aside-nav__main-menu__list__item__link">Custas Processuais</a>
    <ul class="aside-nav__main-menu__list__item menu__children"><li class="aside-nav__main-menu__list__item"><a href="https://esaj.tjce.jus.br/ccpweb/iniciarCalculoDeCustas.do?cdTipoCusta=1&amp;flTipoCusta=0&amp;cdServicoCalculoCusta=690003" class="aside-nav__main-menu__list__item__link">Custas Iniciais</a>
    </li>
    <li class="aside-nav__main-menu__list__item"><a href="https://esaj.tjce.jus.br/ccpweb/iniciarCalculoDeCustas.do?cdTipoCusta=2&amp;flTipoCusta=1&amp;cdServicoCalculoCusta=690008" class="aside-nav__main-menu__list__item__link">Custas Intermediárias</a>
    </li>
    <li class="aside-nav__main-menu__list__item"><a href="https://esaj.tjce.jus.br/ccpweb/iniciarCalculoDeCustas.do?cdTipoCusta=4&amp;flTipoCusta=2&amp;cdServicoCalculoCusta=690006" class="aside-nav__main-menu__list__item__link">Custas Complementares</a>
    </li>
    <li class="aside-nav__main-menu__list__item"><a href="https://esaj.tjce.jus.br/ccpweb/iniciarCalculoDeCustas.do?cdTipoCusta=7&amp;flTipoCusta=0&amp;cdServicoCalculoCusta=690004" class="aside-nav__main-menu__list__item__link">Incidentes Processuais</a>
    </li>
    <li class="aside-nav__main-menu__list__item"><a href="https://esaj.tjce.jus.br/ccpweb/iniciarCalculoDeCustas.do?cdTipoCusta=8&amp;flTipoCusta=5&amp;cdServicoCalculoCusta=690007" class="aside-nav__main-menu__list__item__link">Atos Avulsos</a>
    </li>
    <li class="aside-nav__main-menu__list__item"><a href="https://esaj.tjce.jus.br/ccpweb/iniciarCalculoDeCustas.do?cdTipoCusta=3&amp;flTipoCusta=5&amp;cdServicoCalculoCusta=690010" class="aside-nav__main-menu__list__item__link">Certidões</a>
    </li>
    <li class="aside-nav__main-menu__list__item"><a href="https://esaj.tjce.jus.br/ccpweb/iniciarCalculoDeCustas.do?cdTipoCusta=10&amp;flTipoCusta=0&amp;cdServicoCalculoCusta=690005" class="aside-nav__main-menu__list__item__link">Execuções Fiscais - Pagamento antes do julgamento dos Embargos</a>
    </li>
    <li class="aside-nav__main-menu__list__item"><a href="https://esaj.tjce.jus.br/ccpweb/iniciarCalculoDeCustas.do?cdTipoCusta=11&amp;flTipoCusta=0&amp;cdServicoCalculoCusta=690002" class="aside-nav__main-menu__list__item__link">Execuções Fiscais - Pagamento após o julgamento dos Embargos</a>
    </li>
    <li class="aside-nav__main-menu__list__item"><a href="https://esaj.tjce.jus.br/ccpweb/iniciarCalculoDeCustas.do?cdTipoCusta=9&amp;flTipoCusta=0&amp;cdServicoCalculoCusta=690009" class="aside-nav__main-menu__list__item__link">Execuções Fiscais - Pagamento antes da Penhora</a>
    </li>
    <li class="aside-nav__main-menu__list__item"><a href="https://esaj.tjce.jus.br/ccpweb/abrirConsultaCustas.do" class="aside-nav__main-menu__list__item__link">Consulta de Custas</a>
    </li>
    </ul></li>
    <li class="aside-nav__main-menu__list__item has__menu__children"><a href="#" class="aside-nav__main-menu__list__item__link">Peticionamento Eletrônico</a>
    <ul class="aside-nav__main-menu__list__item menu__children"><li class="aside-nav__main-menu__list__item has__menu__children"><a href="#" class="aside-nav__main-menu__list__item__link">Peticionamento Eletrônico de 1º Grau</a>
    <ul class="aside-nav__main-menu__list__item menu__children"><li class="aside-nav__main-menu__list__item"><a href="/petpg/abrirNovaPeticaoInicial.do?instancia=PG" class="aside-nav__main-menu__list__item__link">Peticionamento Inicial - Primeiro Grau</a>
    </li>
    <li class="aside-nav__main-menu__list__item"><a href="/petpg/abrirNovaPeticaoIntermediaria.do?instancia=PG" class="aside-nav__main-menu__list__item__link">Peticionamento Intermediário - Primeiro Grau</a>
    </li>
    <li class="aside-nav__main-menu__list__item"><a href="/petpg/abrirConsultaPeticoes.do" class="aside-nav__main-menu__list__item__link">Consulta de Petições - Primeiro Grau</a>
    </li>
    </ul></li>
    <li class="aside-nav__main-menu__list__item has__menu__children"><a href="#" class="aside-nav__main-menu__list__item__link">Peticionamento Eletrônico de 2º Grau - Tribunal de Justiça</a>
    <ul class="aside-nav__main-menu__list__item menu__children"><li class="aside-nav__main-menu__list__item"><a href="https://esaj.tjce.jus.br/petsg/abrirNovaPeticaoInicial.do?instancia=SG" class="aside-nav__main-menu__list__item__link">Peticionamento Inicial de 2º Grau</a>
    </li>
    <li class="aside-nav__main-menu__list__item"><a href="https://esaj.tjce.jus.br/petsg/abrirNovaPeticaoIntermediaria.do?instancia=SG" class="aside-nav__main-menu__list__item__link">Peticionamento Intermediário de 2º Grau</a>
    </li>
    <li class="aside-nav__main-menu__list__item"><a href="https://esaj.tjce.jus.br/petsg/abrirConsultaPeticoes.do" class="aside-nav__main-menu__list__item__link">Consulta de Petições de 2º Grau</a>
    </li>
    </ul></li>
    <li class="aside-nav__main-menu__list__item has__menu__children"><a href="#" class="aside-nav__main-menu__list__item__link">Peticionamento Eletrônico de 2º Grau - Turmas Recursais</a>
    <ul class="aside-nav__main-menu__list__item menu__children"><li class="aside-nav__main-menu__list__item"><a href="https://esaj.tjce.jus.br/petcr/abrirNovaPeticaoInicial.do?instancia=CR" class="aside-nav__main-menu__list__item__link">Peticionamento Inicial - Turmas Recursais</a>
    </li>
    <li class="aside-nav__main-menu__list__item"><a href="https://esaj.tjce.jus.br/petcr/abrirNovaPeticaoIntermediaria.do?instancia=CR" class="aside-nav__main-menu__list__item__link">Peticionamento Intermediário - Turmas Recursais</a>
    </li>
    <li class="aside-nav__main-menu__list__item"><a href="https://esaj.tjce.jus.br/petcr/abrirConsultaPeticoes.do" class="aside-nav__main-menu__list__item__link">Consulta de Petições - Turmas Recursais</a>
    </li>
    </ul></li>
    <li class="aside-nav__main-menu__list__item"><a href="https://esaj.tjce.jus.br/substabelecimento" class="aside-nav__main-menu__list__item__link">Substabelecimento</a>
    </li>
    </ul></li>
    <li class="aside-nav__main-menu__list__item"><a href="https://esaj.tjce.jus.br/push/" class="aside-nav__main-menu__list__item__link">Push</a>
    </li>
    <li class="aside-nav__main-menu__list__item has__menu__children"><a href="#" class="aside-nav__main-menu__list__item__link">Intimações e Citações On-line</a>
    <ul class="aside-nav__main-menu__list__item menu__children"><li class="aside-nav__main-menu__list__item"><a href="https://esaj.tjce.jus.br/intimacoesweb/abrirConsultaAtosNaoRecebidos.do" class="aside-nav__main-menu__list__item__link">Recebimento de Intimações e Citações</a>
    </li>
    <li class="aside-nav__main-menu__list__item"><a href="https://esaj.tjce.jus.br/intimacoesweb/abrirConsultaAtosRecebidos.do" class="aside-nav__main-menu__list__item__link">Consulta de Intimações e Citações Recebidas </a>
    </li>
    </ul></li>
    <li class="aside-nav__main-menu__list__item has__menu__children"><a href="#" class="aside-nav__main-menu__list__item__link">Conferência de Documento Digital</a>
    <ul class="aside-nav__main-menu__list__item menu__children"><li class="aside-nav__main-menu__list__item"><a href="https://esaj.tjce.jus.br/pastadigital/pg/abrirConferenciaDocumento.do" class="aside-nav__main-menu__list__item__link">Conferência de Documento Digital do 1ºGrau</a>
    </li>
    <li class="aside-nav__main-menu__list__item"><a href="https://esaj.tjce.jus.br/pastadigital/sg/abrirConferenciaDocumento.do" class="aside-nav__main-menu__list__item__link">Conferência de Documento Digital do 2ºGrau</a>
    </li>
    </ul></li>
    <li class="aside-nav__main-menu__list__item has__menu__children"><a href="#" class="aside-nav__main-menu__list__item__link">Pauta Julgamento</a>
    <ul class="aside-nav__main-menu__list__item menu__children"><li class="aside-nav__main-menu__list__item"><a href="https://esaj.tjce.jus.br/pauta-julgamento/consulta" class="aside-nav__main-menu__list__item__link">Consulta da Pauta de Julgamento</a>
    </li>
    </ul></li></ul>
            </nav>
            <div id="esaj-beta-switcher-placeholder"></div>
        </div>
    </aside>
    <aside class="aside-nav aside-nav--right aside-nav__user">
        <div class="aside-nav__inner">
            <div class="aside-nav__user__sign">
                <div class="aside-nav__user__sign__brand">
                    <img src="https://esaj.tjce.jus.br/esaj/img/aside/brasoes/br-tjce.jpg" alt="">
                </div>
                <ul class="aside-nav__user__sign__list">
                    <li><span class="aside-nav__user__sign__place">Tribunal de Justiça do Estado do Ceará</span></li>
                </ul>
                <a href="#" class="aside-nav__user__close-button close-offcanvas">
                    <img src="https://esaj.tjce.jus.br/esaj/img/icons/icon-close--dark.png" alt="">
                </a>
            </div>
            <hr>
            <div class="aside-nav__user__info">
                <h4 class="aside-nav__user__title">Minha conta</h4>
                <ul class="aside-nav__user__info__list">
                    <li class="aside-nav__user__info__list__item"><span class="aside-nav__user__info__name" id="menuNmUsuarioLogado"></span></li>
                    <li class="aside-nav__user__info__list__item"><span class="aside-nav__user__info__oab" id="menuUsuarioOabs">OAB: </span></li>
                </ul>
                <ul class="aside-nav__user__info__list-access">
                    <li class="aside-nav__user__info__list-access__item"><a class="aside-nav__user__info__list-access__item__link" href="https://esaj.tjce.jus.br/esaj/cadastro.do">Meu perfil</a></li>

                        <li class="aside-nav__user__info__list-access__item"><a class="aside-nav__user__info__list-access__item__link" href="https://esaj.tjce.jus.br/caixapostal">Caixa Postal</a></li>

                    <li class="aside-nav__user__info__list-access__item"><a class="aside-nav__user__info__list-access__item__link" id="logoutLink" href="#">Sair</a></li>
                </ul>
            </div>
        </div>
    </aside>
    <header>
        <link rel="shortcut icon" href="https://esaj.tjce.jus.br/esaj/tema/padrao/clientes/CE/imagens/favicon.ico" type="image/x-icon">
        <link href="https://esaj.tjce.jus.br/esaj/app.css" rel="stylesheet" type="text/css">
        <nav class="header__navbar">
            <a class="header__navbar__menu-hamburger open__aside-nav--left navbar-menu-hamburger__item__link">
                <span class="menu-hamburger__alert" style="display:none;"></span>
                <span class="glyph glyph-hamburger"></span>
            </a>

            <h1 class="header__navbar__title" href=""><a class="linkLogo" href="https://esaj.tjce.jus.br/esaj/redirecionarNovoEsaj.do"><strong>e-SAJ</strong></a> | Processos de 1º Grau</h1>

            <ul class="header__navbar__menu header__navbar__menu--right">
                <li class="header__navbar__menu__item header__navbar__menu__item--initials">
                    <a class="header__navbar__brand__initials" href="https://www.tjce.jus.br"> TJCE </a>
                </li>
                <li class="header__navbar__menu__item header__navbar__menu__item--user">
                   <span class="header__navbar__name open__aside-nav--right">
                         <span id="headerNmUsuarioLogado" class="header__navbar__name__text">Identificar-se </span>
                         <span class="glyph glyph-contact header__navbar__name__icon"></span>
                   </span>
                </li>
            </ul>
        </nav>
    </header>
    <div class="offcanvas-backdrop"></div>


    <script>
        var dict = {
            'certificado.tituloCertificadoDigital': 'Certificado digital',
            'certificado.msgCarregandoCertificado': 'Carregando certificados...',
            'certificado.msgNenhumCertificadoEncontrado': 'Nenhum certificado encontrado',
            'certificado.msgErroCarregarCertificado': 'Erro ao carregar certificados',
            'certificado.msgCertificadoExpirado': '[Expirado]',
            'certificado.msgCertificadoNaoValido': '[Ainda não válido]',
            'certificado.msgCertificadoNaoIcpBrasil': '[Não ICP-Brasil]',
            'certificado.tituloProblemasAoAssinar': 'Falha de comunicação com o dispositivo de assinatura digital',

            'label.contato': 'Contato',
            'label.identificarSe': 'Identificar-se ',

            'mensagem.aguarde': 'Por favor, aguarde.',
            'mensagem.paginaNaoCarregada': 'Não foi possível carregar a página.',
            'mensagem.marcarLido': 'Marcar como lido',
            'mensagem.registrosSelecionados': 'Registros selecionados',
            'mensagem.registroJaSelecionado': 'Este registro já está selecionado',

            'mensagem.data.invalida': 'A data digitada é inválida.',
            'mensagem.data.anoInvalido': 'O ano informado deve ser maior que',
            'mensagem.data.mesInvalido': 'O mês não pode ser maior que 12.',
            'mensagem.data.mes': 'O mês',
            'mensagem.data.mesMaior29dias': 'não pode ter mais que 29 dias.',
            'mensagem.data.mesMaior28dias': 'não pode ter mais que 28 dias.',
            'mensagem.data.mesMaior31dias': 'não pode ter mais que 31 dias.',
            'mensagem.data.mesMaior30dias': 'não pode ter mais que 30 dias.',

            'mensagem.email.invalido': 'O formato do endereço de e-mail não é válido. Verifique se ele tem o formato "usuario@dominio".',
            'mensagem.email.caracteresInvalidos': 'O endereço de e-mail possui caracteres inválidos',
            'mensagem.email.usuarioInvalido': 'O formato do usuário informado no endereço de e-mail não é válido.',
            'mensagem.email.ipInvalido': 'O endereço IP informado no endereço de e-mail não é válido.',
            'mensagem.email.dominioInvalido': 'O formato do domínio informado no endereço de e-mail não é válido.',
            'mensagem.email.dominioIncompleto': 'O domínio informado no endereço de e-mail deve possuir pelo menos duas partes. Por exemplo: "usuario@empresa.com.br".',

            'mensagem.texto.tamanhoInvalido': 'O tamanho do texto digitado é maior do que o tamanho permitido. Tamanho permitido:',
            'mensagem.texto.caracter': 'O caracter',
            'mensagem.texto.caracterPosicaoInvalida': 'não está permitido na posição',

            'mensagem.numero.numeroInvalido': 'O valor digitado não é um número válido.',
            'mensagem.numero.numeroNaoPodeCasasDecimais': 'O número não pode conter casas decimais',
            'mensagem.numero.numeroCasaDecimaisInvalidas': 'O número de casas decimais é inválido. O número pode conter apenas',
            'mensagem.numero.casaDecimais': 'casas decimais',
            'mensagem.numero.numeroInteiroInvalido': 'O número de dígitos inteiros é inválido. O número pode conter apenas',
            'mensagem.numero.digitosInteiros': 'dígitos inteiros',
            'mensagem.numero.numeroTamanhoInvalido': 'O número digitado não pode ser maior que',
            'mensagem.numero.numeroZeroInvalido': 'O número digitado deve ser diferente de zero.'
        }
    </script>



    <script>
        var appEsajLayout = appEsajLayout || {};
        appEsajLayout.urlNovoMenuHtml = 'https://esaj.tjce.jus.br/esaj/menuPortalV2Html.do?servico=190101';

        var appEsajCas = appEsajCas || {};
        appEsajCas.urlServicoConteudoIdentificacao = 'https://esaj.tjce.jus.br/sajcas/conteudoIdentificacaoJson?script=1691481668985&retorno=' + encodeURIComponent(location.href);
    </script>
    <script src="https://esaj.tjce.jus.br/esaj/js/portalV2-bundle.js?n=806192629"></script>

    <script src="https://esaj.tjce.jus.br/sajcas/seletorVersaoBeta.js?n=4a270623-3553-4d8c-93a3-61980a8e2292&amp;versao=2"></script>















































    <div style="padding-top: 10px;">




    			<h2 class="subtitle tituloDoBloco">Dados da delegacia</h2>


    </div>

    	<!--  cabecalho da lista (Delegacias) -->

    	<!--  dados da lista (Delegacias) -->


    			<table style="margin-left:15px; margin-top:1px;" align="center" width="98%" border="0" cellspacing="0" cellpadding="1">
    				<thead>
    					<tr class="label">
    						<th>Documento</th>
    						<th>Número</th>
    						<th>Distrito policial</th>
    						<th>Município</th>
    					</tr>
    					<tr class="fundoEscuro" height="2" aria-hidden="true">
    						<td></td>
    						<td></td>
    						<td></td>
    						<td></td>
    					</tr>
    				</thead>
    				<tbody id="dadosDaDelegacia">

    						<tr id="" class="fundoClaro">
    							<td class="documento-delegacia" width="20%">Inquérito Policial</td>
    							<td class="numero-delegacia" width="20%">196/2007</td>
    							<td class="distrito-delegacia" width="30%">8º Distrito Policial (PÓLO) - Fortaleza/CE</td>
    							<td class="municipio-delegacia" width="30%">Fortaleza-CE </td>
    						</tr>

    				</tbody>
    			</table>



    	<!--  dados da lista (Delegacias) -->















































    <div style="padding-top: 10px;">




    			<h2 class="subtitle tituloDoBloco">Partes do processo</h2>


    </div>

    <!--  cabecalho da tabela de lista (partes) -->


    <!--  dados da lista partes principais (partes) -->
    <table id="tablePartesPrincipais" style="margin-left:15px; margin-top:1px;" align="center" border="0" cellpadding="0" cellspacing="0" width="98%">











    <tbody><tr class="fundoClaro">
    	<td valign="top" width="141" style="padding-bottom: 5px" class="label">
    		<span class="mensagemExibindo tipoDeParticipacao">Vítima&nbsp;</span>
    	</td>
    	<td class="nomeParteEAdvogado" width="*" align="left" style="padding-bottom: 5px">




    					G. de O. C.









    	</td>
    </tr>












    <tr class="fundoClaro">
    	<td valign="top" width="141" style="padding-bottom: 5px" class="label">
    		<span class="mensagemExibindo tipoDeParticipacao">Autor&nbsp;</span>
    	</td>
    	<td class="nomeParteEAdvogado" width="*" align="left" style="padding-bottom: 5px">




    					Ministério Público do Estado do Ceará









    	</td>
    </tr>












    <tr class="fundoClaro">
    	<td valign="top" width="141" style="padding-bottom: 5px" class="label">
    		<span class="mensagemExibindo tipoDeParticipacao">Terceiro&nbsp;</span>
    	</td>
    	<td class="nomeParteEAdvogado" width="*" align="left" style="padding-bottom: 5px">




    					Departamento de Tecnologia da Informação e Comunicação - DETIC (Polícia Civil)









    	</td>
    </tr>












    <tr class="fundoClaro">
    	<td valign="top" width="141" style="padding-bottom: 5px" class="label">
    		<span class="mensagemExibindo tipoDeParticipacao">Testemunha&nbsp;</span>
    	</td>
    	<td class="nomeParteEAdvogado" width="*" align="left" style="padding-bottom: 5px">




    					M. L. S. I.









    	</td>
    </tr>


    </tbody></table>



    	<!--  dados da lista todas as partes (partes) -->
    	<table id="tableTodasPartes" style="margin-left:15px; margin-top:1px; display: none; " align="center" width="98%" border="0" cellspacing="0" cellpadding="0">











    <tbody><tr class="fundoClaro">
    	<td valign="top" width="141" style="padding-bottom: 5px" class="label">
    		<span class="mensagemExibindo tipoDeParticipacao">Vítima&nbsp;</span>
    	</td>
    	<td class="nomeParteEAdvogado" width="*" align="left" style="padding-bottom: 5px">




    					G. de O. C.









    	</td>
    </tr>












    <tr class="fundoClaro">
    	<td valign="top" width="141" style="padding-bottom: 5px" class="label">
    		<span class="mensagemExibindo tipoDeParticipacao">Vítima&nbsp;</span>
    	</td>
    	<td class="nomeParteEAdvogado" width="*" align="left" style="padding-bottom: 5px">




    					A. S. F.









    	</td>
    </tr>












    <tr class="fundoClaro">
    	<td valign="top" width="141" style="padding-bottom: 5px" class="label">
    		<span class="mensagemExibindo tipoDeParticipacao">Autor&nbsp;</span>
    	</td>
    	<td class="nomeParteEAdvogado" width="*" align="left" style="padding-bottom: 5px">




    					Ministério Público do Estado do Ceará









    	</td>
    </tr>












    <tr class="fundoClaro">
    	<td valign="top" width="141" style="padding-bottom: 5px" class="label">
    		<span class="mensagemExibindo tipoDeParticipacao">Terceiro&nbsp;</span>
    	</td>
    	<td class="nomeParteEAdvogado" width="*" align="left" style="padding-bottom: 5px">




    					Departamento de Tecnologia da Informação e Comunicação - DETIC (Polícia Civil)









    	</td>
    </tr>












    <tr class="fundoClaro">
    	<td valign="top" width="141" style="padding-bottom: 5px" class="label">
    		<span class="mensagemExibindo tipoDeParticipacao">Testemunha&nbsp;</span>
    	</td>
    	<td class="nomeParteEAdvogado" width="*" align="left" style="padding-bottom: 5px">




    					M. L. S. I.









    	</td>
    </tr>


    	</tbody></table>
        <div id="divLinksTituloBlocoPartes" style="text-align:right">










    <input id="mensagemNaoExibidapartes" type="hidden" value="">

        <input id="linkNaoExibidopartes" type="hidden" value="<span id=&quot;setasDireitapartes&quot; class=&quot;setasDireita&quot;><i class=&quot;unj-link-collapse__icon glyph glyph-chevron-up&quot;></i></span>Recolher">

    <span id="mensagensExibindopartes" class="mensagemExibindo">

    </span> &nbsp;

        <a id="linkpartes" href="javascript:" class="linkNaoSelecionado unj-link-collapse">
            <span id="setasDireitapartes" class="setasDireita">
                <i class="unj-link-collapse__icon glyph glyph-chevron-down"></i>
            </span>
            Mais
        </a>

    <script>
    	$(function() {
    		var controlarLink = function() {
    			var $linkNaoExibido = $('input#linkNaoExibidopartes');
    			var conteudoLinkNaoApresentado = $linkNaoExibido.val();
    			var $link = $('a#linkpartes');

    			$linkNaoExibido.val($link.html());
    			$link.html(conteudoLinkNaoApresentado);
    		};

    		var controlarMensagem = function() {
    			var $mensagemNaoExibida = $('input#mensagemNaoExibidapartes');
    			var $spanMensagem = $('span#mensagensExibindopartes');
    			var mensagemExibida = $spanMensagem.html();
    			var mensagemNaoExibida = $mensagemNaoExibida.val();

    			$spanMensagem.html(mensagemNaoExibida);
    			$mensagemNaoExibida.val(mensagemExibida);
    		};

    		var controlarMensagemLink = function() {
    			controlarMensagem();
    			controlarLink();
    		};

    		var esconderElementosExtrasMostrarDefault = function() {
    			$('#tableTodasPartes').hide();
    			$('#tablePartesPrincipais').show();
    		};

    		var mostrarElementosExtrasEsconderDefault = function() {
    			$('#tablePartesPrincipais').hide();
    			$('#tableTodasPartes').show();
    		};

    		var initPagina = function() {
                var setasDireita = '<span id="setasDireitapartes" class="setasDireita"><i class="unj-link-collapse__icon glyph glyph-chevron-up"></i></span>';
    			var $linkEscondido = $('input#linkNaoExibidopartes');
    			$linkEscondido.val(setasDireita+$linkEscondido.val());
    		};

    		var bindLink = function() {
    			var $link = $('a#linkpartes');
    			$link.funcToggle('click', mostrarElementosExtrasEsconderDefault, esconderElementosExtrasMostrarDefault);
    			$link.bind('click', controlarMensagemLink);
    		};

    		initPagina();
    		bindLink();
    		esconderElementosExtrasMostrarDefault();
    	});
    </script>

        </div>














































    <div style="padding-top: 10px;">











    			<h2 class="subtitle tituloDoBloco">Movimentações</h2>


    </div>





    <table style="margin-left:15px; margin-top:1px;" align="center" border="0" cellpadding="0" cellspacing="0" width="98%">


    			<thead>
    				<tr>
    				  <th width="120" class="label" style="vertical-align: bottom">Data</th>
    				  <th valign="middle" width="20" aria-hidden="true">&nbsp;</th>
    				  <th valign="middle" class="label">Movimento</th>
    				</tr>
    				<tr class="fundoEscuro" height="2" aria-hidden="true">
    					<td></td>
    					<td></td>
    					<td></td>
    				</tr>
    			</thead>


    			<tbody id="tabelaUltimasMovimentacoes">



















    	<tr class="fundoClaro containerMovimentacao" style="">
    		<td class="dataMovimentacao" width="120" style="vertical-align: top">
    			16/08/2022
    		</td>
    		<td width="20" valign="top" aria-hidden="true">

    		</td>
    		<td class="descricaoMovimentacao" style="vertical-align: top; padding-bottom: 5px">




    					Juntada de Ofício



    			<br>
    			<span style="font-style: italic;">
    				Nº Protocolo: WEB1.22.02299977-0
    Tipo da Petição: Ofício
    Data: 16/08/2022 12:49

    			</span>

    		</td>
    	</tr>






















    	<tr class="fundoEscuro containerMovimentacao" style="">
    		<td class="dataMovimentacao" width="120" style="vertical-align: top">
    			16/09/2021
    		</td>
    		<td width="20" valign="top" aria-hidden="true">

    		</td>
    		<td class="descricaoMovimentacao" style="vertical-align: top; padding-bottom: 5px">




    					Juntada de Aviso de Recebimento (AR)



    			<br>
    			<span style="font-style: italic;">

    			</span>

    		</td>
    	</tr>






















    	<tr class="fundoClaro containerMovimentacao" style="">
    		<td class="dataMovimentacao" width="120" style="vertical-align: top">
    			10/09/2021
    		</td>
    		<td width="20" valign="top" aria-hidden="true">








    				<a class="linkMovVincProc" id="linkMovVincProc-51092884" title="Visualizar documento em inteiro teor" href="#liberarAutoPorSenha">
    					<img width="16" height="16" border="0" src="/cpopg/imagens/doc.png">
    				</a>

    		</td>
    		<td class="descricaoMovimentacao" style="vertical-align: top; padding-bottom: 5px">



    					<a class="linkMovVincProc" id="linkMovVincProc-2-51092884" title="Visualizar documento em inteiro teor" href="#liberarAutoPorSenha"> Expedição de Certidão de Arquivamento
    					</a>




    			<br>
    			<span style="font-style: italic;">

    			</span>

    		</td>
    	</tr>






















    	<tr class="fundoEscuro containerMovimentacao" style="">
    		<td class="dataMovimentacao" width="120" style="vertical-align: top">
    			10/09/2021
    		</td>
    		<td width="20" valign="top" aria-hidden="true">

    		</td>
    		<td class="descricaoMovimentacao" style="vertical-align: top; padding-bottom: 5px">




    					Arquivado Definitivamente



    			<br>
    			<span style="font-style: italic;">

    			</span>

    		</td>
    	</tr>






















    	<tr class="fundoClaro containerMovimentacao" style="">
    		<td class="dataMovimentacao" width="120" style="vertical-align: top">
    			06/09/2021
    		</td>
    		<td width="20" valign="top" aria-hidden="true">

    		</td>
    		<td class="descricaoMovimentacao" style="vertical-align: top; padding-bottom: 5px">




    					Juntada de documento



    			<br>
    			<span style="font-style: italic;">

    			</span>

    		</td>
    	</tr>




    			</tbody>


    			<tbody style="display: none;" id="tabelaTodasMovimentacoes">



















    	<tr class="fundoClaro containerMovimentacao" style="">
    		<td class="dataMovimentacao" width="120" style="vertical-align: top">
    			16/08/2022
    		</td>
    		<td width="20" valign="top" aria-hidden="true">

    		</td>
    		<td class="descricaoMovimentacao" style="vertical-align: top; padding-bottom: 5px">




    					Juntada de Ofício



    			<br>
    			<span style="font-style: italic;">
    				Nº Protocolo: WEB1.22.02299977-0
    Tipo da Petição: Ofício
    Data: 16/08/2022 12:49

    			</span>

    		</td>
    	</tr>






















    	<tr class="fundoEscuro containerMovimentacao" style="">
    		<td class="dataMovimentacao" width="120" style="vertical-align: top">
    			16/09/2021
    		</td>
    		<td width="20" valign="top" aria-hidden="true">

    		</td>
    		<td class="descricaoMovimentacao" style="vertical-align: top; padding-bottom: 5px">




    					Juntada de Aviso de Recebimento (AR)



    			<br>
    			<span style="font-style: italic;">

    			</span>

    		</td>
    	</tr>






















    	<tr class="fundoClaro containerMovimentacao" style="">
    		<td class="dataMovimentacao" width="120" style="vertical-align: top">
    			10/09/2021
    		</td>
    		<td width="20" valign="top" aria-hidden="true">








    				<a class="linkMovVincProc" id="linkMovVincProc-51092884" title="Visualizar documento em inteiro teor" href="#liberarAutoPorSenha">
    					<img width="16" height="16" border="0" src="/cpopg/imagens/doc.png">
    				</a>

    		</td>
    		<td class="descricaoMovimentacao" style="vertical-align: top; padding-bottom: 5px">



    					<a class="linkMovVincProc" id="linkMovVincProc-2-51092884" title="Visualizar documento em inteiro teor" href="#liberarAutoPorSenha"> Expedição de Certidão de Arquivamento
    					</a>




    			<br>
    			<span style="font-style: italic;">

    			</span>

    		</td>
    	</tr>






















    	<tr class="fundoEscuro containerMovimentacao" style="">
    		<td class="dataMovimentacao" width="120" style="vertical-align: top">
    			10/09/2021
    		</td>
    		<td width="20" valign="top" aria-hidden="true">

    		</td>
    		<td class="descricaoMovimentacao" style="vertical-align: top; padding-bottom: 5px">




    					Arquivado Definitivamente



    			<br>
    			<span style="font-style: italic;">

    			</span>

    		</td>
    	</tr>






















    	<tr class="fundoClaro containerMovimentacao" style="">
    		<td class="dataMovimentacao" width="120" style="vertical-align: top">
    			06/09/2021
    		</td>
    		<td width="20" valign="top" aria-hidden="true">

    		</td>
    		<td class="descricaoMovimentacao" style="vertical-align: top; padding-bottom: 5px">




    					Juntada de documento



    			<br>
    			<span style="font-style: italic;">

    			</span>

    		</td>
    	</tr>






















    	<tr class="fundoEscuro containerMovimentacao" style="">
    		<td class="dataMovimentacao" width="120" style="vertical-align: top">
    			31/08/2021
    		</td>
    		<td width="20" valign="top" aria-hidden="true">

    		</td>
    		<td class="descricaoMovimentacao" style="vertical-align: top; padding-bottom: 5px">




    					Juntada de documento



    			<br>
    			<span style="font-style: italic;">

    			</span>

    		</td>
    	</tr>






















    	<tr class="fundoClaro containerMovimentacao" style="">
    		<td class="dataMovimentacao" width="120" style="vertical-align: top">
    			27/08/2021
    		</td>
    		<td width="20" valign="top" aria-hidden="true">








    				<a class="linkMovVincProc" id="linkMovVincProc-50670278" title="Visualizar documento em inteiro teor" href="#liberarAutoPorSenha">
    					<img width="16" height="16" border="0" src="/cpopg/imagens/doc.png">
    				</a>

    		</td>
    		<td class="descricaoMovimentacao" style="vertical-align: top; padding-bottom: 5px">



    					<a class="linkMovVincProc" id="linkMovVincProc-2-50670278" title="Visualizar documento em inteiro teor" href="#liberarAutoPorSenha"> Expedição de Ofício
    					</a>




    			<br>
    			<span style="font-style: italic;">

    			</span>

    		</td>
    	</tr>






















    	<tr class="fundoEscuro containerMovimentacao" style="">
    		<td class="dataMovimentacao" width="120" style="vertical-align: top">
    			26/08/2021
    		</td>
    		<td width="20" valign="top" aria-hidden="true">








    				<a class="linkMovVincProc" id="linkMovVincProc-50598180" title="Visualizar documento em inteiro teor" href="/cpopg/abrirDocumentoVinculadoMovimentacao.do?processo.codigo=01Z081I9T0000&amp;cdDocumento=50598180&amp;nmRecursoAcessado=Proferido+despacho+de+mero+expediente" target="_blank">
    					<img width="16" height="16" border="0" src="/cpopg/imagens/doc.png">
    				</a>

    		</td>
    		<td class="descricaoMovimentacao" style="vertical-align: top; padding-bottom: 5px">



    					<a class="linkMovVincProc" id="linkMovVincProc-2-50598180" title="Visualizar documento em inteiro teor" href="/cpopg/abrirDocumentoVinculadoMovimentacao.do?processo.codigo=01Z081I9T0000&amp;cdDocumento=50598180&amp;nmRecursoAcessado=Proferido+despacho+de+mero+expediente" target="_blank"> Proferido despacho de mero expediente
    					</a>




    			<br>
    			<span style="font-style: italic;">
    				Vistos em inspeção anual interna (Portaria nº 01/2021, DJe nº 2679, p. 8, em 20/08/2021) Cumpra-se a determinação contida no item III do despacho de página 556, expedindo-se ofício ao DETRAN para comunicar a proibição imposta ao réu para dirigir veículo automotor no período assinalado, bem como para encaminhar o documento retido, conforme consta na certidão de página 571. Expediente necessário.
    			</span>

    		</td>
    	</tr>






















    	<tr class="fundoClaro containerMovimentacao" style="">
    		<td class="dataMovimentacao" width="120" style="vertical-align: top">
    			26/08/2021
    		</td>
    		<td width="20" valign="top" aria-hidden="true">








    				<a class="linkMovVincProc" id="linkMovVincProc-50597944" title="Visualizar documento em inteiro teor" href="#liberarAutoPorSenha">
    					<img width="16" height="16" border="0" src="/cpopg/imagens/doc.png">
    				</a>

    		</td>
    		<td class="descricaoMovimentacao" style="vertical-align: top; padding-bottom: 5px">



    					<a class="linkMovVincProc" id="linkMovVincProc-2-50597944" title="Visualizar documento em inteiro teor" href="#liberarAutoPorSenha"> Certidão emitida
    					</a>




    			<br>
    			<span style="font-style: italic;">

    			</span>

    		</td>
    	</tr>






















    	<tr class="fundoEscuro containerMovimentacao" style="">
    		<td class="dataMovimentacao" width="120" style="vertical-align: top">
    			26/08/2021
    		</td>
    		<td width="20" valign="top" aria-hidden="true">

    		</td>
    		<td class="descricaoMovimentacao" style="vertical-align: top; padding-bottom: 5px">




    					Processo Desarquivado



    			<br>
    			<span style="font-style: italic;">

    			</span>

    		</td>
    	</tr>






















    	<tr class="fundoClaro containerMovimentacao" style="">
    		<td class="dataMovimentacao" width="120" style="vertical-align: top">
    			25/08/2021
    		</td>
    		<td width="20" valign="top" aria-hidden="true">

    		</td>
    		<td class="descricaoMovimentacao" style="vertical-align: top; padding-bottom: 5px">




    					Juntada de Carta Precatória/Rogatória



    			<br>
    			<span style="font-style: italic;">

    			</span>

    		</td>
    	</tr>






















    	<tr class="fundoEscuro containerMovimentacao" style="">
    		<td class="dataMovimentacao" width="120" style="vertical-align: top">
    			23/08/2021
    		</td>
    		<td width="20" valign="top" aria-hidden="true">








    				<a class="linkMovVincProc" id="linkMovVincProc-50459386" title="Visualizar documento em inteiro teor" href="#liberarAutoPorSenha">
    					<img width="16" height="16" border="0" src="/cpopg/imagens/doc.png">
    				</a>

    		</td>
    		<td class="descricaoMovimentacao" style="vertical-align: top; padding-bottom: 5px">



    					<a class="linkMovVincProc" id="linkMovVincProc-2-50459386" title="Visualizar documento em inteiro teor" href="#liberarAutoPorSenha"> Certidão emitida
    					</a>




    			<br>
    			<span style="font-style: italic;">

    			</span>

    		</td>
    	</tr>






















    	<tr class="fundoClaro containerMovimentacao" style="">
    		<td class="dataMovimentacao" width="120" style="vertical-align: top">
    			26/05/2021
    		</td>
    		<td width="20" valign="top" aria-hidden="true">








    				<a class="linkMovVincProc" id="linkMovVincProc-47558808" title="Visualizar documento em inteiro teor" href="#liberarAutoPorSenha">
    					<img width="16" height="16" border="0" src="/cpopg/imagens/doc.png">
    				</a>

    		</td>
    		<td class="descricaoMovimentacao" style="vertical-align: top; padding-bottom: 5px">



    					<a class="linkMovVincProc" id="linkMovVincProc-2-47558808" title="Visualizar documento em inteiro teor" href="#liberarAutoPorSenha"> Expedição de Certidão de Arquivamento
    					</a>




    			<br>
    			<span style="font-style: italic;">

    			</span>

    		</td>
    	</tr>






















    	<tr class="fundoEscuro containerMovimentacao" style="">
    		<td class="dataMovimentacao" width="120" style="vertical-align: top">
    			26/05/2021
    		</td>
    		<td width="20" valign="top" aria-hidden="true">

    		</td>
    		<td class="descricaoMovimentacao" style="vertical-align: top; padding-bottom: 5px">




    					Arquivado Definitivamente



    			<br>
    			<span style="font-style: italic;">

    			</span>

    		</td>
    	</tr>






















    	<tr class="fundoClaro containerMovimentacao" style="">
    		<td class="dataMovimentacao" width="120" style="vertical-align: top">
    			26/05/2021
    		</td>
    		<td width="20" valign="top" aria-hidden="true">








    				<a class="linkMovVincProc" id="linkMovVincProc-47558769" title="Visualizar documento em inteiro teor" href="#liberarAutoPorSenha">
    					<img width="16" height="16" border="0" src="/cpopg/imagens/doc.png">
    				</a>

    		</td>
    		<td class="descricaoMovimentacao" style="vertical-align: top; padding-bottom: 5px">



    					<a class="linkMovVincProc" id="linkMovVincProc-2-47558769" title="Visualizar documento em inteiro teor" href="#liberarAutoPorSenha"> Certidão emitida
    					</a>




    			<br>
    			<span style="font-style: italic;">

    			</span>

    		</td>
    	</tr>






















    	<tr class="fundoEscuro containerMovimentacao" style="">
    		<td class="dataMovimentacao" width="120" style="vertical-align: top">
    			26/05/2021
    		</td>
    		<td width="20" valign="top" aria-hidden="true">








    				<a class="linkMovVincProc" id="linkMovVincProc-47557334" title="Visualizar documento em inteiro teor" href="/cpopg/abrirDocumentoVinculadoMovimentacao.do?processo.codigo=01Z081I9T0000&amp;cdDocumento=47557334&amp;nmRecursoAcessado=Expedi%C3%A7%C3%A3o+de+Ato+Ordinat%C3%B3rio" target="_blank">
    					<img width="16" height="16" border="0" src="/cpopg/imagens/doc.png">
    				</a>

    		</td>
    		<td class="descricaoMovimentacao" style="vertical-align: top; padding-bottom: 5px">



    					<a class="linkMovVincProc" id="linkMovVincProc-2-47557334" title="Visualizar documento em inteiro teor" href="/cpopg/abrirDocumentoVinculadoMovimentacao.do?processo.codigo=01Z081I9T0000&amp;cdDocumento=47557334&amp;nmRecursoAcessado=Expedi%C3%A7%C3%A3o+de+Ato+Ordinat%C3%B3rio" target="_blank"> Expedição de Ato Ordinatório
    					</a>




    			<br>
    			<span style="font-style: italic;">
    				Comunico ao Departamento de Tecnologia da Informação e Comunicação da Polícia Civil do Estado do Ceará - DETIC, para fins de registros nos sistemas policiais, o seguinte: Nome do juiz(a): Silvio Pinto Falcão Filho Nome(s) do infrator/réu(s): William Azevedo dos Santos, WILLIAM AZEVEDO DOS SANTOS, brasileiro, Casado, pai Francisco das Chagas Santos, mãe Vaneide Azevedo dos Santos, Nascido/Nascida em 03/06/1984, natural de Tucurui - PA, com endereço à Rua Raimundo Félix, 24, Alto Alegre, CEP 62880-000, Horizonte - CE Número do Inquérito Policial: 196/2007 Motivo : Condenação transitada em julgado. Data da Sentença: 29/03/2016 Se condenatória (Informar artigo e pena, tipo de pena e regime): Art. 302 § 1º, II do(a) LEI 9.503/1997. Pena de dois anos e oito meses de detenção Regime inicial: aberto, a ser cumprido na Casa do Albergado. Substituição da pena privativa de liberdade por privativa de direito consistentes em prestação pecuniária e prestação de serviço à comunidade. A prestação pecuniária consistirá no pagamento de R$ 4.000,00 (quatro mil reais), dividido em duas parcelas de R$ 2.000,00 (dois mil reais), corrigidos monetariamente desde a data do arbitramento pelo INPC, a primeira em trinta dias do trânsito em julgado e a segunda no mesmo dia do mês seguinte. Data do Trânsito em Julgado: 12.04.2020
    			</span>

    		</td>
    	</tr>






















    	<tr class="fundoClaro containerMovimentacao" style="">
    		<td class="dataMovimentacao" width="120" style="vertical-align: top">
    			19/04/2021
    		</td>
    		<td width="20" valign="top" aria-hidden="true">

    		</td>
    		<td class="descricaoMovimentacao" style="vertical-align: top; padding-bottom: 5px">




    					Remessa dos autos à Vara de Origem



    			<br>
    			<span style="font-style: italic;">

    			</span>

    		</td>
    	</tr>






















    	<tr class="fundoEscuro containerMovimentacao" style="">
    		<td class="dataMovimentacao" width="120" style="vertical-align: top">
    			19/04/2021
    		</td>
    		<td width="20" valign="top" aria-hidden="true">








    				<a class="linkMovVincProc" id="linkMovVincProc-46282117" title="Visualizar documento em inteiro teor" href="#liberarAutoPorSenha">
    					<img width="16" height="16" border="0" src="/cpopg/imagens/doc.png">
    				</a>

    		</td>
    		<td class="descricaoMovimentacao" style="vertical-align: top; padding-bottom: 5px">



    					<a class="linkMovVincProc" id="linkMovVincProc-2-46282117" title="Visualizar documento em inteiro teor" href="#liberarAutoPorSenha"> Certidão emitida
    					</a>




    			<br>
    			<span style="font-style: italic;">

    			</span>

    		</td>
    	</tr>






















    	<tr class="fundoClaro containerMovimentacao" style="">
    		<td class="dataMovimentacao" width="120" style="vertical-align: top">
    			19/04/2021
    		</td>
    		<td width="20" valign="top" aria-hidden="true">








    				<a class="linkMovVincProc" id="linkMovVincProc-46272600" title="Visualizar documento em inteiro teor" href="#liberarAutoPorSenha">
    					<img width="16" height="16" border="0" src="/cpopg/imagens/doc.png">
    				</a>

    		</td>
    		<td class="descricaoMovimentacao" style="vertical-align: top; padding-bottom: 5px">



    					<a class="linkMovVincProc" id="linkMovVincProc-2-46272600" title="Visualizar documento em inteiro teor" href="#liberarAutoPorSenha"> Certidão emitida
    					</a>




    			<br>
    			<span style="font-style: italic;">

    			</span>

    		</td>
    	</tr>






















    	<tr class="fundoEscuro containerMovimentacao" style="">
    		<td class="dataMovimentacao" width="120" style="vertical-align: top">
    			19/04/2021
    		</td>
    		<td width="20" valign="top" aria-hidden="true">

    		</td>
    		<td class="descricaoMovimentacao" style="vertical-align: top; padding-bottom: 5px">




    					Juntada de documento



    			<br>
    			<span style="font-style: italic;">

    			</span>

    		</td>
    	</tr>






















    	<tr class="fundoClaro containerMovimentacao" style="">
    		<td class="dataMovimentacao" width="120" style="vertical-align: top">
    			07/04/2021
    		</td>
    		<td width="20" valign="top" aria-hidden="true">








    				<a class="linkMovVincProc" id="linkMovVincProc-45911398" title="Visualizar documento em inteiro teor" href="#liberarAutoPorSenha">
    					<img width="16" height="16" border="0" src="/cpopg/imagens/doc.png">
    				</a>

    		</td>
    		<td class="descricaoMovimentacao" style="vertical-align: top; padding-bottom: 5px">



    					<a class="linkMovVincProc" id="linkMovVincProc-2-45911398" title="Visualizar documento em inteiro teor" href="#liberarAutoPorSenha"> Certidão emitida
    					</a>




    			<br>
    			<span style="font-style: italic;">

    			</span>

    		</td>
    	</tr>






















    	<tr class="fundoEscuro containerMovimentacao" style="">
    		<td class="dataMovimentacao" width="120" style="vertical-align: top">
    			07/04/2021
    		</td>
    		<td width="20" valign="top" aria-hidden="true">








    				<a class="linkMovVincProc" id="linkMovVincProc-45911237" title="Visualizar documento em inteiro teor" href="#liberarAutoPorSenha">
    					<img width="16" height="16" border="0" src="/cpopg/imagens/doc.png">
    				</a>

    		</td>
    		<td class="descricaoMovimentacao" style="vertical-align: top; padding-bottom: 5px">



    					<a class="linkMovVincProc" id="linkMovVincProc-2-45911237" title="Visualizar documento em inteiro teor" href="#liberarAutoPorSenha"> Certidão emitida
    					</a>




    			<br>
    			<span style="font-style: italic;">

    			</span>

    		</td>
    	</tr>






















    	<tr class="fundoClaro containerMovimentacao" style="">
    		<td class="dataMovimentacao" width="120" style="vertical-align: top">
    			07/04/2021
    		</td>
    		<td width="20" valign="top" aria-hidden="true">

    		</td>
    		<td class="descricaoMovimentacao" style="vertical-align: top; padding-bottom: 5px">




    					Juntada de Ofício



    			<br>
    			<span style="font-style: italic;">

    			</span>

    		</td>
    	</tr>






















    	<tr class="fundoEscuro containerMovimentacao" style="">
    		<td class="dataMovimentacao" width="120" style="vertical-align: top">
    			06/04/2021
    		</td>
    		<td width="20" valign="top" aria-hidden="true">

    		</td>
    		<td class="descricaoMovimentacao" style="vertical-align: top; padding-bottom: 5px">




    					Juntada de documento



    			<br>
    			<span style="font-style: italic;">

    			</span>

    		</td>
    	</tr>






















    	<tr class="fundoClaro containerMovimentacao" style="">
    		<td class="dataMovimentacao" width="120" style="vertical-align: top">
    			31/03/2021
    		</td>
    		<td width="20" valign="top" aria-hidden="true">








    				<a class="linkMovVincProc" id="linkMovVincProc-45738770" title="Visualizar documento em inteiro teor" href="#liberarAutoPorSenha">
    					<img width="16" height="16" border="0" src="/cpopg/imagens/doc.png">
    				</a>

    		</td>
    		<td class="descricaoMovimentacao" style="vertical-align: top; padding-bottom: 5px">



    					<a class="linkMovVincProc" id="linkMovVincProc-2-45738770" title="Visualizar documento em inteiro teor" href="#liberarAutoPorSenha"> Expedida carta precatória
    					</a>




    			<br>
    			<span style="font-style: italic;">

    			</span>

    		</td>
    	</tr>






















    	<tr class="fundoEscuro containerMovimentacao" style="">
    		<td class="dataMovimentacao" width="120" style="vertical-align: top">
    			31/03/2021
    		</td>
    		<td width="20" valign="top" aria-hidden="true">








    				<a class="linkMovVincProc" id="linkMovVincProc-45739083" title="Visualizar documento em inteiro teor" href="#liberarAutoPorSenha">
    					<img width="16" height="16" border="0" src="/cpopg/imagens/doc.png">
    				</a>

    		</td>
    		<td class="descricaoMovimentacao" style="vertical-align: top; padding-bottom: 5px">



    					<a class="linkMovVincProc" id="linkMovVincProc-2-45739083" title="Visualizar documento em inteiro teor" href="#liberarAutoPorSenha"> Certidão emitida
    					</a>




    			<br>
    			<span style="font-style: italic;">

    			</span>

    		</td>
    	</tr>






















    	<tr class="fundoClaro containerMovimentacao" style="">
    		<td class="dataMovimentacao" width="120" style="vertical-align: top">
    			29/03/2021
    		</td>
    		<td width="20" valign="top" aria-hidden="true">








    				<a class="linkMovVincProc" id="linkMovVincProc-45523704" title="Visualizar documento em inteiro teor" href="/cpopg/abrirDocumentoVinculadoMovimentacao.do?processo.codigo=01Z081I9T0000&amp;cdDocumento=45523704&amp;nmRecursoAcessado=Proferido+despacho+de+mero+expediente" target="_blank">
    					<img width="16" height="16" border="0" src="/cpopg/imagens/doc.png">
    				</a>

    		</td>
    		<td class="descricaoMovimentacao" style="vertical-align: top; padding-bottom: 5px">



    					<a class="linkMovVincProc" id="linkMovVincProc-2-45523704" title="Visualizar documento em inteiro teor" href="/cpopg/abrirDocumentoVinculadoMovimentacao.do?processo.codigo=01Z081I9T0000&amp;cdDocumento=45523704&amp;nmRecursoAcessado=Proferido+despacho+de+mero+expediente" target="_blank"> Proferido despacho de mero expediente
    					</a>




    			<br>
    			<span style="font-style: italic;">
    				Vistos em conclusão. I - Considerando o teor do decisório de págs. 544/550, que transitou em julgado em 12/05/2020 (pág. 553), atualize-se o histórico do apenado WILLIAM AZEVEDO DOS SANTOS no sistema SAJPG. II - Comunique-se ao T.R.E (artigo 71, § 2º, do Código Eleitoral, c/c o art. 15, III, da Constituição Federal), através do Sistema Pólis. III Intime-se o sentenciado, por mandado, para entregar a carteira de habilitação no Gabinete deste Juízo, no prazo de 05 (cinco) dias, após o retorno do atendimento presencial no Fórum. Após a entrega da CNH, oficie-se o DETRAN comunicando a proibição imposta ao réu para dirigir veículo automotor no período assinalado, bem como para encaminhar o documento retido. IV- Expeça-se Carta de Guia à Vara de Execução de Penas Alternativas. V Após o cumprimento das providências acima ordenadas, arquivem-se os presentes autos. Expedientes necessários.
    			</span>

    		</td>
    	</tr>






















    	<tr class="fundoEscuro containerMovimentacao" style="">
    		<td class="dataMovimentacao" width="120" style="vertical-align: top">
    			15/05/2020
    		</td>
    		<td width="20" valign="top" aria-hidden="true">

    		</td>
    		<td class="descricaoMovimentacao" style="vertical-align: top; padding-bottom: 5px">




    					Concluso para Despacho



    			<br>
    			<span style="font-style: italic;">

    			</span>

    		</td>
    	</tr>






















    	<tr class="fundoClaro containerMovimentacao" style="">
    		<td class="dataMovimentacao" width="120" style="vertical-align: top">
    			14/05/2020
    		</td>
    		<td width="20" valign="top" aria-hidden="true">

    		</td>
    		<td class="descricaoMovimentacao" style="vertical-align: top; padding-bottom: 5px">




    					Certificação de Processo Julgado



    			<br>
    			<span style="font-style: italic;">
    				Processo devolvido do SG.
    			</span>

    		</td>
    	</tr>






















    	<tr class="fundoEscuro containerMovimentacao" style="">
    		<td class="dataMovimentacao" width="120" style="vertical-align: top">
    			14/05/2020
    		</td>
    		<td width="20" valign="top" aria-hidden="true">

    		</td>
    		<td class="descricaoMovimentacao" style="vertical-align: top; padding-bottom: 5px">




    					Recebido Recurso Eletrônico



    			<br>
    			<span style="font-style: italic;">
    				Data do julgamento: 21/05/2018 13:46:48
    Tipo de julgamento: Decisão monocrática
    Decisão: Ante o exposto, com base no art. 1.030, inciso V, do CPC, admito o recurso especial. Expedientes necessários. Fortaleza, 18 de maio de 2018. Desembargador WASHINGTON LUÍS BEZERRA DE ARAÚJO Vice-Presidente do TJCE
    Relatora: MARIA DAS GRAÇAS ALMEIDA DE QUENTAL-PORT.723/2018
    			</span>

    		</td>
    	</tr>






















    	<tr class="fundoClaro containerMovimentacao" style="">
    		<td class="dataMovimentacao" width="120" style="vertical-align: top">
    			02/05/2018
    		</td>
    		<td width="20" valign="top" aria-hidden="true">

    		</td>
    		<td class="descricaoMovimentacao" style="vertical-align: top; padding-bottom: 5px">




    					Processo Redistribuído por Sorteio



    			<br>
    			<span style="font-style: italic;">
    				res 06/2018
    			</span>

    		</td>
    	</tr>






















    	<tr class="fundoEscuro containerMovimentacao" style="">
    		<td class="dataMovimentacao" width="120" style="vertical-align: top">
    			01/05/2018
    		</td>
    		<td width="20" valign="top" aria-hidden="true">

    		</td>
    		<td class="descricaoMovimentacao" style="vertical-align: top; padding-bottom: 5px">




    					Remetidos os Autos para o Distribuidor Local



    			<br>
    			<span style="font-style: italic;">

    			</span>

    		</td>
    	</tr>






















    	<tr class="fundoClaro containerMovimentacao" style="">
    		<td class="dataMovimentacao" width="120" style="vertical-align: top">
    			01/05/2018
    		</td>
    		<td width="20" valign="top" aria-hidden="true">








    				<a class="linkMovVincProc" id="linkMovVincProc-17942441" title="Visualizar documento em inteiro teor" href="#liberarAutoPorSenha">
    					<img width="16" height="16" border="0" src="/cpopg/imagens/doc.png">
    				</a>

    		</td>
    		<td class="descricaoMovimentacao" style="vertical-align: top; padding-bottom: 5px">



    					<a class="linkMovVincProc" id="linkMovVincProc-2-17942441" title="Visualizar documento em inteiro teor" href="#liberarAutoPorSenha"> Certidão emitida
    					</a>




    			<br>
    			<span style="font-style: italic;">

    			</span>

    		</td>
    	</tr>






















    	<tr class="fundoEscuro containerMovimentacao" style="">
    		<td class="dataMovimentacao" width="120" style="vertical-align: top">
    			27/04/2018
    		</td>
    		<td width="20" valign="top" aria-hidden="true">

    		</td>
    		<td class="descricaoMovimentacao" style="vertical-align: top; padding-bottom: 5px">




    					Remessa dos Autos para fins de Redistribuição



    			<br>
    			<span style="font-style: italic;">

    			</span>

    		</td>
    	</tr>






















    	<tr class="fundoClaro containerMovimentacao" style="">
    		<td class="dataMovimentacao" width="120" style="vertical-align: top">
    			17/04/2018
    		</td>
    		<td width="20" valign="top" aria-hidden="true">








    				<a class="linkMovVincProc" id="linkMovVincProc-17720838" title="Visualizar documento em inteiro teor" href="#liberarAutoPorSenha">
    					<img width="16" height="16" border="0" src="/cpopg/imagens/doc.png">
    				</a>

    		</td>
    		<td class="descricaoMovimentacao" style="vertical-align: top; padding-bottom: 5px">



    					<a class="linkMovVincProc" id="linkMovVincProc-2-17720838" title="Visualizar documento em inteiro teor" href="#liberarAutoPorSenha"> Certidão emitida
    					</a>




    			<br>
    			<span style="font-style: italic;">

    			</span>

    		</td>
    	</tr>






















    	<tr class="fundoEscuro containerMovimentacao" style="">
    		<td class="dataMovimentacao" width="120" style="vertical-align: top">
    			26/06/2017
    		</td>
    		<td width="20" valign="top" aria-hidden="true">








    				<a class="linkMovVincProc" id="linkMovVincProc-14033456" title="Visualizar documento em inteiro teor" href="#liberarAutoPorSenha">
    					<img width="16" height="16" border="0" src="/cpopg/imagens/doc.png">
    				</a>

    		</td>
    		<td class="descricaoMovimentacao" style="vertical-align: top; padding-bottom: 5px">



    					<a class="linkMovVincProc" id="linkMovVincProc-2-14033456" title="Visualizar documento em inteiro teor" href="#liberarAutoPorSenha"> Certidão emitida
    					</a>




    			<br>
    			<span style="font-style: italic;">

    			</span>

    		</td>
    	</tr>






















    	<tr class="fundoClaro containerMovimentacao" style="">
    		<td class="dataMovimentacao" width="120" style="vertical-align: top">
    			14/09/2016
    		</td>
    		<td width="20" valign="top" aria-hidden="true">








    				<a class="linkMovVincProc" id="linkMovVincProc-11220120" title="Visualizar documento em inteiro teor" href="#liberarAutoPorSenha">
    					<img width="16" height="16" border="0" src="/cpopg/imagens/doc.png">
    				</a>

    		</td>
    		<td class="descricaoMovimentacao" style="vertical-align: top; padding-bottom: 5px">



    					<a class="linkMovVincProc" id="linkMovVincProc-2-11220120" title="Visualizar documento em inteiro teor" href="#liberarAutoPorSenha"> Certidão emitida
    					</a>




    			<br>
    			<span style="font-style: italic;">

    			</span>

    		</td>
    	</tr>






















    	<tr class="fundoEscuro containerMovimentacao" style="">
    		<td class="dataMovimentacao" width="120" style="vertical-align: top">
    			14/09/2016
    		</td>
    		<td width="20" valign="top" aria-hidden="true">

    		</td>
    		<td class="descricaoMovimentacao" style="vertical-align: top; padding-bottom: 5px">




    					Juntada de Ofício



    			<br>
    			<span style="font-style: italic;">

    			</span>

    		</td>
    	</tr>






















    	<tr class="fundoClaro containerMovimentacao" style="">
    		<td class="dataMovimentacao" width="120" style="vertical-align: top">
    			01/09/2016
    		</td>
    		<td width="20" valign="top" aria-hidden="true">

    		</td>
    		<td class="descricaoMovimentacao" style="vertical-align: top; padding-bottom: 5px">




    					Remetido Recurso Eletrônico ao Tribunal de Justiça



    			<br>
    			<span style="font-style: italic;">

    			</span>

    		</td>
    	</tr>






















    	<tr class="fundoEscuro containerMovimentacao" style="">
    		<td class="dataMovimentacao" width="120" style="vertical-align: top">
    			01/09/2016
    		</td>
    		<td width="20" valign="top" aria-hidden="true">

    		</td>
    		<td class="descricaoMovimentacao" style="vertical-align: top; padding-bottom: 5px">




    					Juntada de Carta Precatória/Rogatória



    			<br>
    			<span style="font-style: italic;">

    			</span>

    		</td>
    	</tr>






















    	<tr class="fundoClaro containerMovimentacao" style="">
    		<td class="dataMovimentacao" width="120" style="vertical-align: top">
    			01/09/2016
    		</td>
    		<td width="20" valign="top" aria-hidden="true">

    		</td>
    		<td class="descricaoMovimentacao" style="vertical-align: top; padding-bottom: 5px">




    					Juntada de documento



    			<br>
    			<span style="font-style: italic;">

    			</span>

    		</td>
    	</tr>






















    	<tr class="fundoEscuro containerMovimentacao" style="">
    		<td class="dataMovimentacao" width="120" style="vertical-align: top">
    			25/08/2016
    		</td>
    		<td width="20" valign="top" aria-hidden="true">

    		</td>
    		<td class="descricaoMovimentacao" style="vertical-align: top; padding-bottom: 5px">




    					Juntada de documento



    			<br>
    			<span style="font-style: italic;">

    			</span>

    		</td>
    	</tr>






















    	<tr class="fundoClaro containerMovimentacao" style="">
    		<td class="dataMovimentacao" width="120" style="vertical-align: top">
    			25/08/2016
    		</td>
    		<td width="20" valign="top" aria-hidden="true">








    				<a class="linkMovVincProc" id="linkMovVincProc-11135188" title="Visualizar documento em inteiro teor" href="#liberarAutoPorSenha">
    					<img width="16" height="16" border="0" src="/cpopg/imagens/doc.png">
    				</a>

    		</td>
    		<td class="descricaoMovimentacao" style="vertical-align: top; padding-bottom: 5px">



    					<a class="linkMovVincProc" id="linkMovVincProc-2-11135188" title="Visualizar documento em inteiro teor" href="#liberarAutoPorSenha"> Expedição de Ofício
    					</a>




    			<br>
    			<span style="font-style: italic;">

    			</span>

    		</td>
    	</tr>






















    	<tr class="fundoEscuro containerMovimentacao" style="">
    		<td class="dataMovimentacao" width="120" style="vertical-align: top">
    			24/08/2016
    		</td>
    		<td width="20" valign="top" aria-hidden="true">








    				<a class="linkMovVincProc" id="linkMovVincProc-11116003" title="Visualizar documento em inteiro teor" href="/cpopg/abrirDocumentoVinculadoMovimentacao.do?processo.codigo=01Z081I9T0000&amp;cdDocumento=11116003&amp;nmRecursoAcessado=Proferido+despacho+de+mero+expediente" target="_blank">
    					<img width="16" height="16" border="0" src="/cpopg/imagens/doc.png">
    				</a>

    		</td>
    		<td class="descricaoMovimentacao" style="vertical-align: top; padding-bottom: 5px">



    					<a class="linkMovVincProc" id="linkMovVincProc-2-11116003" title="Visualizar documento em inteiro teor" href="/cpopg/abrirDocumentoVinculadoMovimentacao.do?processo.codigo=01Z081I9T0000&amp;cdDocumento=11116003&amp;nmRecursoAcessado=Proferido+despacho+de+mero+expediente" target="_blank"> Proferido despacho de mero expediente
    					</a>




    			<br>
    			<span style="font-style: italic;">
    				Solicite-se o cumprimento da carta precatória de pág. 281 por intermédio da Corregedoria Geral da Justiça do Estado do Ceará. Oficie-se para essa finalidade.
    			</span>

    		</td>
    	</tr>






















    	<tr class="fundoClaro containerMovimentacao" style="">
    		<td class="dataMovimentacao" width="120" style="vertical-align: top">
    			23/08/2016
    		</td>
    		<td width="20" valign="top" aria-hidden="true">

    		</td>
    		<td class="descricaoMovimentacao" style="vertical-align: top; padding-bottom: 5px">




    					Concluso para Despacho



    			<br>
    			<span style="font-style: italic;">

    			</span>

    		</td>
    	</tr>






















    	<tr class="fundoEscuro containerMovimentacao" style="">
    		<td class="dataMovimentacao" width="120" style="vertical-align: top">
    			23/08/2016
    		</td>
    		<td width="20" valign="top" aria-hidden="true">








    				<a class="linkMovVincProc" id="linkMovVincProc-11115965" title="Visualizar documento em inteiro teor" href="#liberarAutoPorSenha">
    					<img width="16" height="16" border="0" src="/cpopg/imagens/doc.png">
    				</a>

    		</td>
    		<td class="descricaoMovimentacao" style="vertical-align: top; padding-bottom: 5px">



    					<a class="linkMovVincProc" id="linkMovVincProc-2-11115965" title="Visualizar documento em inteiro teor" href="#liberarAutoPorSenha"> Certidão emitida
    					</a>




    			<br>
    			<span style="font-style: italic;">

    			</span>

    		</td>
    	</tr>






















    	<tr class="fundoClaro containerMovimentacao" style="">
    		<td class="dataMovimentacao" width="120" style="vertical-align: top">
    			18/08/2016
    		</td>
    		<td width="20" valign="top" aria-hidden="true">

    		</td>
    		<td class="descricaoMovimentacao" style="vertical-align: top; padding-bottom: 5px">




    					Juntada de Petição



    			<br>
    			<span style="font-style: italic;">
    				Nº Protocolo: WEB1.16.10377382-2
    Tipo da Petição: Pedido de Juntada de Documento
    Data: 17/08/2016 18:29

    			</span>

    		</td>
    	</tr>






















    	<tr class="fundoEscuro containerMovimentacao" style="">
    		<td class="dataMovimentacao" width="120" style="vertical-align: top">
    			09/08/2016
    		</td>
    		<td width="20" valign="top" aria-hidden="true">

    		</td>
    		<td class="descricaoMovimentacao" style="vertical-align: top; padding-bottom: 5px">




    					Juntada de Petição



    			<br>
    			<span style="font-style: italic;">
    				Nº Protocolo: WEB1.16.10361896-7
    Tipo da Petição: RECURSO DE APELAÇÃO
    Data: 08/08/2016 18:17

    			</span>

    		</td>
    	</tr>






















    	<tr class="fundoClaro containerMovimentacao" style="">
    		<td class="dataMovimentacao" width="120" style="vertical-align: top">
    			28/06/2016
    		</td>
    		<td width="20" valign="top" aria-hidden="true">

    		</td>
    		<td class="descricaoMovimentacao" style="vertical-align: top; padding-bottom: 5px">




    					Juntada de documento



    			<br>
    			<span style="font-style: italic;">

    			</span>

    		</td>
    	</tr>






















    	<tr class="fundoEscuro containerMovimentacao" style="">
    		<td class="dataMovimentacao" width="120" style="vertical-align: top">
    			28/06/2016
    		</td>
    		<td width="20" valign="top" aria-hidden="true">








    				<a class="linkMovVincProc" id="linkMovVincProc-10619134" title="Visualizar documento em inteiro teor" href="#liberarAutoPorSenha">
    					<img width="16" height="16" border="0" src="/cpopg/imagens/doc.png">
    				</a>

    		</td>
    		<td class="descricaoMovimentacao" style="vertical-align: top; padding-bottom: 5px">



    					<a class="linkMovVincProc" id="linkMovVincProc-2-10619134" title="Visualizar documento em inteiro teor" href="#liberarAutoPorSenha"> Expedição de Ofício
    					</a>




    			<br>
    			<span style="font-style: italic;">

    			</span>

    		</td>
    	</tr>






















    	<tr class="fundoClaro containerMovimentacao" style="">
    		<td class="dataMovimentacao" width="120" style="vertical-align: top">
    			23/06/2016
    		</td>
    		<td width="20" valign="top" aria-hidden="true">








    				<a class="linkMovVincProc" id="linkMovVincProc-10427855" title="Visualizar documento em inteiro teor" href="/cpopg/abrirDocumentoVinculadoMovimentacao.do?processo.codigo=01Z081I9T0000&amp;cdDocumento=10427855&amp;nmRecursoAcessado=Proferido+despacho+de+mero+expediente" target="_blank">
    					<img width="16" height="16" border="0" src="/cpopg/imagens/doc.png">
    				</a>

    		</td>
    		<td class="descricaoMovimentacao" style="vertical-align: top; padding-bottom: 5px">



    					<a class="linkMovVincProc" id="linkMovVincProc-2-10427855" title="Visualizar documento em inteiro teor" href="/cpopg/abrirDocumentoVinculadoMovimentacao.do?processo.codigo=01Z081I9T0000&amp;cdDocumento=10427855&amp;nmRecursoAcessado=Proferido+despacho+de+mero+expediente" target="_blank"> Proferido despacho de mero expediente
    					</a>




    			<br>
    			<span style="font-style: italic;">
    				Visto em inspeção ordinária - Portaria nº 01/2016.Oficie-se ao Juízo deprecado solicitando o cumprimento da carta precatória, no prazo de trinta(30) dias..
    			</span>

    		</td>
    	</tr>






















    	<tr class="fundoEscuro containerMovimentacao" style="">
    		<td class="dataMovimentacao" width="120" style="vertical-align: top">
    			13/05/2016
    		</td>
    		<td width="20" valign="top" aria-hidden="true">

    		</td>
    		<td class="descricaoMovimentacao" style="vertical-align: top; padding-bottom: 5px">




    					Juntada de Petição



    			<br>
    			<span style="font-style: italic;">
    				Nº Protocolo: WEB1.16.10209425-5
    Tipo da Petição: Contrarrazões Recursais
    Data: 13/05/2016 19:17

    			</span>

    		</td>
    	</tr>






















    	<tr class="fundoClaro containerMovimentacao" style="">
    		<td class="dataMovimentacao" width="120" style="vertical-align: top">
    			26/04/2016
    		</td>
    		<td width="20" valign="top" aria-hidden="true">








    				<a class="linkMovVincProc" id="linkMovVincProc-9966271" title="Visualizar documento em inteiro teor" href="#liberarAutoPorSenha">
    					<img width="16" height="16" border="0" src="/cpopg/imagens/doc.png">
    				</a>

    		</td>
    		<td class="descricaoMovimentacao" style="vertical-align: top; padding-bottom: 5px">



    					<a class="linkMovVincProc" id="linkMovVincProc-2-9966271" title="Visualizar documento em inteiro teor" href="#liberarAutoPorSenha"> Certidão emitida
    					</a>




    			<br>
    			<span style="font-style: italic;">

    			</span>

    		</td>
    	</tr>






















    	<tr class="fundoEscuro containerMovimentacao" style="">
    		<td class="dataMovimentacao" width="120" style="vertical-align: top">
    			15/04/2016
    		</td>
    		<td width="20" valign="top" aria-hidden="true">








    				<a class="linkMovVincProc" id="linkMovVincProc-9889336" title="Visualizar documento em inteiro teor" href="#liberarAutoPorSenha">
    					<img width="16" height="16" border="0" src="/cpopg/imagens/doc.png">
    				</a>

    		</td>
    		<td class="descricaoMovimentacao" style="vertical-align: top; padding-bottom: 5px">



    					<a class="linkMovVincProc" id="linkMovVincProc-2-9889336" title="Visualizar documento em inteiro teor" href="#liberarAutoPorSenha"> Certidão emitida
    					</a>




    			<br>
    			<span style="font-style: italic;">

    			</span>

    		</td>
    	</tr>






















    	<tr class="fundoClaro containerMovimentacao" style="">
    		<td class="dataMovimentacao" width="120" style="vertical-align: top">
    			14/04/2016
    		</td>
    		<td width="20" valign="top" aria-hidden="true">








    				<a class="linkMovVincProc" id="linkMovVincProc-9882609" title="Visualizar documento em inteiro teor" href="/cpopg/abrirDocumentoVinculadoMovimentacao.do?processo.codigo=01Z081I9T0000&amp;cdDocumento=9882609&amp;nmRecursoAcessado=Recebido+o+recurso+Com+efeito+suspensivo" target="_blank">
    					<img width="16" height="16" border="0" src="/cpopg/imagens/doc.png">
    				</a>

    		</td>
    		<td class="descricaoMovimentacao" style="vertical-align: top; padding-bottom: 5px">



    					<a class="linkMovVincProc" id="linkMovVincProc-2-9882609" title="Visualizar documento em inteiro teor" href="/cpopg/abrirDocumentoVinculadoMovimentacao.do?processo.codigo=01Z081I9T0000&amp;cdDocumento=9882609&amp;nmRecursoAcessado=Recebido+o+recurso+Com+efeito+suspensivo" target="_blank"> Recebido o recurso Com efeito suspensivo
    					</a>




    			<br>
    			<span style="font-style: italic;">
    				Recebo a apelação de pág. 301/320 no efeito suspensivo. Dê-se vista dos autos à representante ministerial para apresentar suas contrarrazões, no prazo de 08 (oito) dias.Apresentadas ou transcorrido o prazo, e devolvido o mandado de intimação do réu, sigam os autos ao TJ/CE.
    			</span>

    		</td>
    	</tr>






















    	<tr class="fundoEscuro containerMovimentacao" style="">
    		<td class="dataMovimentacao" width="120" style="vertical-align: top">
    			14/04/2016
    		</td>
    		<td width="20" valign="top" aria-hidden="true">

    		</td>
    		<td class="descricaoMovimentacao" style="vertical-align: top; padding-bottom: 5px">




    					Concluso para Decisão Interlocutória



    			<br>
    			<span style="font-style: italic;">

    			</span>

    		</td>
    	</tr>






















    	<tr class="fundoClaro containerMovimentacao" style="">
    		<td class="dataMovimentacao" width="120" style="vertical-align: top">
    			13/04/2016
    		</td>
    		<td width="20" valign="top" aria-hidden="true">

    		</td>
    		<td class="descricaoMovimentacao" style="vertical-align: top; padding-bottom: 5px">




    					Juntada de Petição



    			<br>
    			<span style="font-style: italic;">
    				Nº Protocolo: WEB1.16.10158782-7
    Tipo da Petição: RECURSO DE APELAÇÃO
    Data: 13/04/2016 20:11

    			</span>

    		</td>
    	</tr>






















    	<tr class="fundoEscuro containerMovimentacao" style="">
    		<td class="dataMovimentacao" width="120" style="vertical-align: top">
    			09/04/2016
    		</td>
    		<td width="20" valign="top" aria-hidden="true">








    				<a class="linkMovVincProc" id="linkMovVincProc-9843254" title="Visualizar documento em inteiro teor" href="#liberarAutoPorSenha">
    					<img width="16" height="16" border="0" src="/cpopg/imagens/doc.png">
    				</a>

    		</td>
    		<td class="descricaoMovimentacao" style="vertical-align: top; padding-bottom: 5px">



    					<a class="linkMovVincProc" id="linkMovVincProc-2-9843254" title="Visualizar documento em inteiro teor" href="#liberarAutoPorSenha"> Certidão emitida
    					</a>




    			<br>
    			<span style="font-style: italic;">

    			</span>

    		</td>
    	</tr>






















    	<tr class="fundoClaro containerMovimentacao" style="">
    		<td class="dataMovimentacao" width="120" style="vertical-align: top">
    			09/04/2016
    		</td>
    		<td width="20" valign="top" aria-hidden="true">








    				<a class="linkMovVincProc" id="linkMovVincProc-9843253" title="Visualizar documento em inteiro teor" href="#liberarAutoPorSenha">
    					<img width="16" height="16" border="0" src="/cpopg/imagens/doc.png">
    				</a>

    		</td>
    		<td class="descricaoMovimentacao" style="vertical-align: top; padding-bottom: 5px">



    					<a class="linkMovVincProc" id="linkMovVincProc-2-9843253" title="Visualizar documento em inteiro teor" href="#liberarAutoPorSenha"> Certidão emitida
    					</a>




    			<br>
    			<span style="font-style: italic;">

    			</span>

    		</td>
    	</tr>






















    	<tr class="fundoEscuro containerMovimentacao" style="">
    		<td class="dataMovimentacao" width="120" style="vertical-align: top">
    			06/04/2016
    		</td>
    		<td width="20" valign="top" aria-hidden="true">

    		</td>
    		<td class="descricaoMovimentacao" style="vertical-align: top; padding-bottom: 5px">




    					Juntada de documento



    			<br>
    			<span style="font-style: italic;">

    			</span>

    		</td>
    	</tr>






















    	<tr class="fundoClaro containerMovimentacao" style="">
    		<td class="dataMovimentacao" width="120" style="vertical-align: top">
    			29/03/2016
    		</td>
    		<td width="20" valign="top" aria-hidden="true">








    				<a class="linkMovVincProc" id="linkMovVincProc-9735595" title="Visualizar documento em inteiro teor" href="#liberarAutoPorSenha">
    					<img width="16" height="16" border="0" src="/cpopg/imagens/doc.png">
    				</a>

    		</td>
    		<td class="descricaoMovimentacao" style="vertical-align: top; padding-bottom: 5px">



    					<a class="linkMovVincProc" id="linkMovVincProc-2-9735595" title="Visualizar documento em inteiro teor" href="#liberarAutoPorSenha"> Certidão emitida
    					</a>




    			<br>
    			<span style="font-style: italic;">

    			</span>

    		</td>
    	</tr>






















    	<tr class="fundoEscuro containerMovimentacao" style="">
    		<td class="dataMovimentacao" width="120" style="vertical-align: top">
    			29/03/2016
    		</td>
    		<td width="20" valign="top" aria-hidden="true">








    				<a class="linkMovVincProc" id="linkMovVincProc-9735590" title="Visualizar documento em inteiro teor" href="#liberarAutoPorSenha">
    					<img width="16" height="16" border="0" src="/cpopg/imagens/doc.png">
    				</a>

    		</td>
    		<td class="descricaoMovimentacao" style="vertical-align: top; padding-bottom: 5px">



    					<a class="linkMovVincProc" id="linkMovVincProc-2-9735590" title="Visualizar documento em inteiro teor" href="#liberarAutoPorSenha"> Certidão emitida
    					</a>




    			<br>
    			<span style="font-style: italic;">

    			</span>

    		</td>
    	</tr>






















    	<tr class="fundoClaro containerMovimentacao" style="">
    		<td class="dataMovimentacao" width="120" style="vertical-align: top">
    			29/03/2016
    		</td>
    		<td width="20" valign="top" aria-hidden="true">








    				<a class="linkMovVincProc" id="linkMovVincProc-9733623" title="Visualizar documento em inteiro teor" href="/cpopg/abrirDocumentoVinculadoMovimentacao.do?processo.codigo=01Z081I9T0000&amp;cdDocumento=9733623&amp;nmRecursoAcessado=Embargos+de+Declara%C3%A7%C3%A3o+N%C3%A3o-acolhidos" target="_blank">
    					<img width="16" height="16" border="0" src="/cpopg/imagens/doc.png">
    				</a>

    		</td>
    		<td class="descricaoMovimentacao" style="vertical-align: top; padding-bottom: 5px">



    					<a class="linkMovVincProc" id="linkMovVincProc-2-9733623" title="Visualizar documento em inteiro teor" href="/cpopg/abrirDocumentoVinculadoMovimentacao.do?processo.codigo=01Z081I9T0000&amp;cdDocumento=9733623&amp;nmRecursoAcessado=Embargos+de+Declara%C3%A7%C3%A3o+N%C3%A3o-acolhidos" target="_blank"> Embargos de Declaração Não-acolhidos
    					</a>




    			<br>
    			<span style="font-style: italic;">
    				Cuida-se de embargos declaratórios manejados pela defesa do réu WILLIAM AZEVEDO DOS SANTOS, respaldado no artigo 382 do CPP. Conforme previsão do artigo 620 do CPP os embargos de declaração serão deduzidos em requerimento onde constem os pontos em que a sentença é ambígua, obscura, contraditória ou omissa, de modo a distingui-los do inconformismo próprio da apelação.Da petição que interpõe o embargo não há como identificar quais os argumentos que o postulante reputa vícios da sentença, pois ora narra que houve problemas de formação, acreditando tratar-se de arquivo corrompido, ora alega ausência de fundamentação e de justificativa na prolação do decreto condenatório. A sentença apresentada é sintética, abandona a disposição analítica, sem que isso represente afronta à indicação do CPP. A apresentação sintética, dividida por tópicos, reproduz a complexidade própria dos crimes de trânsito, sem comprometer qualquer dos seus requisitos essenciais. A solução do processo volta-se prioritariamente para agilidade e objetividade na exposição dos fatos, fundamento e dispositivo. No presente caso não há qualquer argumento de acusação, ou defesa, que tenha deixado de ser mencionado e apreciado circunstanciadamente. A vinculação a fórmulas não é capaz de oferecer resposta consentânea com as modernas exigências a que o Judiciário é desafiado: agilidade, clareza e segurança. O protagonismo desse processo deve ser compartilhado por todos que integram o sistema de justiça. Nesse sentido, é muito importante a crítica que surge da iniciativa recursal, desde que hábil a indicar que as deficiências da nova fórmula que merecem aprimoramento. O artigo 381 do CPP indica o conteúdo obrigatório da sentença como sendo: nomes das partes; exposição sucinta da acusação e da defesa; a indicação dos motivos de fato e de direito em que se fundar a decisão; a indicação dos artigos de lei aplicados; o dispositivo; data e a assinatura do juiz. O embargo não identifica a omissão ou insuficiência de qualquer deles, limita-se a imputar falta fundamentação, sem indicar qual argumento da acusação ou defesa que não foi apreciado fundamentadamente, para que a omissão possa ser suprida.Os embargos de declaração excepcionam a regra geral dos recursos, pois a sua interposição não visa necessariamente a reforma da decisão recorrida, mas à supressão de vício ou defeito que comprometa a compreensão do ato decisório.Desse modo, não havendo omissão capaz de admitir a oposição de embargos declaratórios, cumpre reconhecer a inadequação da pretensão veiculada pelo embargante, ante a ausência de pressuposto recursal, sendo impróprio o seu uso como sucedâneo da apelação ou como forma de exercitar efeito regressivo estranho à modalidade recursal eleita, contrariando à logica processual e os fins pretendidos pela norma vigente.Ante o exposto, rejeito os embargos declaratórios manejados pela defesa, em razão da ausência de pressuposto processual intrínseco ao recebimento do recurso, previsto no art. 620 do Código de Processo Penal, não há obscuridade, ambigüidade, contradição ou omissão a ser suprida.Intimem-se as partes. Prazo recursal interrompido apenas para a defesa. Intime-se para recontagem.
    			</span>

    		</td>
    	</tr>






















    	<tr class="fundoEscuro containerMovimentacao" style="">
    		<td class="dataMovimentacao" width="120" style="vertical-align: top">
    			25/03/2016
    		</td>
    		<td width="20" valign="top" aria-hidden="true">








    				<a class="linkMovVincProc" id="linkMovVincProc-9718093" title="Visualizar documento em inteiro teor" href="#liberarAutoPorSenha">
    					<img width="16" height="16" border="0" src="/cpopg/imagens/doc.png">
    				</a>

    		</td>
    		<td class="descricaoMovimentacao" style="vertical-align: top; padding-bottom: 5px">



    					<a class="linkMovVincProc" id="linkMovVincProc-2-9718093" title="Visualizar documento em inteiro teor" href="#liberarAutoPorSenha"> Certidão emitida
    					</a>




    			<br>
    			<span style="font-style: italic;">

    			</span>

    		</td>
    	</tr>






















    	<tr class="fundoClaro containerMovimentacao" style="">
    		<td class="dataMovimentacao" width="120" style="vertical-align: top">
    			22/03/2016
    		</td>
    		<td width="20" valign="top" aria-hidden="true">

    		</td>
    		<td class="descricaoMovimentacao" style="vertical-align: top; padding-bottom: 5px">




    					Concluso para Decisão Interlocutória



    			<br>
    			<span style="font-style: italic;">

    			</span>

    		</td>
    	</tr>






















    	<tr class="fundoEscuro containerMovimentacao" style="">
    		<td class="dataMovimentacao" width="120" style="vertical-align: top">
    			22/03/2016
    		</td>
    		<td width="20" valign="top" aria-hidden="true">

    		</td>
    		<td class="descricaoMovimentacao" style="vertical-align: top; padding-bottom: 5px">




    					Juntada de Petição



    			<br>
    			<span style="font-style: italic;">
    				Nº Protocolo: WEB1.16.10122590-9
    Tipo da Petição: Embargos de Declaração
    Data: 21/03/2016 22:08

    			</span>

    		</td>
    	</tr>






















    	<tr class="fundoClaro containerMovimentacao" style="">
    		<td class="dataMovimentacao" width="120" style="vertical-align: top">
    			22/03/2016
    		</td>
    		<td width="20" valign="top" aria-hidden="true">

    		</td>
    		<td class="descricaoMovimentacao" style="vertical-align: top; padding-bottom: 5px">




    					Processo entranhado



    			<br>
    			<span style="font-style: italic;">
    				Entranhado o processo 0070337-91.2008.8.06.0001/01 - Classe: Embargos de Declaração em Ação Penal - Procedimento Ordinário - Assunto principal: Crimes de Trânsito
    			</span>

    		</td>
    	</tr>






















    	<tr class="fundoEscuro containerMovimentacao" style="">
    		<td class="dataMovimentacao" width="120" style="vertical-align: top">
    			22/03/2016
    		</td>
    		<td width="20" valign="top" aria-hidden="true">

    		</td>
    		<td class="descricaoMovimentacao" style="vertical-align: top; padding-bottom: 5px">




    					Recurso interposto



    			<br>
    			<span style="font-style: italic;">
    				Seq.: 01 - Embargos de Declaração
    			</span>

    		</td>
    	</tr>






















    	<tr class="fundoClaro containerMovimentacao" style="">
    		<td class="dataMovimentacao" width="120" style="vertical-align: top">
    			17/03/2016
    		</td>
    		<td width="20" valign="top" aria-hidden="true">








    				<a class="linkMovVincProc" id="linkMovVincProc-9641630" title="Visualizar documento em inteiro teor" href="#liberarAutoPorSenha">
    					<img width="16" height="16" border="0" src="/cpopg/imagens/doc.png">
    				</a>

    		</td>
    		<td class="descricaoMovimentacao" style="vertical-align: top; padding-bottom: 5px">



    					<a class="linkMovVincProc" id="linkMovVincProc-2-9641630" title="Visualizar documento em inteiro teor" href="#liberarAutoPorSenha"> Expedida carta precatória
    					</a>




    			<br>
    			<span style="font-style: italic;">

    			</span>

    		</td>
    	</tr>






















    	<tr class="fundoEscuro containerMovimentacao" style="">
    		<td class="dataMovimentacao" width="120" style="vertical-align: top">
    			14/03/2016
    		</td>
    		<td width="20" valign="top" aria-hidden="true">








    				<a class="linkMovVincProc" id="linkMovVincProc-9618413" title="Visualizar documento em inteiro teor" href="#liberarAutoPorSenha">
    					<img width="16" height="16" border="0" src="/cpopg/imagens/doc.png">
    				</a>

    		</td>
    		<td class="descricaoMovimentacao" style="vertical-align: top; padding-bottom: 5px">



    					<a class="linkMovVincProc" id="linkMovVincProc-2-9618413" title="Visualizar documento em inteiro teor" href="#liberarAutoPorSenha"> Certidão emitida
    					</a>




    			<br>
    			<span style="font-style: italic;">

    			</span>

    		</td>
    	</tr>






















    	<tr class="fundoClaro containerMovimentacao" style="">
    		<td class="dataMovimentacao" width="120" style="vertical-align: top">
    			14/03/2016
    		</td>
    		<td width="20" valign="top" aria-hidden="true">








    				<a class="linkMovVincProc" id="linkMovVincProc-9618412" title="Visualizar documento em inteiro teor" href="#liberarAutoPorSenha">
    					<img width="16" height="16" border="0" src="/cpopg/imagens/doc.png">
    				</a>

    		</td>
    		<td class="descricaoMovimentacao" style="vertical-align: top; padding-bottom: 5px">



    					<a class="linkMovVincProc" id="linkMovVincProc-2-9618412" title="Visualizar documento em inteiro teor" href="#liberarAutoPorSenha"> Certidão emitida
    					</a>




    			<br>
    			<span style="font-style: italic;">

    			</span>

    		</td>
    	</tr>






















    	<tr class="fundoEscuro containerMovimentacao" style="">
    		<td class="dataMovimentacao" width="120" style="vertical-align: top">
    			10/03/2016
    		</td>
    		<td width="20" valign="top" aria-hidden="true">








    				<a class="linkMovVincProc" id="linkMovVincProc-9585965" title="Visualizar documento em inteiro teor" href="/cpopg/abrirDocumentoVinculadoMovimentacao.do?processo.codigo=01Z081I9T0000&amp;cdDocumento=9585965&amp;nmRecursoAcessado=Julgado+procedente+o+pedido" target="_blank">
    					<img width="16" height="16" border="0" src="/cpopg/imagens/doc.png">
    				</a>

    		</td>
    		<td class="descricaoMovimentacao" style="vertical-align: top; padding-bottom: 5px">



    					<a class="linkMovVincProc" id="linkMovVincProc-2-9585965" title="Visualizar documento em inteiro teor" href="/cpopg/abrirDocumentoVinculadoMovimentacao.do?processo.codigo=01Z081I9T0000&amp;cdDocumento=9585965&amp;nmRecursoAcessado=Julgado+procedente+o+pedido" target="_blank"> Julgado procedente o pedido
    					</a>




    			<br>
    			<span style="font-style: italic;">
    				DISPOSITIVO Condeno o réu. Circunstâncias judiciais:Nenhuma digna de menção Pena base: dois anos de detenção Aumento: Um terço em razão da majorante prevista no art. 302, § 1º, II da Lei 9.503/97 Pena Final:dois anos e oito meses de detenção Regime inicial: aberto, a ser cumprido na Casa do Albergado. Valor mínimo para reparação dos danos causados pela infração, considerando os prejuízos sofridos pelo ofendido artigo 387, IV do CPP: R$ 4.000,00 (quatro mil reais) com pagamento até dez dias após o trânsito em julgado. Após isso acrescer 50% Suspensão ou de proibição de se obter a permissão ou a habilitação para dirigir veículo automotor, previsto no artigo 293 do CTB: nove meses (se houver morte), seis (lesão corporal). A pena privativa de liberdade não é superior a quatro anos, o crime é culposo e o réu não é reincidente em crime doloso. A culpabilidade, os antecedentes, a conduta social e a personalidade do condenado, bem como os motivos e as circunstâncias indicam que a substituição da pena privativa de liberdade por privativa de direito consistentes em prestação pecuniária e prestação de serviço à comunidade. A última poderá ser substituída por limitação de fim de semana (art. 48 do CPP), a critério do juiz da execução. A prestação pecuniária consistirá no pagamento de R$ 4.000,00 (quatro mil reais), dividido em duas parcelas de R$ 2.000,00 (dois mil reais), corrigidos monetariamente desde a data do arbitramento pelo INPC, a primeira em trinta dias do trânsito em julgado e a segunda no mesmo dia do mês seguinte, depositados na conta-corrente nº 5873-4 da agência 3515-7 do Banco do Brasil, em benefício do INSTITUTO DO CORAÇÃO DA CRIANÇA E DO ADOLESCENTE - INCOR CRIANÇA, localizado na r. Núbia Barrocas n° 125 Parque Manibura Fortaleza-CE | CEP: 60.821-775, fone: (85) 3492-9400 / (85) 3492-9401 / (85) 3492-9402. O(A) réu(ré) deverá apresentar os comprovantes de depósito mensalmente, tão logo efetue o pagamento, desde já advertido(a) que a transposição de cinco dias da data limite para pagamento de qualquer parcela, sem justificativa, será tida por descumprimento da obrigação e poderá importar na retomada da pena privativa de liberdade substituída. A prestação de serviço à comunidade deverá ser realizada gratuitamente, de acordo com suas aptidões, por prazo igual ao fixado para a pena privativa de liberdade, à razão de uma hora de tarefa por dia de condenação, fixadas de modo a não prejudicar a jornada normal de trabalho, preferencialmente junto à PEFOCE, ou qualquer outro órgão direta ou indiretamente ligado com o trânsito (IML, AMC, DETRAN), de modo a aproximar o(a) réu(ré) das repercussões dos crimes de trânsito. Outro destino poderá ser especificado pelo Juiz das execuções penais competente. O acompanhamento no cumprimento das penas alternativas incumbirá ao juízo da execução criminal competente, para onde deverá ser encaminhada carta de guia. Fica desde logo determinada a conversão da pena restritiva de direitos em privativa de liberdade (art. 44 § 4º do CPB) quando ocorrer o descumprimento e o condenado não apresentar justificativa nos cinco dias que se seguirem, independente de intimação. Após o trânsito em julgado: Réu(ré) Entrega da carteira de habilitação no prazo de cinco dias na secretaria da vara. A transposição desse prazo sem a providência determinada será tida como suficiente para inviabilizar a fruição do benefício da substituição da pena privativa de liberdade por restritiva de direito. Vítima ou familiares Possibilidade de executar a sentença no juízo cível, sem prejuízo da apuração do dano efetivamente sofrido em ação autônoma (art. 63 parágrafo único do CPP). Secretaria Após entregue a CNH, oficiar o DETRAN comunicando a proibição imposta a(o) ré(u) para dirigir veículo automotor no período assinalado, bem como para encaminhar o documento retido. Transposto o prazo sem entrega ou justificativa, desconsiderar a pena substitutiva. Suspender direitos políticos ativos e passivos do réu, (art. 15, II CF/88). Expedir carta de guia ao juízo da execução. Arquivamento com baixa.
    			</span>

    		</td>
    	</tr>






















    	<tr class="fundoClaro containerMovimentacao" style="">
    		<td class="dataMovimentacao" width="120" style="vertical-align: top">
    			03/03/2016
    		</td>
    		<td width="20" valign="top" aria-hidden="true">

    		</td>
    		<td class="descricaoMovimentacao" style="vertical-align: top; padding-bottom: 5px">




    					Concluso para Sentença



    			<br>
    			<span style="font-style: italic;">

    			</span>

    		</td>
    	</tr>






















    	<tr class="fundoEscuro containerMovimentacao" style="">
    		<td class="dataMovimentacao" width="120" style="vertical-align: top">
    			03/03/2016
    		</td>
    		<td width="20" valign="top" aria-hidden="true">

    		</td>
    		<td class="descricaoMovimentacao" style="vertical-align: top; padding-bottom: 5px">




    					Juntada de Petição



    			<br>
    			<span style="font-style: italic;">
    				Nº Protocolo: WEB1.16.10092085-9
    Tipo da Petição: Memoriais
    Data: 03/03/2016 09:58

    			</span>

    		</td>
    	</tr>






















    	<tr class="fundoClaro containerMovimentacao" style="">
    		<td class="dataMovimentacao" width="120" style="vertical-align: top">
    			19/11/2015
    		</td>
    		<td width="20" valign="top" aria-hidden="true">








    				<a class="linkMovVincProc" id="linkMovVincProc-8767174" title="Visualizar documento em inteiro teor" href="#liberarAutoPorSenha">
    					<img width="16" height="16" border="0" src="/cpopg/imagens/doc.png">
    				</a>

    		</td>
    		<td class="descricaoMovimentacao" style="vertical-align: top; padding-bottom: 5px">



    					<a class="linkMovVincProc" id="linkMovVincProc-2-8767174" title="Visualizar documento em inteiro teor" href="#liberarAutoPorSenha"> Certidão emitida
    					</a>




    			<br>
    			<span style="font-style: italic;">

    			</span>

    		</td>
    	</tr>






















    	<tr class="fundoEscuro containerMovimentacao" style="">
    		<td class="dataMovimentacao" width="120" style="vertical-align: top">
    			19/11/2015
    		</td>
    		<td width="20" valign="top" aria-hidden="true">

    		</td>
    		<td class="descricaoMovimentacao" style="vertical-align: top; padding-bottom: 5px">




    					Juntada de documento



    			<br>
    			<span style="font-style: italic;">

    			</span>

    		</td>
    	</tr>






















    	<tr class="fundoClaro containerMovimentacao" style="">
    		<td class="dataMovimentacao" width="120" style="vertical-align: top">
    			01/04/2015
    		</td>
    		<td width="20" valign="top" aria-hidden="true">

    		</td>
    		<td class="descricaoMovimentacao" style="vertical-align: top; padding-bottom: 5px">




    					Certidão com o Recebimento da Intimação Pessoal do Defensor



    			<br>
    			<span style="font-style: italic;">

    			</span>

    		</td>
    	</tr>






















    	<tr class="fundoEscuro containerMovimentacao" style="">
    		<td class="dataMovimentacao" width="120" style="vertical-align: top">
    			15/10/2014
    		</td>
    		<td width="20" valign="top" aria-hidden="true">

    		</td>
    		<td class="descricaoMovimentacao" style="vertical-align: top; padding-bottom: 5px">




    					Juntada de Petição



    			<br>
    			<span style="font-style: italic;">
    				Nº Protocolo: WEB1.14.71565572-1
    Tipo da Petição: Memoriais
    Data: 15/10/2014 18:11

    			</span>

    		</td>
    	</tr>






















    	<tr class="fundoClaro containerMovimentacao" style="">
    		<td class="dataMovimentacao" width="120" style="vertical-align: top">
    			10/10/2014
    		</td>
    		<td width="20" valign="top" aria-hidden="true">

    		</td>
    		<td class="descricaoMovimentacao" style="vertical-align: top; padding-bottom: 5px">




    					Juntada de Carta Precatória/Rogatória



    			<br>
    			<span style="font-style: italic;">
    				Nº Protocolo: PROT.14.01353297-0
    Tipo da Petição: Retorno de Carta Precatória
    Data: 06/10/2014 12:54
    Complemento: Acompanha mídia original(CD).

    			</span>

    		</td>
    	</tr>






















    	<tr class="fundoEscuro containerMovimentacao" style="">
    		<td class="dataMovimentacao" width="120" style="vertical-align: top">
    			17/07/2014
    		</td>
    		<td width="20" valign="top" aria-hidden="true">

    		</td>
    		<td class="descricaoMovimentacao" style="vertical-align: top; padding-bottom: 5px">




    					Juntada de Ofício



    			<br>
    			<span style="font-style: italic;">

    			</span>

    		</td>
    	</tr>






















    	<tr class="fundoClaro containerMovimentacao" style="">
    		<td class="dataMovimentacao" width="120" style="vertical-align: top">
    			13/06/2014
    		</td>
    		<td width="20" valign="top" aria-hidden="true">








    				<a class="linkMovVincProc" id="linkMovVincProc-4915093" title="Visualizar documento em inteiro teor" href="#liberarAutoPorSenha">
    					<img width="16" height="16" border="0" src="/cpopg/imagens/doc.png">
    				</a>

    		</td>
    		<td class="descricaoMovimentacao" style="vertical-align: top; padding-bottom: 5px">



    					<a class="linkMovVincProc" id="linkMovVincProc-2-4915093" title="Visualizar documento em inteiro teor" href="#liberarAutoPorSenha"> Decorrido prazo
    					</a>




    			<br>
    			<span style="font-style: italic;">

    			</span>

    		</td>
    	</tr>






















    	<tr class="fundoEscuro containerMovimentacao" style="">
    		<td class="dataMovimentacao" width="120" style="vertical-align: top">
    			05/05/2014
    		</td>
    		<td width="20" valign="top" aria-hidden="true">

    		</td>
    		<td class="descricaoMovimentacao" style="vertical-align: top; padding-bottom: 5px">




    					Juntada de Ofício



    			<br>
    			<span style="font-style: italic;">

    			</span>

    		</td>
    	</tr>






















    	<tr class="fundoClaro containerMovimentacao" style="">
    		<td class="dataMovimentacao" width="120" style="vertical-align: top">
    			15/04/2014
    		</td>
    		<td width="20" valign="top" aria-hidden="true">

    		</td>
    		<td class="descricaoMovimentacao" style="vertical-align: top; padding-bottom: 5px">




    					Juntada de Aviso de Recebimento (AR)



    			<br>
    			<span style="font-style: italic;">

    			</span>

    		</td>
    	</tr>






















    	<tr class="fundoEscuro containerMovimentacao" style="">
    		<td class="dataMovimentacao" width="120" style="vertical-align: top">
    			26/02/2014
    		</td>
    		<td width="20" valign="top" aria-hidden="true">

    		</td>
    		<td class="descricaoMovimentacao" style="vertical-align: top; padding-bottom: 5px">




    					Juntada de documento



    			<br>
    			<span style="font-style: italic;">

    			</span>

    		</td>
    	</tr>






















    	<tr class="fundoClaro containerMovimentacao" style="">
    		<td class="dataMovimentacao" width="120" style="vertical-align: top">
    			20/02/2014
    		</td>
    		<td width="20" valign="top" aria-hidden="true">








    				<a class="linkMovVincProc" id="linkMovVincProc-4220808" title="Visualizar documento em inteiro teor" href="#liberarAutoPorSenha">
    					<img width="16" height="16" border="0" src="/cpopg/imagens/doc.png">
    				</a>

    		</td>
    		<td class="descricaoMovimentacao" style="vertical-align: top; padding-bottom: 5px">



    					<a class="linkMovVincProc" id="linkMovVincProc-2-4220808" title="Visualizar documento em inteiro teor" href="#liberarAutoPorSenha"> Expedida carta precatória
    					</a>




    			<br>
    			<span style="font-style: italic;">

    			</span>

    		</td>
    	</tr>






















    	<tr class="fundoEscuro containerMovimentacao" style="">
    		<td class="dataMovimentacao" width="120" style="vertical-align: top">
    			13/02/2014
    		</td>
    		<td width="20" valign="top" aria-hidden="true">








    				<a class="linkMovVincProc" id="linkMovVincProc-4119649" title="Visualizar documento em inteiro teor" href="#liberarAutoPorSenha">
    					<img width="16" height="16" border="0" src="/cpopg/imagens/doc.png">
    				</a>

    		</td>
    		<td class="descricaoMovimentacao" style="vertical-align: top; padding-bottom: 5px">



    					<a class="linkMovVincProc" id="linkMovVincProc-2-4119649" title="Visualizar documento em inteiro teor" href="#liberarAutoPorSenha"> Expedição de Termo de Audiência
    					</a>




    			<br>
    			<span style="font-style: italic;">

    			</span>

    		</td>
    	</tr>






















    	<tr class="fundoClaro containerMovimentacao" style="">
    		<td class="dataMovimentacao" width="120" style="vertical-align: top">
    			10/02/2014
    		</td>
    		<td width="20" valign="top" aria-hidden="true">








    				<a class="linkMovVincProc" id="linkMovVincProc-4119522" title="Visualizar documento em inteiro teor" href="#liberarAutoPorSenha">
    					<img width="16" height="16" border="0" src="/cpopg/imagens/doc.png">
    				</a>

    		</td>
    		<td class="descricaoMovimentacao" style="vertical-align: top; padding-bottom: 5px">



    					<a class="linkMovVincProc" id="linkMovVincProc-2-4119522" title="Visualizar documento em inteiro teor" href="#liberarAutoPorSenha"> Expedição de Termo
    					</a>




    			<br>
    			<span style="font-style: italic;">

    			</span>

    		</td>
    	</tr>






















    	<tr class="fundoEscuro containerMovimentacao" style="">
    		<td class="dataMovimentacao" width="120" style="vertical-align: top">
    			04/02/2014
    		</td>
    		<td width="20" valign="top" aria-hidden="true">

    		</td>
    		<td class="descricaoMovimentacao" style="vertical-align: top; padding-bottom: 5px">




    					Juntada de mandado



    			<br>
    			<span style="font-style: italic;">

    			</span>

    		</td>
    	</tr>






















    	<tr class="fundoClaro containerMovimentacao" style="">
    		<td class="dataMovimentacao" width="120" style="vertical-align: top">
    			30/01/2014
    		</td>
    		<td width="20" valign="top" aria-hidden="true">

    		</td>
    		<td class="descricaoMovimentacao" style="vertical-align: top; padding-bottom: 5px">




    					Juntada de mandado



    			<br>
    			<span style="font-style: italic;">

    			</span>

    		</td>
    	</tr>






















    	<tr class="fundoEscuro containerMovimentacao" style="">
    		<td class="dataMovimentacao" width="120" style="vertical-align: top">
    			28/01/2014
    		</td>
    		<td width="20" valign="top" aria-hidden="true">

    		</td>
    		<td class="descricaoMovimentacao" style="vertical-align: top; padding-bottom: 5px">




    					Juntada de documento



    			<br>
    			<span style="font-style: italic;">

    			</span>

    		</td>
    	</tr>






















    	<tr class="fundoClaro containerMovimentacao" style="">
    		<td class="dataMovimentacao" width="120" style="vertical-align: top">
    			28/01/2014
    		</td>
    		<td width="20" valign="top" aria-hidden="true">

    		</td>
    		<td class="descricaoMovimentacao" style="vertical-align: top; padding-bottom: 5px">




    					Juntada de documento



    			<br>
    			<span style="font-style: italic;">

    			</span>

    		</td>
    	</tr>






















    	<tr class="fundoEscuro containerMovimentacao" style="">
    		<td class="dataMovimentacao" width="120" style="vertical-align: top">
    			28/01/2014
    		</td>
    		<td width="20" valign="top" aria-hidden="true">

    		</td>
    		<td class="descricaoMovimentacao" style="vertical-align: top; padding-bottom: 5px">




    					Juntada de mandado



    			<br>
    			<span style="font-style: italic;">

    			</span>

    		</td>
    	</tr>






















    	<tr class="fundoClaro containerMovimentacao" style="">
    		<td class="dataMovimentacao" width="120" style="vertical-align: top">
    			28/01/2014
    		</td>
    		<td width="20" valign="top" aria-hidden="true">

    		</td>
    		<td class="descricaoMovimentacao" style="vertical-align: top; padding-bottom: 5px">




    					Juntada de documento



    			<br>
    			<span style="font-style: italic;">

    			</span>

    		</td>
    	</tr>






















    	<tr class="fundoEscuro containerMovimentacao" style="">
    		<td class="dataMovimentacao" width="120" style="vertical-align: top">
    			28/01/2014
    		</td>
    		<td width="20" valign="top" aria-hidden="true">

    		</td>
    		<td class="descricaoMovimentacao" style="vertical-align: top; padding-bottom: 5px">




    					Juntada de documento



    			<br>
    			<span style="font-style: italic;">

    			</span>

    		</td>
    	</tr>






















    	<tr class="fundoClaro containerMovimentacao" style="">
    		<td class="dataMovimentacao" width="120" style="vertical-align: top">
    			28/01/2014
    		</td>
    		<td width="20" valign="top" aria-hidden="true">

    		</td>
    		<td class="descricaoMovimentacao" style="vertical-align: top; padding-bottom: 5px">




    					Juntada de documento



    			<br>
    			<span style="font-style: italic;">

    			</span>

    		</td>
    	</tr>






















    	<tr class="fundoEscuro containerMovimentacao" style="">
    		<td class="dataMovimentacao" width="120" style="vertical-align: top">
    			28/01/2014
    		</td>
    		<td width="20" valign="top" aria-hidden="true">

    		</td>
    		<td class="descricaoMovimentacao" style="vertical-align: top; padding-bottom: 5px">




    					Juntada de documento



    			<br>
    			<span style="font-style: italic;">

    			</span>

    		</td>
    	</tr>






















    	<tr class="fundoClaro containerMovimentacao" style="">
    		<td class="dataMovimentacao" width="120" style="vertical-align: top">
    			28/01/2014
    		</td>
    		<td width="20" valign="top" aria-hidden="true">

    		</td>
    		<td class="descricaoMovimentacao" style="vertical-align: top; padding-bottom: 5px">




    					Juntada de documento



    			<br>
    			<span style="font-style: italic;">

    			</span>

    		</td>
    	</tr>






















    	<tr class="fundoEscuro containerMovimentacao" style="">
    		<td class="dataMovimentacao" width="120" style="vertical-align: top">
    			28/01/2014
    		</td>
    		<td width="20" valign="top" aria-hidden="true">

    		</td>
    		<td class="descricaoMovimentacao" style="vertical-align: top; padding-bottom: 5px">




    					Juntada de Parecer do Ministério Público



    			<br>
    			<span style="font-style: italic;">

    			</span>

    		</td>
    	</tr>






















    	<tr class="fundoClaro containerMovimentacao" style="">
    		<td class="dataMovimentacao" width="120" style="vertical-align: top">
    			28/01/2014
    		</td>
    		<td width="20" valign="top" aria-hidden="true">

    		</td>
    		<td class="descricaoMovimentacao" style="vertical-align: top; padding-bottom: 5px">




    					Juntada de documento



    			<br>
    			<span style="font-style: italic;">

    			</span>

    		</td>
    	</tr>






















    	<tr class="fundoEscuro containerMovimentacao" style="">
    		<td class="dataMovimentacao" width="120" style="vertical-align: top">
    			28/01/2014
    		</td>
    		<td width="20" valign="top" aria-hidden="true">

    		</td>
    		<td class="descricaoMovimentacao" style="vertical-align: top; padding-bottom: 5px">




    					Juntada de documento



    			<br>
    			<span style="font-style: italic;">

    			</span>

    		</td>
    	</tr>






















    	<tr class="fundoClaro containerMovimentacao" style="">
    		<td class="dataMovimentacao" width="120" style="vertical-align: top">
    			28/01/2014
    		</td>
    		<td width="20" valign="top" aria-hidden="true">

    		</td>
    		<td class="descricaoMovimentacao" style="vertical-align: top; padding-bottom: 5px">




    					Juntada de Petição



    			<br>
    			<span style="font-style: italic;">

    			</span>

    		</td>
    	</tr>






















    	<tr class="fundoEscuro containerMovimentacao" style="">
    		<td class="dataMovimentacao" width="120" style="vertical-align: top">
    			28/01/2014
    		</td>
    		<td width="20" valign="top" aria-hidden="true">

    		</td>
    		<td class="descricaoMovimentacao" style="vertical-align: top; padding-bottom: 5px">




    					Juntada de documento



    			<br>
    			<span style="font-style: italic;">

    			</span>

    		</td>
    	</tr>






















    	<tr class="fundoClaro containerMovimentacao" style="">
    		<td class="dataMovimentacao" width="120" style="vertical-align: top">
    			28/01/2014
    		</td>
    		<td width="20" valign="top" aria-hidden="true">

    		</td>
    		<td class="descricaoMovimentacao" style="vertical-align: top; padding-bottom: 5px">




    					Juntada de documento



    			<br>
    			<span style="font-style: italic;">

    			</span>

    		</td>
    	</tr>






















    	<tr class="fundoEscuro containerMovimentacao" style="">
    		<td class="dataMovimentacao" width="120" style="vertical-align: top">
    			28/01/2014
    		</td>
    		<td width="20" valign="top" aria-hidden="true">

    		</td>
    		<td class="descricaoMovimentacao" style="vertical-align: top; padding-bottom: 5px">




    					Juntada de documento



    			<br>
    			<span style="font-style: italic;">

    			</span>

    		</td>
    	</tr>






















    	<tr class="fundoClaro containerMovimentacao" style="">
    		<td class="dataMovimentacao" width="120" style="vertical-align: top">
    			28/01/2014
    		</td>
    		<td width="20" valign="top" aria-hidden="true">

    		</td>
    		<td class="descricaoMovimentacao" style="vertical-align: top; padding-bottom: 5px">




    					Juntada de documento



    			<br>
    			<span style="font-style: italic;">

    			</span>

    		</td>
    	</tr>






















    	<tr class="fundoEscuro containerMovimentacao" style="">
    		<td class="dataMovimentacao" width="120" style="vertical-align: top">
    			28/01/2014
    		</td>
    		<td width="20" valign="top" aria-hidden="true">

    		</td>
    		<td class="descricaoMovimentacao" style="vertical-align: top; padding-bottom: 5px">




    					Juntada de Petição



    			<br>
    			<span style="font-style: italic;">

    			</span>

    		</td>
    	</tr>






















    	<tr class="fundoClaro containerMovimentacao" style="">
    		<td class="dataMovimentacao" width="120" style="vertical-align: top">
    			28/01/2014
    		</td>
    		<td width="20" valign="top" aria-hidden="true">

    		</td>
    		<td class="descricaoMovimentacao" style="vertical-align: top; padding-bottom: 5px">




    					Juntada de mandado



    			<br>
    			<span style="font-style: italic;">

    			</span>

    		</td>
    	</tr>






















    	<tr class="fundoEscuro containerMovimentacao" style="">
    		<td class="dataMovimentacao" width="120" style="vertical-align: top">
    			28/01/2014
    		</td>
    		<td width="20" valign="top" aria-hidden="true">

    		</td>
    		<td class="descricaoMovimentacao" style="vertical-align: top; padding-bottom: 5px">




    					Juntada de documento



    			<br>
    			<span style="font-style: italic;">

    			</span>

    		</td>
    	</tr>






















    	<tr class="fundoClaro containerMovimentacao" style="">
    		<td class="dataMovimentacao" width="120" style="vertical-align: top">
    			28/01/2014
    		</td>
    		<td width="20" valign="top" aria-hidden="true">

    		</td>
    		<td class="descricaoMovimentacao" style="vertical-align: top; padding-bottom: 5px">




    					Juntada de documento



    			<br>
    			<span style="font-style: italic;">

    			</span>

    		</td>
    	</tr>






















    	<tr class="fundoEscuro containerMovimentacao" style="">
    		<td class="dataMovimentacao" width="120" style="vertical-align: top">
    			28/01/2014
    		</td>
    		<td width="20" valign="top" aria-hidden="true">

    		</td>
    		<td class="descricaoMovimentacao" style="vertical-align: top; padding-bottom: 5px">




    					Juntada de documento



    			<br>
    			<span style="font-style: italic;">

    			</span>

    		</td>
    	</tr>






















    	<tr class="fundoClaro containerMovimentacao" style="">
    		<td class="dataMovimentacao" width="120" style="vertical-align: top">
    			28/01/2014
    		</td>
    		<td width="20" valign="top" aria-hidden="true">

    		</td>
    		<td class="descricaoMovimentacao" style="vertical-align: top; padding-bottom: 5px">




    					Juntada de documento



    			<br>
    			<span style="font-style: italic;">

    			</span>

    		</td>
    	</tr>






















    	<tr class="fundoEscuro containerMovimentacao" style="">
    		<td class="dataMovimentacao" width="120" style="vertical-align: top">
    			28/01/2014
    		</td>
    		<td width="20" valign="top" aria-hidden="true">

    		</td>
    		<td class="descricaoMovimentacao" style="vertical-align: top; padding-bottom: 5px">




    					Juntada de documento



    			<br>
    			<span style="font-style: italic;">

    			</span>

    		</td>
    	</tr>






















    	<tr class="fundoClaro containerMovimentacao" style="">
    		<td class="dataMovimentacao" width="120" style="vertical-align: top">
    			28/01/2014
    		</td>
    		<td width="20" valign="top" aria-hidden="true">

    		</td>
    		<td class="descricaoMovimentacao" style="vertical-align: top; padding-bottom: 5px">




    					Juntada de Aviso de Recebimento (AR)



    			<br>
    			<span style="font-style: italic;">

    			</span>

    		</td>
    	</tr>






















    	<tr class="fundoEscuro containerMovimentacao" style="">
    		<td class="dataMovimentacao" width="120" style="vertical-align: top">
    			28/01/2014
    		</td>
    		<td width="20" valign="top" aria-hidden="true">

    		</td>
    		<td class="descricaoMovimentacao" style="vertical-align: top; padding-bottom: 5px">




    					Juntada de documento



    			<br>
    			<span style="font-style: italic;">

    			</span>

    		</td>
    	</tr>






















    	<tr class="fundoClaro containerMovimentacao" style="">
    		<td class="dataMovimentacao" width="120" style="vertical-align: top">
    			28/01/2014
    		</td>
    		<td width="20" valign="top" aria-hidden="true">

    		</td>
    		<td class="descricaoMovimentacao" style="vertical-align: top; padding-bottom: 5px">




    					Juntada de documento



    			<br>
    			<span style="font-style: italic;">

    			</span>

    		</td>
    	</tr>






















    	<tr class="fundoEscuro containerMovimentacao" style="">
    		<td class="dataMovimentacao" width="120" style="vertical-align: top">
    			28/01/2014
    		</td>
    		<td width="20" valign="top" aria-hidden="true">

    		</td>
    		<td class="descricaoMovimentacao" style="vertical-align: top; padding-bottom: 5px">




    					Juntada de documento



    			<br>
    			<span style="font-style: italic;">

    			</span>

    		</td>
    	</tr>






















    	<tr class="fundoClaro containerMovimentacao" style="">
    		<td class="dataMovimentacao" width="120" style="vertical-align: top">
    			28/01/2014
    		</td>
    		<td width="20" valign="top" aria-hidden="true">

    		</td>
    		<td class="descricaoMovimentacao" style="vertical-align: top; padding-bottom: 5px">




    					Juntada de Petição



    			<br>
    			<span style="font-style: italic;">

    			</span>

    		</td>
    	</tr>






















    	<tr class="fundoEscuro containerMovimentacao" style="">
    		<td class="dataMovimentacao" width="120" style="vertical-align: top">
    			28/01/2014
    		</td>
    		<td width="20" valign="top" aria-hidden="true">

    		</td>
    		<td class="descricaoMovimentacao" style="vertical-align: top; padding-bottom: 5px">




    					Juntada de documento



    			<br>
    			<span style="font-style: italic;">

    			</span>

    		</td>
    	</tr>






















    	<tr class="fundoClaro containerMovimentacao" style="">
    		<td class="dataMovimentacao" width="120" style="vertical-align: top">
    			28/01/2014
    		</td>
    		<td width="20" valign="top" aria-hidden="true">

    		</td>
    		<td class="descricaoMovimentacao" style="vertical-align: top; padding-bottom: 5px">




    					Juntada de Denúncia



    			<br>
    			<span style="font-style: italic;">

    			</span>

    		</td>
    	</tr>






















    	<tr class="fundoEscuro containerMovimentacao" style="">
    		<td class="dataMovimentacao" width="120" style="vertical-align: top">
    			28/01/2014
    		</td>
    		<td width="20" valign="top" aria-hidden="true">

    		</td>
    		<td class="descricaoMovimentacao" style="vertical-align: top; padding-bottom: 5px">




    					Juntada de documento



    			<br>
    			<span style="font-style: italic;">

    			</span>

    		</td>
    	</tr>






















    	<tr class="fundoClaro containerMovimentacao" style="">
    		<td class="dataMovimentacao" width="120" style="vertical-align: top">
    			28/01/2014
    		</td>
    		<td width="20" valign="top" aria-hidden="true">

    		</td>
    		<td class="descricaoMovimentacao" style="vertical-align: top; padding-bottom: 5px">




    					Juntada de documento



    			<br>
    			<span style="font-style: italic;">

    			</span>

    		</td>
    	</tr>






















    	<tr class="fundoEscuro containerMovimentacao" style="">
    		<td class="dataMovimentacao" width="120" style="vertical-align: top">
    			27/11/2013
    		</td>
    		<td width="20" valign="top" aria-hidden="true">

    		</td>
    		<td class="descricaoMovimentacao" style="vertical-align: top; padding-bottom: 5px">




    					Audiência de instrução e julgamento designada



    			<br>
    			<span style="font-style: italic;">
    				AUDIÊNCIA DE INSTRUÇÃO E JULGAMENTO DESIGNADA DATA DA AUDIENCIA: 04/02/2014

    HORA DA AUDIENCIA: 11:20 - Local: VARA ÚNICA DE TRÂNSITO DA COMARCA DE FORTALEZA
    			</span>

    		</td>
    	</tr>






















    	<tr class="fundoClaro containerMovimentacao" style="">
    		<td class="dataMovimentacao" width="120" style="vertical-align: top">
    			29/07/2013
    		</td>
    		<td width="20" valign="top" aria-hidden="true">

    		</td>
    		<td class="descricaoMovimentacao" style="vertical-align: top; padding-bottom: 5px">




    					Juntada de documento



    			<br>
    			<span style="font-style: italic;">
    				JUNTADA DE DOCUMENTO TIPO DE DOCUMENTO: DESPACHO - Local: VARA ÚNICA DE TRÂNSITO DA COMARCA DE FORTALEZA
    			</span>

    		</td>
    	</tr>






















    	<tr class="fundoEscuro containerMovimentacao" style="">
    		<td class="dataMovimentacao" width="120" style="vertical-align: top">
    			24/07/2013
    		</td>
    		<td width="20" valign="top" aria-hidden="true">

    		</td>
    		<td class="descricaoMovimentacao" style="vertical-align: top; padding-bottom: 5px">




    					Concluso ao juiz



    			<br>
    			<span style="font-style: italic;">
    				CONCLUSO AO JUIZ TIPO DE CONCLUSÃO: DESPACHO/DECISÃO - Local: VARA ÚNICA DE TRÂNSITO DA COMARCA DE FORTALEZA
    			</span>

    		</td>
    	</tr>






















    	<tr class="fundoClaro containerMovimentacao" style="">
    		<td class="dataMovimentacao" width="120" style="vertical-align: top">
    			24/07/2013
    		</td>
    		<td width="20" valign="top" aria-hidden="true">

    		</td>
    		<td class="descricaoMovimentacao" style="vertical-align: top; padding-bottom: 5px">




    					Juntada de documento



    			<br>
    			<span style="font-style: italic;">
    				JUNTADA DE DOCUMENTO TIPO DE DOCUMENTO: PARECER MP - Local: VARA ÚNICA DE TRÂNSITO DA COMARCA DE FORTALEZA
    			</span>

    		</td>
    	</tr>






















    	<tr class="fundoEscuro containerMovimentacao" style="">
    		<td class="dataMovimentacao" width="120" style="vertical-align: top">
    			24/07/2013
    		</td>
    		<td width="20" valign="top" aria-hidden="true">

    		</td>
    		<td class="descricaoMovimentacao" style="vertical-align: top; padding-bottom: 5px">




    					Recebidos os autos



    			<br>
    			<span style="font-style: italic;">
    				RECEBIDOS OS AUTOS DE QUEM: MP

    PROVENIENTE DE : CARGA/VISTA - Local: VARA ÚNICA DE TRÂNSITO DA COMARCA DE FORTALEZA
    			</span>

    		</td>
    	</tr>






















    	<tr class="fundoClaro containerMovimentacao" style="">
    		<td class="dataMovimentacao" width="120" style="vertical-align: top">
    			11/07/2013
    		</td>
    		<td width="20" valign="top" aria-hidden="true">

    		</td>
    		<td class="descricaoMovimentacao" style="vertical-align: top; padding-bottom: 5px">




    					Autos entregues com carga/vista ao ministério público



    			<br>
    			<span style="font-style: italic;">
    				AUTOS ENTREGUES COM CARGA/VISTA AO MINISTÉRIO PÚBLICO NOME DO DESTINATÁRIO: DRA. MARIA DO CARMO

    FUNCIONARIO: NEHYSE LIMA

    NO. DAS FOLHAS: 00

    DATA INICIAL DO PRAZO: 11/07/2013 - Local: VARA ÚNICA DE TRÂNSITO DA COMARCA DE FORTALEZA
    			</span>

    		</td>
    	</tr>






















    	<tr class="fundoEscuro containerMovimentacao" style="">
    		<td class="dataMovimentacao" width="120" style="vertical-align: top">
    			20/05/2013
    		</td>
    		<td width="20" valign="top" aria-hidden="true">

    		</td>
    		<td class="descricaoMovimentacao" style="vertical-align: top; padding-bottom: 5px">




    					Autos entregues com carga/vista ao ministério público



    			<br>
    			<span style="font-style: italic;">
    				VISTA P/ CIÊNCIA DO MP - Local: VARA ÚNICA DE TRÂNSITO DA COMARCA DE FORTALEZA
    			</span>

    		</td>
    	</tr>






















    	<tr class="fundoClaro containerMovimentacao" style="">
    		<td class="dataMovimentacao" width="120" style="vertical-align: top">
    			20/05/2013
    		</td>
    		<td width="20" valign="top" aria-hidden="true">

    		</td>
    		<td class="descricaoMovimentacao" style="vertical-align: top; padding-bottom: 5px">




    					Juntada de documento



    			<br>
    			<span style="font-style: italic;">
    				JUNTADA DE DOCUMENTO TIPO DE DOCUMENTO: DESPACHO - Local: VARA ÚNICA DE TRÂNSITO DA COMARCA DE FORTALEZA
    			</span>

    		</td>
    	</tr>






















    	<tr class="fundoEscuro containerMovimentacao" style="">
    		<td class="dataMovimentacao" width="120" style="vertical-align: top">
    			17/05/2013
    		</td>
    		<td width="20" valign="top" aria-hidden="true">

    		</td>
    		<td class="descricaoMovimentacao" style="vertical-align: top; padding-bottom: 5px">




    					Concluso ao juiz



    			<br>
    			<span style="font-style: italic;">
    				CONCLUSO AO JUIZ TIPO DE CONCLUSÃO: DESPACHO/DECISÃO - Local: VARA ÚNICA DE TRÂNSITO DA COMARCA DE FORTALEZA
    			</span>

    		</td>
    	</tr>






















    	<tr class="fundoClaro containerMovimentacao" style="">
    		<td class="dataMovimentacao" width="120" style="vertical-align: top">
    			17/05/2013
    		</td>
    		<td width="20" valign="top" aria-hidden="true">

    		</td>
    		<td class="descricaoMovimentacao" style="vertical-align: top; padding-bottom: 5px">




    					Juntada de documento



    			<br>
    			<span style="font-style: italic;">
    				JUNTADA DE DOCUMENTO TIPO DE DOCUMENTO: PARECER DEFENSOR PUBLICO - Local: VARA ÚNICA DE TRÂNSITO DA COMARCA DE FORTALEZA
    			</span>

    		</td>
    	</tr>






















    	<tr class="fundoEscuro containerMovimentacao" style="">
    		<td class="dataMovimentacao" width="120" style="vertical-align: top">
    			17/05/2013
    		</td>
    		<td width="20" valign="top" aria-hidden="true">

    		</td>
    		<td class="descricaoMovimentacao" style="vertical-align: top; padding-bottom: 5px">




    					Concluso ao juiz



    			<br>
    			<span style="font-style: italic;">
    				CONCLUSO AO JUIZ TIPO DE CONCLUSÃO: DESPACHO/DECISÃO - Local: VARA ÚNICA DE TRÂNSITO DA COMARCA DE FORTALEZA
    			</span>

    		</td>
    	</tr>






















    	<tr class="fundoClaro containerMovimentacao" style="">
    		<td class="dataMovimentacao" width="120" style="vertical-align: top">
    			17/05/2013
    		</td>
    		<td width="20" valign="top" aria-hidden="true">

    		</td>
    		<td class="descricaoMovimentacao" style="vertical-align: top; padding-bottom: 5px">




    					Juntada de documento



    			<br>
    			<span style="font-style: italic;">
    				JUNTADA DE DOCUMENTO TIPO DE DOCUMENTO: PARECER DEFENSOR PUBLICO - Local: VARA ÚNICA DE TRÂNSITO DA COMARCA DE FORTALEZA
    			</span>

    		</td>
    	</tr>






















    	<tr class="fundoEscuro containerMovimentacao" style="">
    		<td class="dataMovimentacao" width="120" style="vertical-align: top">
    			17/05/2013
    		</td>
    		<td width="20" valign="top" aria-hidden="true">

    		</td>
    		<td class="descricaoMovimentacao" style="vertical-align: top; padding-bottom: 5px">




    					Recebidos os autos



    			<br>
    			<span style="font-style: italic;">
    				RECEBIDOS OS AUTOS DE QUEM: DEFENSOR PUBLICO

    PROVENIENTE DE : CARGA/VISTA - Local: VARA ÚNICA DE TRÂNSITO DA COMARCA DE FORTALEZA
    			</span>

    		</td>
    	</tr>






















    	<tr class="fundoClaro containerMovimentacao" style="">
    		<td class="dataMovimentacao" width="120" style="vertical-align: top">
    			14/05/2013
    		</td>
    		<td width="20" valign="top" aria-hidden="true">

    		</td>
    		<td class="descricaoMovimentacao" style="vertical-align: top; padding-bottom: 5px">




    					Autos entregues com carga/vista ao defensor público



    			<br>
    			<span style="font-style: italic;">
    				AUTOS ENTREGUES COM CARGA/VISTA AO DEFENSOR PÚBLICO NOME DO DESTINATÁRIO: DR. ATHILA BEZERRA 

    FUNCIONARIO: NEHYSE LIMA

    NO. DAS FOLHAS: 00

    DATA INICIAL DO PRAZO: 14/05/2013

    DATA FINAL DO PRAZO: 19/05/2013 - Local: VARA ÚNICA DE TRÂNSITO DA COMARCA DE FORTALEZA
    			</span>

    		</td>
    	</tr>






















    	<tr class="fundoEscuro containerMovimentacao" style="">
    		<td class="dataMovimentacao" width="120" style="vertical-align: top">
    			28/08/2012
    		</td>
    		<td width="20" valign="top" aria-hidden="true">

    		</td>
    		<td class="descricaoMovimentacao" style="vertical-align: top; padding-bottom: 5px">




    					Juntada de documento



    			<br>
    			<span style="font-style: italic;">
    				JUNTADA DE DOCUMENTO TIPO DE DOCUMENTO: DESPACHO - Local: VARA ÚNICA DE TRÂNSITO DA COMARCA DE FORTALEZA
    			</span>

    		</td>
    	</tr>






















    	<tr class="fundoClaro containerMovimentacao" style="">
    		<td class="dataMovimentacao" width="120" style="vertical-align: top">
    			23/08/2012
    		</td>
    		<td width="20" valign="top" aria-hidden="true">

    		</td>
    		<td class="descricaoMovimentacao" style="vertical-align: top; padding-bottom: 5px">




    					Concluso ao juiz



    			<br>
    			<span style="font-style: italic;">
    				CONCLUSO AO JUIZ TIPO DE CONCLUSÃO: DESPACHO/DECISÃO COM RESPOSTA Á ACUSAÇÃO - Local: VARA ÚNICA DE TRÂNSITO DA COMARCA DE FORTALEZA
    			</span>

    		</td>
    	</tr>






















    	<tr class="fundoEscuro containerMovimentacao" style="">
    		<td class="dataMovimentacao" width="120" style="vertical-align: top">
    			23/08/2012
    		</td>
    		<td width="20" valign="top" aria-hidden="true">

    		</td>
    		<td class="descricaoMovimentacao" style="vertical-align: top; padding-bottom: 5px">




    					Recebidos os autos



    			<br>
    			<span style="font-style: italic;">
    				RECEBIDOS OS AUTOS DE QUEM: DEFENSOR PUBLICO

    PROVENIENTE DE : CARGA/VISTA - Local: VARA ÚNICA DE TRÂNSITO DA COMARCA DE FORTALEZA
    			</span>

    		</td>
    	</tr>






















    	<tr class="fundoClaro containerMovimentacao" style="">
    		<td class="dataMovimentacao" width="120" style="vertical-align: top">
    			21/08/2012
    		</td>
    		<td width="20" valign="top" aria-hidden="true">

    		</td>
    		<td class="descricaoMovimentacao" style="vertical-align: top; padding-bottom: 5px">




    					Autos entregues com carga/vista ao defensor público



    			<br>
    			<span style="font-style: italic;">
    				AUTOS ENTREGUES COM CARGA/VISTA AO DEFENSOR PÚBLICO NOME DO DESTINATÁRIO: Dr Lino

    FUNCIONARIO: alberto

    NO. DAS FOLHAS: 95

    DATA INICIAL DO PRAZO: 22/08/2012

    DATA FINAL DO PRAZO: 26/08/2012 - Local: VARA ÚNICA DE TRÂNSITO DA COMARCA DE FORTALEZA
    			</span>

    		</td>
    	</tr>






















    	<tr class="fundoEscuro containerMovimentacao" style="">
    		<td class="dataMovimentacao" width="120" style="vertical-align: top">
    			10/07/2012
    		</td>
    		<td width="20" valign="top" aria-hidden="true">

    		</td>
    		<td class="descricaoMovimentacao" style="vertical-align: top; padding-bottom: 5px">




    					Entrada de petição de acompanhamento



    			<br>
    			<span style="font-style: italic;">
    				ENTRADA DE PETIÇÃO DE ACOMPANHAMENTO Objeto Peticao :  - Local Entrada :SERVIÇO DE PORTARIA DOS FEITOS JUDICIAIS DA COMARCA DE FORTALEZA ( COMARCA DE FORTALEZA ) - Local: VARA ÚNICA DE TRÂNSITO DA COMARCA DE FORTALEZA
    			</span>

    		</td>
    	</tr>






















    	<tr class="fundoClaro containerMovimentacao" style="">
    		<td class="dataMovimentacao" width="120" style="vertical-align: top">
    			19/12/2011
    		</td>
    		<td width="20" valign="top" aria-hidden="true">

    		</td>
    		<td class="descricaoMovimentacao" style="vertical-align: top; padding-bottom: 5px">




    					Expedição de documento



    			<br>
    			<span style="font-style: italic;">
    				EXPEDIÇÃO DE DOCUMENTO TIPO DE DOCUMENTO: CARTA PRECATÓRIA ENVIAR - Local: VARA ÚNICA DE TRÂNSITO DA COMARCA DE FORTALEZA
    			</span>

    		</td>
    	</tr>






















    	<tr class="fundoEscuro containerMovimentacao" style="">
    		<td class="dataMovimentacao" width="120" style="vertical-align: top">
    			16/12/2011
    		</td>
    		<td width="20" valign="top" aria-hidden="true">

    		</td>
    		<td class="descricaoMovimentacao" style="vertical-align: top; padding-bottom: 5px">




    					Expedição de documento



    			<br>
    			<span style="font-style: italic;">
    				EXPEDIÇÃO DE DOCUMENTO TIPO DE DOCUMENTO: OFÍCIO SELAR EXPEDIENTES - Local: VARA ÚNICA DE TRÂNSITO DA COMARCA DE FORTALEZA
    			</span>

    		</td>
    	</tr>






















    	<tr class="fundoClaro containerMovimentacao" style="">
    		<td class="dataMovimentacao" width="120" style="vertical-align: top">
    			28/11/2011
    		</td>
    		<td width="20" valign="top" aria-hidden="true">

    		</td>
    		<td class="descricaoMovimentacao" style="vertical-align: top; padding-bottom: 5px">




    					Expedição de documento



    			<br>
    			<span style="font-style: italic;">
    				EXPEDIÇÃO DE DOCUMENTO TIPO DE DOCUMENTO: MANDADO DE CITAÇÃO - Local: VARA ÚNICA DE TRÂNSITO DA COMARCA DE FORTALEZA
    			</span>

    		</td>
    	</tr>






















    	<tr class="fundoEscuro containerMovimentacao" style="">
    		<td class="dataMovimentacao" width="120" style="vertical-align: top">
    			16/11/2011
    		</td>
    		<td width="20" valign="top" aria-hidden="true">

    		</td>
    		<td class="descricaoMovimentacao" style="vertical-align: top; padding-bottom: 5px">




    					Autuação



    			<br>
    			<span style="font-style: italic;">
    				AUTUAÇÃO DOCUMENTO ATUAL: DENÚNCIA - Local: VARA ÚNICA DE TRÂNSITO DA COMARCA DE FORTALEZA
    			</span>

    		</td>
    	</tr>






















    	<tr class="fundoClaro containerMovimentacao" style="">
    		<td class="dataMovimentacao" width="120" style="vertical-align: top">
    			31/10/2011
    		</td>
    		<td width="20" valign="top" aria-hidden="true">

    		</td>
    		<td class="descricaoMovimentacao" style="vertical-align: top; padding-bottom: 5px">




    					Concluso ao juiz



    			<br>
    			<span style="font-style: italic;">
    				CONCLUSO AO JUIZ TIPO DE CONCLUSÃO: DESPACHO/DECISÃO COM DENÚNCIA - Local: VARA ÚNICA DE TRÂNSITO DA COMARCA DE FORTALEZA
    			</span>

    		</td>
    	</tr>






















    	<tr class="fundoEscuro containerMovimentacao" style="">
    		<td class="dataMovimentacao" width="120" style="vertical-align: top">
    			31/10/2011
    		</td>
    		<td width="20" valign="top" aria-hidden="true">

    		</td>
    		<td class="descricaoMovimentacao" style="vertical-align: top; padding-bottom: 5px">




    					Recebidos os autos



    			<br>
    			<span style="font-style: italic;">
    				RECEBIDOS OS AUTOS DE QUEM: MP

    PROVENIENTE DE : CARGA/VISTA - Local: VARA ÚNICA DE TRÂNSITO DA COMARCA DE FORTALEZA
    			</span>

    		</td>
    	</tr>






















    	<tr class="fundoClaro containerMovimentacao" style="">
    		<td class="dataMovimentacao" width="120" style="vertical-align: top">
    			31/10/2011
    		</td>
    		<td width="20" valign="top" aria-hidden="true">

    		</td>
    		<td class="descricaoMovimentacao" style="vertical-align: top; padding-bottom: 5px">




    					Recebida a denúncia



    			<br>
    			<span style="font-style: italic;">
    				RECEBIDA A DENÚNCIA Inquerito transformado em Processo - Local: VARA ÚNICA DE TRÂNSITO DA COMARCA DE FORTALEZA
    			</span>

    		</td>
    	</tr>






















    	<tr class="fundoEscuro containerMovimentacao" style="">
    		<td class="dataMovimentacao" width="120" style="vertical-align: top">
    			24/10/2011
    		</td>
    		<td width="20" valign="top" aria-hidden="true">

    		</td>
    		<td class="descricaoMovimentacao" style="vertical-align: top; padding-bottom: 5px">




    					Autos entregues com carga/vista ao ministério público



    			<br>
    			<span style="font-style: italic;">
    				AUTOS ENTREGUES COM CARGA/VISTA AO MINISTÉRIO PÚBLICO NOME DO DESTINATÁRIO: DR. BRUNO JORGE

    FUNCIONARIO: MARTA ESDRAS

    NO. DAS FOLHAS: 1

    DATA INICIAL DO PRAZO: 24/10/2011 - Local: VARA ÚNICA DE TRÂNSITO DA COMARCA DE FORTALEZA
    			</span>

    		</td>
    	</tr>






















    	<tr class="fundoClaro containerMovimentacao" style="">
    		<td class="dataMovimentacao" width="120" style="vertical-align: top">
    			23/09/2011
    		</td>
    		<td width="20" valign="top" aria-hidden="true">

    		</td>
    		<td class="descricaoMovimentacao" style="vertical-align: top; padding-bottom: 5px">




    					Concluso ao juiz



    			<br>
    			<span style="font-style: italic;">
    				CONCLUSO AO JUIZ TIPO DE CONCLUSÃO: DESPACHO/DECISÃO - Local: VARA ÚNICA DE TRÂNSITO DA COMARCA DE FORTALEZA
    			</span>

    		</td>
    	</tr>






















    	<tr class="fundoEscuro containerMovimentacao" style="">
    		<td class="dataMovimentacao" width="120" style="vertical-align: top">
    			22/06/2011
    		</td>
    		<td width="20" valign="top" aria-hidden="true">

    		</td>
    		<td class="descricaoMovimentacao" style="vertical-align: top; padding-bottom: 5px">




    					Remessa dos autos



    			<br>
    			<span style="font-style: italic;">
    				REMESSA DOS AUTOS DESTINO: À DELEGACIA 8º DP - Local: VARA ÚNICA DE TRÂNSITO DA COMARCA DE FORTALEZA
    			</span>

    		</td>
    	</tr>






















    	<tr class="fundoClaro containerMovimentacao" style="">
    		<td class="dataMovimentacao" width="120" style="vertical-align: top">
    			23/05/2011
    		</td>
    		<td width="20" valign="top" aria-hidden="true">

    		</td>
    		<td class="descricaoMovimentacao" style="vertical-align: top; padding-bottom: 5px">




    					Concluso ao juiz



    			<br>
    			<span style="font-style: italic;">
    				CONCLUSO AO JUIZ TIPO DE CONCLUSÃO: DESPACHO/DECISÃO DILIGÊNCIAS - Local: VARA ÚNICA DE TRÂNSITO DA COMARCA DE FORTALEZA
    			</span>

    		</td>
    	</tr>






















    	<tr class="fundoEscuro containerMovimentacao" style="">
    		<td class="dataMovimentacao" width="120" style="vertical-align: top">
    			21/03/2011
    		</td>
    		<td width="20" valign="top" aria-hidden="true">

    		</td>
    		<td class="descricaoMovimentacao" style="vertical-align: top; padding-bottom: 5px">




    					Concluso ao juiz



    			<br>
    			<span style="font-style: italic;">
    				CONCLUSO AO JUIZ TIPO DE CONCLUSÃO: DESPACHO/DECISÃO - Local: VARA ÚNICA DE TRÂNSITO DA COMARCA DE FORTALEZA
    			</span>

    		</td>
    	</tr>






















    	<tr class="fundoClaro containerMovimentacao" style="">
    		<td class="dataMovimentacao" width="120" style="vertical-align: top">
    			16/03/2011
    		</td>
    		<td width="20" valign="top" aria-hidden="true">

    		</td>
    		<td class="descricaoMovimentacao" style="vertical-align: top; padding-bottom: 5px">




    					Entrada de petição de acompanhamento



    			<br>
    			<span style="font-style: italic;">
    				ENTRADA DE PETIÇÃO DE ACOMPANHAMENTO Objeto Peticao :  - Local Entrada :SERVIÇO DE PORTARIA DOS FEITOS JUDICIAIS DA COMARCA DE FORTALEZA ( COMARCA DE FORTALEZA ) - Local: VARA ÚNICA DE TRÂNSITO DA COMARCA DE FORTALEZA
    			</span>

    		</td>
    	</tr>






















    	<tr class="fundoEscuro containerMovimentacao" style="">
    		<td class="dataMovimentacao" width="120" style="vertical-align: top">
    			28/02/2011
    		</td>
    		<td width="20" valign="top" aria-hidden="true">

    		</td>
    		<td class="descricaoMovimentacao" style="vertical-align: top; padding-bottom: 5px">




    					Concluso ao juiz



    			<br>
    			<span style="font-style: italic;">
    				CONCLUSO AO JUIZ TIPO DE CONCLUSÃO: DESPACHO/DECISÃO - Local: VARA ÚNICA DE TRÂNSITO DA COMARCA DE FORTALEZA
    			</span>

    		</td>
    	</tr>






















    	<tr class="fundoClaro containerMovimentacao" style="">
    		<td class="dataMovimentacao" width="120" style="vertical-align: top">
    			18/06/2010
    		</td>
    		<td width="20" valign="top" aria-hidden="true">

    		</td>
    		<td class="descricaoMovimentacao" style="vertical-align: top; padding-bottom: 5px">




    					Remessa dos autos



    			<br>
    			<span style="font-style: italic;">
    				REMESSA DOS AUTOS DESTINO: À DELEGACIA 8º DP - Local: VARA ÚNICA DE TRÂNSITO DA COMARCA DE FORTALEZA
    			</span>

    		</td>
    	</tr>






















    	<tr class="fundoEscuro containerMovimentacao" style="">
    		<td class="dataMovimentacao" width="120" style="vertical-align: top">
    			07/06/2010
    		</td>
    		<td width="20" valign="top" aria-hidden="true">

    		</td>
    		<td class="descricaoMovimentacao" style="vertical-align: top; padding-bottom: 5px">




    					Expedição de documento



    			<br>
    			<span style="font-style: italic;">
    				EXPEDIÇÃO DE DOCUMENTO TIPO DE DOCUMENTO: OFÍCIO - Local: VARA ÚNICA DE TRÂNSITO DA COMARCA DE FORTALEZA
    			</span>

    		</td>
    	</tr>






















    	<tr class="fundoClaro containerMovimentacao" style="">
    		<td class="dataMovimentacao" width="120" style="vertical-align: top">
    			27/05/2010
    		</td>
    		<td width="20" valign="top" aria-hidden="true">

    		</td>
    		<td class="descricaoMovimentacao" style="vertical-align: top; padding-bottom: 5px">




    					Concluso ao juiz



    			<br>
    			<span style="font-style: italic;">
    				CONCLUSO AO JUIZ TIPO DE CONCLUSÃO: DESPACHO/DECISÃO - Local: VARA ÚNICA DE TRÂNSITO DA COMARCA DE FORTALEZA
    			</span>

    		</td>
    	</tr>






















    	<tr class="fundoEscuro containerMovimentacao" style="">
    		<td class="dataMovimentacao" width="120" style="vertical-align: top">
    			27/05/2010
    		</td>
    		<td width="20" valign="top" aria-hidden="true">

    		</td>
    		<td class="descricaoMovimentacao" style="vertical-align: top; padding-bottom: 5px">




    					Recebidos os autos



    			<br>
    			<span style="font-style: italic;">
    				RECEBIDOS OS AUTOS DE QUEM: MP

    PROVENIENTE DE : CARGA/VISTA - Local: VARA ÚNICA DE TRÂNSITO DA COMARCA DE FORTALEZA
    			</span>

    		</td>
    	</tr>






















    	<tr class="fundoClaro containerMovimentacao" style="">
    		<td class="dataMovimentacao" width="120" style="vertical-align: top">
    			27/05/2010
    		</td>
    		<td width="20" valign="top" aria-hidden="true">

    		</td>
    		<td class="descricaoMovimentacao" style="vertical-align: top; padding-bottom: 5px">




    					Recebidos os autos



    			<br>
    			<span style="font-style: italic;">
    				RECEBIDOS OS AUTOS DE QUEM: MP

    PROVENIENTE DE : CARGA/VISTA - Local: VARA ÚNICA DE TRÂNSITO DA COMARCA DE FORTALEZA
    			</span>

    		</td>
    	</tr>






















    	<tr class="fundoEscuro containerMovimentacao" style="">
    		<td class="dataMovimentacao" width="120" style="vertical-align: top">
    			27/05/2010
    		</td>
    		<td width="20" valign="top" aria-hidden="true">

    		</td>
    		<td class="descricaoMovimentacao" style="vertical-align: top; padding-bottom: 5px">




    					Recebidos os autos



    			<br>
    			<span style="font-style: italic;">
    				RECEBIDOS OS AUTOS DE QUEM: MP

    PROVENIENTE DE : CARGA/VISTA - Local: VARA ÚNICA DE TRÂNSITO DA COMARCA DE FORTALEZA
    			</span>

    		</td>
    	</tr>






















    	<tr class="fundoClaro containerMovimentacao" style="">
    		<td class="dataMovimentacao" width="120" style="vertical-align: top">
    			17/05/2010
    		</td>
    		<td width="20" valign="top" aria-hidden="true">

    		</td>
    		<td class="descricaoMovimentacao" style="vertical-align: top; padding-bottom: 5px">




    					Autos entregues com carga/vista ao ministério público



    			<br>
    			<span style="font-style: italic;">
    				AUTOS ENTREGUES COM CARGA/VISTA AO MINISTÉRIO PÚBLICO NOME DO DESTINATÁRIO: DR. BRUNO JORGE

    FUNCIONARIO: MARTA ESDRAS

    NO. DAS FOLHAS: 2

    DATA INICIAL DO PRAZO: 17/05/2010 - Local: VARA ÚNICA DE TRÂNSITO DA COMARCA DE FORTALEZA
    			</span>

    		</td>
    	</tr>






















    	<tr class="fundoEscuro containerMovimentacao" style="">
    		<td class="dataMovimentacao" width="120" style="vertical-align: top">
    			17/03/2009
    		</td>
    		<td width="20" valign="top" aria-hidden="true">

    		</td>
    		<td class="descricaoMovimentacao" style="vertical-align: top; padding-bottom: 5px">




    					Redistribuição por encaminhamento



    			<br>
    			<span style="font-style: italic;">
    				REDISTRIBUIÇÃO POR ENCAMINHAMENTO Distribuído automaticamente conforme provimento nº04/2009 circulado no Diário da Justiça em 22/01/2009. Motivo: TRANSFORMAÇÃO 1ª VARA DO TRÂNSITO EM VARA ÚNICA DO TRÂNSITO - Local: VARA ÚNICA DE TRÂNSITO DA COMARCA DE FORTALEZA
    			</span>

    		</td>
    	</tr>






















    	<tr class="fundoClaro containerMovimentacao" style="">
    		<td class="dataMovimentacao" width="120" style="vertical-align: top">
    			10/03/2009
    		</td>
    		<td width="20" valign="top" aria-hidden="true">

    		</td>
    		<td class="descricaoMovimentacao" style="vertical-align: top; padding-bottom: 5px">




    					Entrada de petição de acompanhamento



    			<br>
    			<span style="font-style: italic;">
    				ENTRADA DE PETIÇÃO DE ACOMPANHAMENTO Objeto Peticao :  - Local Entrada :SERVIÇO DE PORTARIA DOS FEITOS JUDICIAIS DA COMARCA DE FORTALEZA ( COMARCA DE FORTALEZA ) - Local: 1ª VARA DE TRANSITO DA COMARCA DE FORTALEZA
    			</span>

    		</td>
    	</tr>






















    	<tr class="fundoEscuro containerMovimentacao" style="">
    		<td class="dataMovimentacao" width="120" style="vertical-align: top">
    			27/02/2009
    		</td>
    		<td width="20" valign="top" aria-hidden="true">

    		</td>
    		<td class="descricaoMovimentacao" style="vertical-align: top; padding-bottom: 5px">




    					Entrada de petição de acompanhamento



    			<br>
    			<span style="font-style: italic;">
    				ENTRADA DE PETIÇÃO DE ACOMPANHAMENTO Objeto Peticao :  - Local Entrada :SERVIÇO DE PORTARIA DOS FEITOS JUDICIAIS DA COMARCA DE FORTALEZA ( COMARCA DE FORTALEZA ) - Local: 1ª VARA DE TRANSITO DA COMARCA DE FORTALEZA
    			</span>

    		</td>
    	</tr>






















    	<tr class="fundoClaro containerMovimentacao" style="">
    		<td class="dataMovimentacao" width="120" style="vertical-align: top">
    			20/02/2009
    		</td>
    		<td width="20" valign="top" aria-hidden="true">

    		</td>
    		<td class="descricaoMovimentacao" style="vertical-align: top; padding-bottom: 5px">




    					Remessa dos autos



    			<br>
    			<span style="font-style: italic;">
    				REMESSA DOS AUTOS DESTINO: 8º DP. p/ diligências - Local: 1ª VARA DE TRANSITO DA COMARCA DE FORTALEZA
    			</span>

    		</td>
    	</tr>






















    	<tr class="fundoEscuro containerMovimentacao" style="">
    		<td class="dataMovimentacao" width="120" style="vertical-align: top">
    			09/02/2009
    		</td>
    		<td width="20" valign="top" aria-hidden="true">

    		</td>
    		<td class="descricaoMovimentacao" style="vertical-align: top; padding-bottom: 5px">




    					Concluso ao juiz



    			<br>
    			<span style="font-style: italic;">
    				CONCLUSO AO JUIZ TIPO DE CONCLUSÃO: DESPACHO/DECISÃO - Local: 1ª VARA DE TRANSITO DA COMARCA DE FORTALEZA
    			</span>

    		</td>
    	</tr>






















    	<tr class="fundoClaro containerMovimentacao" style="">
    		<td class="dataMovimentacao" width="120" style="vertical-align: top">
    			19/01/2009
    		</td>
    		<td width="20" valign="top" aria-hidden="true">

    		</td>
    		<td class="descricaoMovimentacao" style="vertical-align: top; padding-bottom: 5px">




    					Autos entregues com carga/vista ao ministério público



    			<br>
    			<span style="font-style: italic;">
    				AUTOS ENTREGUES COM CARGA/VISTA AO MINISTÉRIO PÚBLICO NOME DO DESTINATÁRIO: DR. BRUNO JORGE

    FUNCIONARIO: MARTA ESDRAS

    NO. DAS FOLHAS: 31

    DATA INICIAL DO PRAZO: 19/01/2009 - Local: 1ª VARA DE TRANSITO DA COMARCA DE FORTALEZA
    			</span>

    		</td>
    	</tr>






















    	<tr class="fundoEscuro containerMovimentacao" style="">
    		<td class="dataMovimentacao" width="120" style="vertical-align: top">
    			16/01/2009
    		</td>
    		<td width="20" valign="top" aria-hidden="true">

    		</td>
    		<td class="descricaoMovimentacao" style="vertical-align: top; padding-bottom: 5px">




    					Concluso ao juiz



    			<br>
    			<span style="font-style: italic;">
    				CONCLUSO AO JUIZ TIPO DE CONCLUSÃO: DESPACHO/DECISÃO vindos do 8º DP - Local: 1ª VARA DE TRANSITO DA COMARCA DE FORTALEZA
    			</span>

    		</td>
    	</tr>






















    	<tr class="fundoClaro containerMovimentacao" style="">
    		<td class="dataMovimentacao" width="120" style="vertical-align: top">
    			27/11/2008
    		</td>
    		<td width="20" valign="top" aria-hidden="true">

    		</td>
    		<td class="descricaoMovimentacao" style="vertical-align: top; padding-bottom: 5px">




    					Autos entregues com carga/vista ao ministério público



    			<br>
    			<span style="font-style: italic;">
    				AUTOS ENTREGUES COM CARGA/VISTA AO MINISTÉRIO PÚBLICO NOME DO DESTINATÁRIO: DR. BRUNO JORGE

    FUNCIONARIO: MARTA ESDRAS

    NO. DAS FOLHAS: 18

    DATA INICIAL DO PRAZO: 27/11/2008 - Local: 1ª VARA DE TRANSITO DA COMARCA DE FORTALEZA
    			</span>

    		</td>
    	</tr>






















    	<tr class="fundoEscuro containerMovimentacao" style="">
    		<td class="dataMovimentacao" width="120" style="vertical-align: top">
    			19/08/2008
    		</td>
    		<td width="20" valign="top" aria-hidden="true">

    		</td>
    		<td class="descricaoMovimentacao" style="vertical-align: top; padding-bottom: 5px">




    					Remessa à delegacia de origem



    			<br>
    			<span style="font-style: italic;">
    				REMESSA À DELEGACIA DE ORIGEM DELEGACIA: 8° DP - Local: CENTRAL DE INQUERITOS
    			</span>

    		</td>
    	</tr>






















    	<tr class="fundoClaro containerMovimentacao" style="">
    		<td class="dataMovimentacao" width="120" style="vertical-align: top">
    			14/07/2008
    		</td>
    		<td width="20" valign="top" aria-hidden="true">

    		</td>
    		<td class="descricaoMovimentacao" style="vertical-align: top; padding-bottom: 5px">




    					Entregue ao promotor de justiça



    			<br>
    			<span style="font-style: italic;">
    				ENTREGUE AO PROMOTOR DE JUSTIÇA PROMOTOR: DRA. MORGANA - Local: CENTRAL DE INQUERITOS
    			</span>

    		</td>
    	</tr>






















    	<tr class="fundoEscuro containerMovimentacao" style="">
    		<td class="dataMovimentacao" width="120" style="vertical-align: top">
    			11/07/2008
    		</td>
    		<td width="20" valign="top" aria-hidden="true">

    		</td>
    		<td class="descricaoMovimentacao" style="vertical-align: top; padding-bottom: 5px">




    					Distribuição automática



    			<br>
    			<span style="font-style: italic;">
    				DISTRIBUIÇÃO AUTOMÁTICA DISTRIBUIÇÃO AUTOMÁTICA  Motivo : EQÜIDADE.  -  - Local: SERVIÇO DE DISTRIBUIÇAO DOS FEITOS JUDICIAIS DA COMARCA DE FORTALEZA
    			</span>

    		</td>
    	</tr>






















    	<tr class="fundoClaro containerMovimentacao" style="">
    		<td class="dataMovimentacao" width="120" style="vertical-align: top">
    			11/07/2008
    		</td>
    		<td width="20" valign="top" aria-hidden="true">

    		</td>
    		<td class="descricaoMovimentacao" style="vertical-align: top; padding-bottom: 5px">




    					Permitir distribuição



    			<br>
    			<span style="font-style: italic;">
    				PERMITIR DISTRIBUIÇÃO - Local: SERVIÇO DE DISTRIBUIÇAO DOS FEITOS JUDICIAIS DA COMARCA DE FORTALEZA
    			</span>

    		</td>
    	</tr>






















    	<tr class="fundoEscuro containerMovimentacao" style="">
    		<td class="dataMovimentacao" width="120" style="vertical-align: top">
    			11/07/2008
    		</td>
    		<td width="20" valign="top" aria-hidden="true">

    		</td>
    		<td class="descricaoMovimentacao" style="vertical-align: top; padding-bottom: 5px">




    					Em classificação



    			<br>
    			<span style="font-style: italic;">
    				EM CLASSIFICAÇÃO - Local: SERVIÇO DE DISTRIBUIÇAO DOS FEITOS JUDICIAIS DA COMARCA DE FORTALEZA
    			</span>

    		</td>
    	</tr>






















    	<tr class="fundoClaro containerMovimentacao" style="">
    		<td class="dataMovimentacao" width="120" style="vertical-align: top">
    			10/07/2008
    		</td>
    		<td width="20" valign="top" aria-hidden="true">

    		</td>
    		<td class="descricaoMovimentacao" style="vertical-align: top; padding-bottom: 5px">




    					Protocolado



    			<br>
    			<span style="font-style: italic;">
    				PROTOCOLADO - Local: SERVIÇO DE PORTARIA DOS FEITOS JUDICIAIS DA COMARCA DE FORTALEZA
    			</span>

    		</td>
    	</tr>




    			</tbody>




    </table>

    	<div id="divLinksTituloBlocoMovimentacoes" style="text-align:right">










    <input id="mensagemNaoExibidamovimentacoes" type="hidden" value="">

        <input id="linkNaoExibidomovimentacoes" type="hidden" value="<span id=&quot;setasDireitamovimentacoes&quot; class=&quot;setasDireita&quot;><i class=&quot;unj-link-collapse__icon glyph glyph-chevron-up&quot;></i></span>Recolher">

    <span id="mensagensExibindomovimentacoes" class="mensagemExibindo">

    </span> &nbsp;

        <a id="linkmovimentacoes" href="javascript:" class="linkNaoSelecionado unj-link-collapse">
            <span id="setasDireitamovimentacoes" class="setasDireita">
                <i class="unj-link-collapse__icon glyph glyph-chevron-down"></i>
            </span>
            Mais
        </a>

    <script>
    	$(function() {
    		var controlarLink = function() {
    			var $linkNaoExibido = $('input#linkNaoExibidomovimentacoes');
    			var conteudoLinkNaoApresentado = $linkNaoExibido.val();
    			var $link = $('a#linkmovimentacoes');

    			$linkNaoExibido.val($link.html());
    			$link.html(conteudoLinkNaoApresentado);
    		};

    		var controlarMensagem = function() {
    			var $mensagemNaoExibida = $('input#mensagemNaoExibidamovimentacoes');
    			var $spanMensagem = $('span#mensagensExibindomovimentacoes');
    			var mensagemExibida = $spanMensagem.html();
    			var mensagemNaoExibida = $mensagemNaoExibida.val();

    			$spanMensagem.html(mensagemNaoExibida);
    			$mensagemNaoExibida.val(mensagemExibida);
    		};

    		var controlarMensagemLink = function() {
    			controlarMensagem();
    			controlarLink();
    		};

    		var esconderElementosExtrasMostrarDefault = function() {
    			$('#tabelaTodasMovimentacoes').hide();
    			$('#tabelaUltimasMovimentacoes').show();
    		};

    		var mostrarElementosExtrasEsconderDefault = function() {
    			$('#tabelaUltimasMovimentacoes').hide();
    			$('#tabelaTodasMovimentacoes').show();
    		};

    		var initPagina = function() {
                var setasDireita = '<span id="setasDireitamovimentacoes" class="setasDireita"><i class="unj-link-collapse__icon glyph glyph-chevron-up"></i></span>';
    			var $linkEscondido = $('input#linkNaoExibidomovimentacoes');
    			$linkEscondido.val(setasDireita+$linkEscondido.val());
    		};

    		var bindLink = function() {
    			var $link = $('a#linkmovimentacoes');
    			$link.funcToggle('click', mostrarElementosExtrasEsconderDefault, esconderElementosExtrasMostrarDefault);
    			$link.bind('click', controlarMensagemLink);
    		};

    		initPagina();
    		bindLink();
    		esconderElementosExtrasMostrarDefault();
    	});
    </script>

    	</div>







































    <div style="padding-top: 10px;">




    			<h2 class="subtitle tituloDoBloco">Petições diversas</h2>


    </div>

    <!-- Tabela de petições diversas -->
    <table style="margin-left:15px; margin-top:1px;" align="center" width="98%" border="0" cellspacing="0" cellpadding="1">


    			<thead>
    			    <tr class="label">
    			      <th width="140" style="text-align:left">Data</th>
    			      <th width="*">Tipo</th>
    			    </tr>
    			    <tr class="fundoEscuro" height="2" aria-hidden="true">
    					<td></td>
    					<td></td>
    				</tr>
    			</thead>
    			<tbody>


    						<tr class="fundoClaro"> 
    							<td width="140" style="text-align:left">
    								06/10/2014
    							</td>
    							<td width="*">
    								Retorno de Carta Precatória <br>
    								Acompanha mídia original(CD).
    							</td>
    						</tr>



    						<tr class="fundoEscuro"> 
    							<td width="140" style="text-align:left">
    								15/10/2014
    							</td>
    							<td width="*">
    								Memoriais <br>

    							</td>
    						</tr>



    						<tr class="fundoClaro"> 
    							<td width="140" style="text-align:left">
    								03/03/2016
    							</td>
    							<td width="*">
    								Memoriais <br>

    							</td>
    						</tr>



    						<tr class="fundoEscuro"> 
    							<td width="140" style="text-align:left">
    								13/04/2016
    							</td>
    							<td width="*">
    								RECURSO DE APELAÇÃO <br>

    							</td>
    						</tr>



    						<tr class="fundoClaro"> 
    							<td width="140" style="text-align:left">
    								13/05/2016
    							</td>
    							<td width="*">
    								Contrarrazões Recursais <br>

    							</td>
    						</tr>



    						<tr class="fundoEscuro"> 
    							<td width="140" style="text-align:left">
    								08/08/2016
    							</td>
    							<td width="*">
    								RECURSO DE APELAÇÃO <br>

    							</td>
    						</tr>



    						<tr class="fundoClaro"> 
    							<td width="140" style="text-align:left">
    								17/08/2016
    							</td>
    							<td width="*">
    								Pedido de Juntada de Documento <br>

    							</td>
    						</tr>



    						<tr class="fundoEscuro"> 
    							<td width="140" style="text-align:left">
    								16/08/2022
    							</td>
    							<td width="*">
    								Ofício <br>

    							</td>
    						</tr>


    			</tbody>



    </table>
    <!--  Tabela de petições diversas -->




























    <script type="text/javascript">
    	(function($) {
    		$(function(){
    			var captcha = $.saj.getUrlParameter('uuidCaptcha');
    			if(!captcha){
    				return;
    			}
    			$('.incidente a').each(function(){
    				var $incidente = $(this);
    				var url = $incidente.attr('href');
    				$incidente.attr('href', url+'&uuidCaptcha='+captcha);
    			});
    		})
    	})(jQuery);
    </script>











    <div style="padding-top: 10px;">




    			<h2 class="subtitle tituloDoBloco">Incidentes, ações incidentais, recursos e execuções de sentenças</h2>


    </div>

    <table style="margin-left:15px; margin-top:1px;" align="center" width="98%" border="0" cellspacing="0" cellpadding="1">


    	    <tbody><tr class="label">
    	    	<th width="140">
    				Recebido em
    			</th>
    			<th width="*" class="label">
    				Classe
    			</th>
    	    </tr>
    	    <tr class="fundoEscuro" height="2" aria-hidden="true">
    			<td></td><td></td>
    		</tr>



    			<tr class="fundoClaro">
    			  <td width="140" style="text-align:left">
    			    21/03/2016
    			  </td>
    			<td width="*">


    						<a class="incidente" href="/cpopg/show.do?localPesquisa.cdLocal=1&amp;processo.codigo=01Z081I9T0001&amp;processo.foro=1" target="_top">
    							Embargos de Declaração Criminal

    								 - 00001


    						</a>



    			</td>
    		</tr>        




    </tbody></table>
    <!--  Incidentes -->





































    <script type="text/javascript">
        (function ($) {
            $(function () {
                var captcha = $.saj.getUrlParameter('uuidCaptcha');

                if(!captcha){
                    return;
                }
                $.each($('.processoApensado'), function (i, value) {
                    var $link = $(value);
                    $link.attr('href', $link.attr('href') + '&uuidCaptcha=' + captcha);
                })

            })
        })(jQuery);
    </script>









    <div style="padding-top: 10px;">




    			<h2 class="subtitle tituloDoBloco">Apensos, Entranhados e Unificados</h2>


    </div>






            <table style="margin-left:15px; margin-top:1px;" align="center" width="98%" border="0" cellspacing="0" cellpadding="1">
                <thead>
    	            <tr class="label">
    	                <th align="left" width="15%">Número</th>
    	                <th align="left" width="20%">Classe</th>
    	                <th align="left" width="10%">Apensamento</th>
    	                <th align="left" width="50%">Motivo</th>
    	            </tr>
    	            <tr class="fundoEscuro" height="2" aria-hidden="true">
    	                <td></td>
    	                <td></td>
    	                <td></td>
    	                <td></td>
    	            </tr>
                </thead>
                <tbody id="dadosApenso">




    	                    <tr id="" class="fundoClaro">



    	                                <td width="15%">
    	                                    <a class="processoApensado" href="/cpopg/show.do?processo.codigo=01Z081I9T0001&amp;processo.foro=1&amp;referencia.codigo=01Z081I9T0000&amp;referencia.foro=1">
    	                                        0070337-91.2008.8.06.0001
    	                                    </a>
    	                                    &nbsp;(01)
    	                                </td>



    	                        <td width="20%">Embargos de Declaração Criminal</td>
    	                        <td width="10%">22/03/2016</td>
    	                        <td width="50%"></td>
    	                    </tr>


                </tbody>
            </table>























    <div style="padding-top: 10px;">




    			<h2 class="subtitle tituloDoBloco">Audiências</h2>


    </div>
























    <a name="audienciasPlaceHolder"></a>
    <table style="margin-left:15px; margin-top:1px;" align="center" width="98%" border="0" cellspacing="0" cellpadding="1">


                <tbody><tr class="label">
                    <th align="left" valign="top" width="140">Data</th>
                    <th align="left" valign="top" width="*">Audiência</th>
                    <th align="left" valign="top" width="100">Situação</th>
                    <th align="left" valign="top" width="100">Qt. Pessoas</th>
                </tr>
                <tr class="fundoEscuro" height="2" aria-hidden="true">
                    <td colspan="4"></td>
                </tr>

                    <tr class="fundoClaro">
                        <td valign="top" align="left" width="140">
                            04/02/2014
                        </td>



                                <td valign="top" align="left" width="*">
                                    Instrução e Julgamento
                                </td>



                        <td align="left" valign="top" width="100">
                            Realizada
                        </td>
                        <td align="left" valign="top" width="100">
                            0
                        </td>
                    </tr>




    </tbody></table>






































    <div style="padding-top: 10px;">




    			<h2 class="subtitle tituloDoBloco">Histórico de classes</h2>


    </div>

    <table style="margin-left:15px; margin-top:1px;" align="center" width="98%" border="0" cellspacing="0" cellpadding="1">
    	<thead>
    	    <tr class="label">
    	        <th align="left" valign="top" width="150">Data</th>
    	        <th align="left" valign="top" width="120">Tipo</th>
    	        <th align="left" valign="top" width="300">Classe</th>
    	        <th align="left" valign="top" width="120">Área</th>
    	        <th align="left" valign="top" width="*">Motivo</th>
    	    </tr>
    	    <tr class="fundoEscuro" height="2" aria-hidden="true">
    	        <td></td>
    	        <td></td>
    	        <td></td>
    	        <td></td>
    	        <td></td>
    	    </tr>
        </thead>


        	<tbody>
    	        <tr class="fundoClaro">
    	            <td valign="top" align="left" width="150">
    	                30/01/2014
    	            </td>
    	            <td align="left" valign="top" width="120">
    	                Evolução
    	            </td>
    	            <td align="left" valign="top" width="300">
    	                Ação Penal - Procedimento Ordinário
    	            </td>
    	            <td align="left" valign="top" width="120">
    	                Criminal
    	            </td>
    	            <td align="left" valign="top" width="*">
    	                -
    	            </td>
    	        </tr>
            </tbody>

        	<tbody>
    	        <tr class="fundoEscuro">
    	            <td valign="top" align="left" width="150">
    	                11/12/2013
    	            </td>
    	            <td align="left" valign="top" width="120">
    	                Inicial
    	            </td>
    	            <td align="left" valign="top" width="300">
    	                Inquérito Policial
    	            </td>
    	            <td align="left" valign="top" width="120">
    	                Criminal
    	            </td>
    	            <td align="left" valign="top" width="*">
    	                -
    	            </td>
    	        </tr>
            </tbody>

    </table>





























    <form id="popupCdas" style="display: none;">
    	<!--  dados da lista (CDAs) -->
    	<div style="height:210px; overflow: auto;">
    		<table id="tableCdasPrincipais" style="margin-left:10px; margin-top:1px; width: 98%;">
    			<thead>
    				<tr class="fundoClaro">
    					<th style="text-align:left;">Número CDA</th>
    					<th style="text-align:left;">Valor</th>
    					<th style="text-align:left;">Dt. CDA</th>
    					<th style="text-align:left;">Valor atualizado</th>
    					<th style="text-align:left;">Dt. atualização</th>
    					<th style="text-align:left;">Situação</th>
    				</tr>
    				<tr class="fundoEscuro" height="2" aria-hidden="true">
    					<td colspan="6">
    				</td></tr>
    			</thead>
    			<tbody>

    			</tbody>
    		</table>
    	</div>
    </form>






















    	<form action="/cpopg/show.do?processo.codigo=01Z081I9T0000&amp;processo.foro=1&amp;processo.numero=0070337-91.2008.8.06.0001" id="popupSenha" style="display: none;" method="POST">

    		<table role="document">
    			<tbody><tr>
    				<td colspan="2" style="padding-bottom:20px">Atendendo a resolução 121 do CNJ.</td>
    			</tr>

    				<tr>
    					<td colspan="2" style="padding-bottom:20px">Se for advogado(a) nesse processo, é necessário<span id="identificacao"><strong><a href="https://esaj.tjce.jus.br/esaj/identificacao.do?retorno=https%3A//esaj.tjce.jus.br/cpopg/show.do%3Fprocesso.codigo%3D01Z081I9T0000%26processo.foro%3D1%26processo.numero%3D0070337-91.2008.8.06.0001">Identificar-se</a></strong></span></td>



    							<script language="javascript" type="text/JavaScript" src="https://esaj.tjce.jus.br/sajcas/conteudoIdentificacao?script=1691514670104"></script>


    				</tr>

    			<tr align="center">
    				<td align="left" colspan="2" style="padding-bottom:20px">
    					<div style="float:left; line-height:30px;">Se for uma parte ou interessado, digite a senha do processo</div>
    					<div style="float:left;width: 140px; padding-left:15px">
    						<input type="password" name="senhaProcesso" maxlength="12" value="" rotulo="" class="form-control" id="senhaProcesso">
    						<input type="hidden" name="idRecursoQueProvocouLiberacaoPorSenha" value="">
    					</div>
    					<div class="unj-form-control-group__icon">
    						<div class="dropdown show">
    							<a href="javascript:;" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
    								<span class="glyph glyph-info" aria-hidden="true"></span>
    							</a>
    							<div class="dropdown-menu tooltip-campos" aria-labelledby="dropdownMenuLink">

    									É necessário informar uma senha para acessar processo em segredo de justiça, bem como para acessar autos dos demais processos.<br><br>
    									Se for parte do processo e ainda não possua uma senha, <b>solicite-a no cartório</b>.<br><br>


    							</div>
    						</div>
    					</div>
    				</td>
    			</tr>
    			<tr>
    				<td colspan="2" align="center">





















    	<input type="button" name="btFechar" value="Cancelar" onclick="" onmouseover="B_mOver(this);" onmouseout="B_mOut(this);" class="spwBotao " id="botaoFecharPopupSenha">






















    	<input type="submit" name="btEnviarSenha" value="Continuar" onclick="" onmouseover="B_mOver(this);" onmouseout="B_mOut(this);" class="spwBotaoDefault btn-space" id="btEnviarSenha">




    				</td>
    			</tr>
    		</tbody></table>
    	</form>





    </div>






















    <footer>
        <nav class="navbar__footer">
            <div class="navbar__footer__container">

                <ul class="navbar__footer__list-brand">
                    <li class="navbar__footer__list-brand__item">
                        <a href="https://www.softplan.com.br/solucoes/saj-tribunais/" class="navbar__footer__list-brand__item__link link_softplan_tribunais">
                            <img src="https://esaj.tjce.jus.br/esaj/img/brand/icon-saj.png" alt="SAJ">
                        </a>
                    </li>
                    <li class="navbar__footer__list-brand__item">
                        <a href="https://www.softplan.com.br/" class="navbar__footer__list-brand__item__link link_softplan">
                            <img src="https://esaj.tjce.jus.br/esaj/img/brand/icon-softplan.png" alt="Softplan">
                        </a>
                    </li>
                </ul>

                <ul class="navbar__footer__list-actions">
                </ul>
            </div>
        </nav>
    </footer>







    <script type="text/javascript">window.NREUM||(NREUM={});NREUM.info={"errorBeacon":"bam.nr-data.net","licenseKey":"b61bdf610d","agent":"","beacon":"bam.nr-data.net","applicationTime":255,"applicationID":"434000584","transactionName":"MlZRN0QECkMAVERZDgscYBdEEBBDIFREWQ4LHFERGAYLXU9EX1YVFV9SDRgWBVpPVEBfTxZHQRZCFkpRAkNZXw9LYFsMQSQHRAhYXg==","queueTime":0}</script>

    <div id="forest-ext-shadow-host"></div></body></html>
    """
    try:
        soup = BeautifulSoup(tjce_html_page, 'html.parser')
        return soup
    except Exception as e:
        print("Erro ao criar o objeto BeautifulSoup:", e)
        return None
