module.exports=function(t){return{transformIncoming:e=>e.scheme==="vscode-remote"?{scheme:"file",path:e.path}:e.scheme==="file"?{scheme:"vscode-local",path:e.path}:e,transformOutgoing:e=>e.scheme==="file"?{scheme:"vscode-remote",authority:t,path:e.path}:e.scheme==="vscode-local"?{scheme:"file",path:e.path}:e,transformOutgoingScheme:e=>e==="file"?"vscode-remote":e==="vscode-local"?"file":e}};

//# sourceMappingURL=https://ticino.blob.core.windows.net/sourcemaps/ee8c7def80afc00dd6e593ef12f37756d8f504ea/core/vs/server/uriTransformer.js.map
