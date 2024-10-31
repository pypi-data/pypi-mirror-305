import{j as r}from"./reactflow-vendor-BDofclgK.js";import{r as s}from"./react-vendor-4ldeB94U.js";import{h as m,v as b,S as w}from"./index-D-ULYqgV.js";/**
 * @license @tabler/icons-react v3.18.0 - MIT
 *
 * This source code is licensed under the MIT license.
 * See the LICENSE file in the root directory of this source tree.
 */var j={outline:{xmlns:"http://www.w3.org/2000/svg",width:24,height:24,viewBox:"0 0 24 24",fill:"none",stroke:"currentColor",strokeWidth:2,strokeLinecap:"round",strokeLinejoin:"round"},filled:{xmlns:"http://www.w3.org/2000/svg",width:24,height:24,viewBox:"0 0 24 24",fill:"currentColor",stroke:"none"}};/**
 * @license @tabler/icons-react v3.18.0 - MIT
 *
 * This source code is licensed under the MIT license.
 * See the LICENSE file in the root directory of this source tree.
 */const u=(e,n,t,o)=>{const i=s.forwardRef(({color:l="currentColor",size:a=24,stroke:c=2,title:d,className:v,children:f,...x},g)=>s.createElement("svg",{ref:g,...j[e],width:a,height:a,className:["tabler-icon",`tabler-icon-${n}`,v].join(" "),...e==="filled"?{fill:l}:{strokeWidth:c,stroke:l},...x},[d&&s.createElement("title",{key:"svg-title"},d),...o.map(([p,y])=>s.createElement(p,y)),...Array.isArray(f)?f:[f]]));return i.displayName=`${t}`,i};/**
 * @license @tabler/icons-react v3.18.0 - MIT
 *
 * This source code is licensed under the MIT license.
 * See the LICENSE file in the root directory of this source tree.
 */var F=u("outline","folder","IconFolder",[["path",{d:"M5 4h4l3 3h7a2 2 0 0 1 2 2v8a2 2 0 0 1 -2 2h-14a2 2 0 0 1 -2 -2v-11a2 2 0 0 1 2 -2",key:"svg-0"}]]);/**
 * @license @tabler/icons-react v3.18.0 - MIT
 *
 * This source code is licensed under the MIT license.
 * See the LICENSE file in the root directory of this source tree.
 */var k=u("outline","loader-2","IconLoader2",[["path",{d:"M12 3a9 9 0 1 0 9 9",key:"svg-0"}]]);const h=s.forwardRef((e,n)=>{let{size:t=18,...o}=e;return typeof t=="string"&&(t=t==="sm"?12:t==="md"?24:18),r.jsxs("div",{...o,children:[r.jsx(k,{className:m("w-4 h-4 animate-spin",e.className)}),r.jsx("span",{className:"sr-only",children:"Loading..."})]})});h.displayName="Spinner";const N=b("inline-flex items-center justify-center whitespace-nowrap rounded-md text-sm font-medium ring-offset-background transition-colors focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring focus-visible:ring-offset-2 disabled:pointer-events-none disabled:opacity-50",{variants:{variant:{default:"bg-primary text-primary-foreground hover:bg-primary/90",destructive:"bg-destructive text-destructive-foreground hover:bg-destructive/90",outline:"border border-primary/60 border-2 hover:bg-accent hover:text-accent-foreground",secondary:"bg-secondary text-secondary-foreground hover:bg-secondary/80",ghost:"hover:bg-accent hover:text-accent-foreground",link:"text-primary underline-offset-4 hover:underline"},size:{default:"h-8 px-4 py-2",sm:"h-6 rounded-md px-3",lg:"h-10 rounded-md px-8",icon:"h-8 w-8"}},defaultVariants:{variant:"default",size:"default"}}),R=s.forwardRef(({className:e,variant:n,size:t,asChild:o=!1,isLoading:i=!1,left:l,...a},c)=>{const d=o?w:"button";return r.jsx(d,{className:m(N({variant:n,size:t,className:e})),ref:c,...a,disabled:i||a.disabled,children:i?r.jsxs("div",{className:"flex items-center gap-1",children:[r.jsx(h,{size:t==="default"?"md":t=="sm"?"sm":"lg"}),r.jsx("span",{children:a.children})]}):r.jsxs("div",{className:"flex items-center gap-1",children:[l&&r.jsx("div",{className:"w-4",children:l}),r.jsx("span",{children:a.children})]})})});R.displayName="Button";const S=s.forwardRef((e,n)=>r.jsx("div",{ref:n,style:{display:"flex",flexDirection:"row",alignItems:"center",...e.style},...e}));S.displayName="Flex";const C=s.forwardRef((e,n)=>r.jsx("div",{ref:n,style:{display:"flex",flexDirection:"column",...e.style},...e}));C.displayName="Stack";export{R as B,S as F,F as I,h as S,C as a,u as c};
