(window["webpackJsonp"]=window["webpackJsonp"]||[]).push([[3],{"0Fdr":function(e,t,r){"use strict";var a=r("TqRt");Object.defineProperty(t,"__esModule",{value:!0}),t.default=void 0;var s=a(r("MVZn")),u=a(r("o0o1"));r("miYZ");var n=a(r("tsqr")),d=r("dCQc"),o=r("34ay"),c=r("HZnN"),i=r("7DNP"),l={namespace:"register",state:{status:void 0},effects:{submit:u.default.mark(function e(t,r){var a,s,o,c;return u.default.wrap(function(e){while(1)switch(e.prev=e.next){case 0:return a=t.payload,s=r.call,o=r.put,e.next=4,s(d.fakeRegister,a);case 4:if(c=e.sent,0!==c.code){e.next=11;break}return n.default.success(c.msg),e.next=9,o(i.routerRedux.push("/user/login"));case 9:e.next=12;break;case 11:n.default.error(c.msg);case 12:case"end":return e.stop()}},e,this)})},reducers:{registerHandle:function(e,t){var r=t.payload;return(0,o.setAuthority)("user"),(0,c.reloadAuthorized)(),(0,s.default)({},e,{status:r.status})}}};t.default=l}}]);