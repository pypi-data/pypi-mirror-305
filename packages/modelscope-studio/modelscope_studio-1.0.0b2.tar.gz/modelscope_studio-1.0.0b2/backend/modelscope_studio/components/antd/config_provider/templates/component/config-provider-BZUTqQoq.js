import { g as je, w as D, c as He } from "./Index-TdQBP9_Q.js";
const P = window.ms_globals.React, Te = window.ms_globals.React.forwardRef, Le = window.ms_globals.React.useRef, Pe = window.ms_globals.React.useState, Ee = window.ms_globals.React.useEffect, Ne = window.ms_globals.React.useMemo, Q = window.ms_globals.ReactDOM.createPortal, Ke = window.ms_globals.antdCssinjs.StyleProvider, Ue = window.ms_globals.antd.ConfigProvider, G = window.ms_globals.antd.theme, Se = window.ms_globals.dayjs;
var ve = {
  exports: {}
}, L = {};
/**
 * @license React
 * react-jsx-runtime.production.min.js
 *
 * Copyright (c) Facebook, Inc. and its affiliates.
 *
 * This source code is licensed under the MIT license found in the
 * LICENSE file in the root directory of this source tree.
 */
var Be = P, Ge = Symbol.for("react.element"), We = Symbol.for("react.fragment"), Ze = Object.prototype.hasOwnProperty, qe = Be.__SECRET_INTERNALS_DO_NOT_USE_OR_YOU_WILL_BE_FIRED.ReactCurrentOwner, Je = {
  key: !0,
  ref: !0,
  __self: !0,
  __source: !0
};
function ke(e, t, r) {
  var n, i = {}, o = null, s = null;
  r !== void 0 && (o = "" + r), t.key !== void 0 && (o = "" + t.key), t.ref !== void 0 && (s = t.ref);
  for (n in t) Ze.call(t, n) && !Je.hasOwnProperty(n) && (i[n] = t[n]);
  if (e && e.defaultProps) for (n in t = e.defaultProps, t) i[n] === void 0 && (i[n] = t[n]);
  return {
    $$typeof: Ge,
    type: e,
    key: o,
    ref: s,
    props: i,
    _owner: qe.current
  };
}
L.Fragment = We;
L.jsx = ke;
L.jsxs = ke;
ve.exports = L;
var R = ve.exports;
const {
  SvelteComponent: Qe,
  assign: le,
  binding_callbacks: ce,
  check_outros: Xe,
  children: Ce,
  claim_element: ze,
  claim_space: Ve,
  component_subscribe: ue,
  compute_slots: $e,
  create_slot: et,
  detach: k,
  element: Re,
  empty: fe,
  exclude_internal_props: ae,
  get_all_dirty_from_scope: tt,
  get_slot_changes: rt,
  group_outros: nt,
  init: ot,
  insert_hydration: x,
  safe_not_equal: it,
  set_custom_element_data: Oe,
  space: st,
  transition_in: F,
  transition_out: X,
  update_slot_base: lt
} = window.__gradio__svelte__internal, {
  beforeUpdate: ct,
  getContext: ut,
  onDestroy: ft,
  setContext: at
} = window.__gradio__svelte__internal;
function _e(e) {
  let t, r;
  const n = (
    /*#slots*/
    e[7].default
  ), i = et(
    n,
    e,
    /*$$scope*/
    e[6],
    null
  );
  return {
    c() {
      t = Re("svelte-slot"), i && i.c(), this.h();
    },
    l(o) {
      t = ze(o, "SVELTE-SLOT", {
        class: !0
      });
      var s = Ce(t);
      i && i.l(s), s.forEach(k), this.h();
    },
    h() {
      Oe(t, "class", "svelte-1rt0kpf");
    },
    m(o, s) {
      x(o, t, s), i && i.m(t, null), e[9](t), r = !0;
    },
    p(o, s) {
      i && i.p && (!r || s & /*$$scope*/
      64) && lt(
        i,
        n,
        o,
        /*$$scope*/
        o[6],
        r ? rt(
          n,
          /*$$scope*/
          o[6],
          s,
          null
        ) : tt(
          /*$$scope*/
          o[6]
        ),
        null
      );
    },
    i(o) {
      r || (F(i, o), r = !0);
    },
    o(o) {
      X(i, o), r = !1;
    },
    d(o) {
      o && k(t), i && i.d(o), e[9](null);
    }
  };
}
function _t(e) {
  let t, r, n, i, o = (
    /*$$slots*/
    e[4].default && _e(e)
  );
  return {
    c() {
      t = Re("react-portal-target"), r = st(), o && o.c(), n = fe(), this.h();
    },
    l(s) {
      t = ze(s, "REACT-PORTAL-TARGET", {
        class: !0
      }), Ce(t).forEach(k), r = Ve(s), o && o.l(s), n = fe(), this.h();
    },
    h() {
      Oe(t, "class", "svelte-1rt0kpf");
    },
    m(s, l) {
      x(s, t, l), e[8](t), x(s, r, l), o && o.m(s, l), x(s, n, l), i = !0;
    },
    p(s, [l]) {
      /*$$slots*/
      s[4].default ? o ? (o.p(s, l), l & /*$$slots*/
      16 && F(o, 1)) : (o = _e(s), o.c(), F(o, 1), o.m(n.parentNode, n)) : o && (nt(), X(o, 1, 1, () => {
        o = null;
      }), Xe());
    },
    i(s) {
      i || (F(o), i = !0);
    },
    o(s) {
      X(o), i = !1;
    },
    d(s) {
      s && (k(t), k(r), k(n)), e[8](null), o && o.d(s);
    }
  };
}
function de(e) {
  const {
    svelteInit: t,
    ...r
  } = e;
  return r;
}
function dt(e, t, r) {
  let n, i, {
    $$slots: o = {},
    $$scope: s
  } = t;
  const l = $e(o);
  let {
    svelteInit: c
  } = t;
  const g = D(de(t)), a = D();
  ue(e, a, (f) => r(0, n = f));
  const p = D();
  ue(e, p, (f) => r(1, i = f));
  const u = [], _ = ut("$$ms-gr-react-wrapper"), {
    slotKey: d,
    slotIndex: v,
    subSlotIndex: U
  } = je() || {}, B = c({
    parent: _,
    props: g,
    target: a,
    slot: p,
    slotKey: d,
    slotIndex: v,
    subSlotIndex: U,
    onDestroy(f) {
      u.push(f);
    }
  });
  at("$$ms-gr-react-wrapper", B), ct(() => {
    g.set(de(t));
  }), ft(() => {
    u.forEach((f) => f());
  });
  function A(f) {
    ce[f ? "unshift" : "push"](() => {
      n = f, a.set(n);
    });
  }
  function w(f) {
    ce[f ? "unshift" : "push"](() => {
      i = f, p.set(i);
    });
  }
  return e.$$set = (f) => {
    r(17, t = le(le({}, t), ae(f))), "svelteInit" in f && r(5, c = f.svelteInit), "$$scope" in f && r(6, s = f.$$scope);
  }, t = ae(t), [n, i, a, p, l, c, s, o, A, w];
}
class mt extends Qe {
  constructor(t) {
    super(), ot(this, t, dt, _t, it, {
      svelteInit: 5
    });
  }
}
const me = window.ms_globals.rerender, W = window.ms_globals.tree;
function ht(e) {
  function t(r) {
    const n = D(), i = new mt({
      ...r,
      props: {
        svelteInit(o) {
          window.ms_globals.autokey += 1;
          const s = {
            key: window.ms_globals.autokey,
            svelteInstance: n,
            reactComponent: e,
            props: o.props,
            slot: o.slot,
            target: o.target,
            slotIndex: o.slotIndex,
            subSlotIndex: o.subSlotIndex,
            slotKey: o.slotKey,
            nodes: []
          }, l = o.parent ?? W;
          return l.nodes = [...l.nodes, s], me({
            createPortal: Q,
            node: W
          }), o.onDestroy(() => {
            l.nodes = l.nodes.filter((c) => c.svelteInstance !== n), me({
              createPortal: Q,
              node: W
            });
          }), s;
        },
        ...r.props
      }
    });
    return n.set(i), i;
  }
  return new Promise((r) => {
    window.ms_globals.initializePromise.then(() => {
      r(t);
    });
  });
}
const pt = ["animationIterationCount", "borderImageOutset", "borderImageSlice", "borderImageWidth", "boxFlex", "boxFlexGroup", "boxOrdinalGroup", "columnCount", "columns", "flex", "flexGrow", "flexPositive", "flexShrink", "flexNegative", "flexOrder", "gridArea", "gridColumn", "gridColumnEnd", "gridColumnStart", "gridRow", "gridRowEnd", "gridRowStart", "lineClamp", "lineHeight", "opacity", "order", "orphans", "tabSize", "widows", "zIndex", "zoom", "fontWeight", "letterSpacing", "lineHeight"];
function yt(e) {
  return e ? Object.keys(e).reduce((t, r) => {
    const n = e[r];
    return typeof n == "number" && !pt.includes(r) ? t[r] = n + "px" : t[r] = n, t;
  }, {}) : {};
}
function V(e) {
  const t = [], r = e.cloneNode(!1);
  if (e._reactElement)
    return t.push(Q(P.cloneElement(e._reactElement, {
      ...e._reactElement.props,
      children: P.Children.toArray(e._reactElement.props.children).map((i) => {
        if (P.isValidElement(i) && i.props.__slot__) {
          const {
            portals: o,
            clonedElement: s
          } = V(i.props.el);
          return P.cloneElement(i, {
            ...i.props,
            el: s,
            children: [...P.Children.toArray(i.props.children), ...o]
          });
        }
        return null;
      })
    }), r)), {
      clonedElement: r,
      portals: t
    };
  Object.keys(e.getEventListeners()).forEach((i) => {
    e.getEventListeners(i).forEach(({
      listener: s,
      type: l,
      useCapture: c
    }) => {
      r.addEventListener(l, s, c);
    });
  });
  const n = Array.from(e.childNodes);
  for (let i = 0; i < n.length; i++) {
    const o = n[i];
    if (o.nodeType === 1) {
      const {
        clonedElement: s,
        portals: l
      } = V(o);
      t.push(...l), r.appendChild(s);
    } else o.nodeType === 3 && r.appendChild(o.cloneNode());
  }
  return {
    clonedElement: r,
    portals: t
  };
}
function gt(e, t) {
  e && (typeof e == "function" ? e(t) : e.current = t);
}
const Ie = Te(({
  slot: e,
  clone: t,
  className: r,
  style: n
}, i) => {
  const o = Le(), [s, l] = Pe([]);
  return Ee(() => {
    var p;
    if (!o.current || !e)
      return;
    let c = e;
    function g() {
      let u = c;
      if (c.tagName.toLowerCase() === "svelte-slot" && c.children.length === 1 && c.children[0] && (u = c.children[0], u.tagName.toLowerCase() === "react-portal-target" && u.children[0] && (u = u.children[0])), gt(i, u), r && u.classList.add(...r.split(" ")), n) {
        const _ = yt(n);
        Object.keys(_).forEach((d) => {
          u.style[d] = _[d];
        });
      }
    }
    let a = null;
    if (t && window.MutationObserver) {
      let u = function() {
        var v;
        const {
          portals: _,
          clonedElement: d
        } = V(e);
        c = d, l(_), c.style.display = "contents", g(), (v = o.current) == null || v.appendChild(c);
      };
      u(), a = new window.MutationObserver(() => {
        var _, d;
        (_ = o.current) != null && _.contains(c) && ((d = o.current) == null || d.removeChild(c)), u();
      }), a.observe(e, {
        attributes: !0,
        childList: !0,
        subtree: !0
      });
    } else
      c.style.display = "contents", g(), (p = o.current) == null || p.appendChild(c);
    return () => {
      var u, _;
      c.style.display = "", (u = o.current) != null && u.contains(c) && ((_ = o.current) == null || _.removeChild(c)), a == null || a.disconnect();
    };
  }, [e, t, r, n, i]), P.createElement("react-child", {
    ref: o,
    style: {
      display: "contents"
    }
  }, ...s);
});
function wt(e) {
  try {
    return typeof e == "string" ? new Function(`return (...args) => (${e})(...args)`)() : void 0;
  } catch {
    return;
  }
}
function Z(e) {
  return Ne(() => wt(e), [e]);
}
function bt(e, t) {
  return e ? /* @__PURE__ */ R.jsx(Ie, {
    slot: e,
    clone: t == null ? void 0 : t.clone
  }) : null;
}
function Pt({
  key: e,
  setSlotParams: t,
  slots: r
}, n) {
  return (...i) => (t(e, i), bt(r[e], {
    clone: !0,
    ...n
  }));
}
var Ae = Symbol.for("immer-nothing"), he = Symbol.for("immer-draftable"), m = Symbol.for("immer-state");
function y(e, ...t) {
  throw new Error(`[Immer] minified error nr: ${e}. Full error at: https://bit.ly/3cXEKWf`);
}
var C = Object.getPrototypeOf;
function z(e) {
  return !!e && !!e[m];
}
function E(e) {
  var t;
  return e ? De(e) || Array.isArray(e) || !!e[he] || !!((t = e.constructor) != null && t[he]) || j(e) || H(e) : !1;
}
var Et = Object.prototype.constructor.toString();
function De(e) {
  if (!e || typeof e != "object") return !1;
  const t = C(e);
  if (t === null)
    return !0;
  const r = Object.hasOwnProperty.call(t, "constructor") && t.constructor;
  return r === Object ? !0 : typeof r == "function" && Function.toString.call(r) === Et;
}
function Y(e, t) {
  N(e) === 0 ? Reflect.ownKeys(e).forEach((r) => {
    t(r, e[r], e);
  }) : e.forEach((r, n) => t(n, r, e));
}
function N(e) {
  const t = e[m];
  return t ? t.type_ : Array.isArray(e) ? 1 : j(e) ? 2 : H(e) ? 3 : 0;
}
function $(e, t) {
  return N(e) === 2 ? e.has(t) : Object.prototype.hasOwnProperty.call(e, t);
}
function xe(e, t, r) {
  const n = N(e);
  n === 2 ? e.set(t, r) : n === 3 ? e.add(r) : e[t] = r;
}
function St(e, t) {
  return e === t ? e !== 0 || 1 / e === 1 / t : e !== e && t !== t;
}
function j(e) {
  return e instanceof Map;
}
function H(e) {
  return e instanceof Set;
}
function b(e) {
  return e.copy_ || e.base_;
}
function ee(e, t) {
  if (j(e))
    return new Map(e);
  if (H(e))
    return new Set(e);
  if (Array.isArray(e)) return Array.prototype.slice.call(e);
  const r = De(e);
  if (t === !0 || t === "class_only" && !r) {
    const n = Object.getOwnPropertyDescriptors(e);
    delete n[m];
    let i = Reflect.ownKeys(n);
    for (let o = 0; o < i.length; o++) {
      const s = i[o], l = n[s];
      l.writable === !1 && (l.writable = !0, l.configurable = !0), (l.get || l.set) && (n[s] = {
        configurable: !0,
        writable: !0,
        // could live with !!desc.set as well here...
        enumerable: l.enumerable,
        value: e[s]
      });
    }
    return Object.create(C(e), n);
  } else {
    const n = C(e);
    if (n !== null && r)
      return {
        ...e
      };
    const i = Object.create(n);
    return Object.assign(i, e);
  }
}
function ie(e, t = !1) {
  return K(e) || z(e) || !E(e) || (N(e) > 1 && (e.set = e.add = e.clear = e.delete = vt), Object.freeze(e), t && Object.entries(e).forEach(([r, n]) => ie(n, !0))), e;
}
function vt() {
  y(2);
}
function K(e) {
  return Object.isFrozen(e);
}
var kt = {};
function S(e) {
  const t = kt[e];
  return t || y(0, e), t;
}
var O;
function Fe() {
  return O;
}
function Ct(e, t) {
  return {
    drafts_: [],
    parent_: e,
    immer_: t,
    // Whenever the modified draft contains a draft from another scope, we
    // need to prevent auto-freezing so the unowned draft can be finalized.
    canAutoFreeze_: !0,
    unfinalizedDrafts_: 0
  };
}
function pe(e, t) {
  t && (S("Patches"), e.patches_ = [], e.inversePatches_ = [], e.patchListener_ = t);
}
function te(e) {
  re(e), e.drafts_.forEach(zt), e.drafts_ = null;
}
function re(e) {
  e === O && (O = e.parent_);
}
function ye(e) {
  return O = Ct(O, e);
}
function zt(e) {
  const t = e[m];
  t.type_ === 0 || t.type_ === 1 ? t.revoke_() : t.revoked_ = !0;
}
function ge(e, t) {
  t.unfinalizedDrafts_ = t.drafts_.length;
  const r = t.drafts_[0];
  return e !== void 0 && e !== r ? (r[m].modified_ && (te(t), y(4)), E(e) && (e = M(t, e), t.parent_ || T(t, e)), t.patches_ && S("Patches").generateReplacementPatches_(r[m].base_, e, t.patches_, t.inversePatches_)) : e = M(t, r, []), te(t), t.patches_ && t.patchListener_(t.patches_, t.inversePatches_), e !== Ae ? e : void 0;
}
function M(e, t, r) {
  if (K(t)) return t;
  const n = t[m];
  if (!n)
    return Y(t, (i, o) => we(e, n, t, i, o, r)), t;
  if (n.scope_ !== e) return t;
  if (!n.modified_)
    return T(e, n.base_, !0), n.base_;
  if (!n.finalized_) {
    n.finalized_ = !0, n.scope_.unfinalizedDrafts_--;
    const i = n.copy_;
    let o = i, s = !1;
    n.type_ === 3 && (o = new Set(i), i.clear(), s = !0), Y(o, (l, c) => we(e, n, i, l, c, r, s)), T(e, i, !1), r && e.patches_ && S("Patches").generatePatches_(n, r, e.patches_, e.inversePatches_);
  }
  return n.copy_;
}
function we(e, t, r, n, i, o, s) {
  if (z(i)) {
    const l = o && t && t.type_ !== 3 && // Set objects are atomic since they have no keys.
    !$(t.assigned_, n) ? o.concat(n) : void 0, c = M(e, i, l);
    if (xe(r, n, c), z(c))
      e.canAutoFreeze_ = !1;
    else return;
  } else s && r.add(i);
  if (E(i) && !K(i)) {
    if (!e.immer_.autoFreeze_ && e.unfinalizedDrafts_ < 1)
      return;
    M(e, i), (!t || !t.scope_.parent_) && typeof n != "symbol" && Object.prototype.propertyIsEnumerable.call(r, n) && T(e, i);
  }
}
function T(e, t, r = !1) {
  !e.parent_ && e.immer_.autoFreeze_ && e.canAutoFreeze_ && ie(t, r);
}
function Rt(e, t) {
  const r = Array.isArray(e), n = {
    type_: r ? 1 : 0,
    // Track which produce call this is associated with.
    scope_: t ? t.scope_ : Fe(),
    // True for both shallow and deep changes.
    modified_: !1,
    // Used during finalization.
    finalized_: !1,
    // Track which properties have been assigned (true) or deleted (false).
    assigned_: {},
    // The parent draft state.
    parent_: t,
    // The base state.
    base_: e,
    // The base proxy.
    draft_: null,
    // set below
    // The base copy with any updated values.
    copy_: null,
    // Called by the `produce` function.
    revoke_: null,
    isManual_: !1
  };
  let i = n, o = se;
  r && (i = [n], o = I);
  const {
    revoke: s,
    proxy: l
  } = Proxy.revocable(i, o);
  return n.draft_ = l, n.revoke_ = s, l;
}
var se = {
  get(e, t) {
    if (t === m) return e;
    const r = b(e);
    if (!$(r, t))
      return Ot(e, r, t);
    const n = r[t];
    return e.finalized_ || !E(n) ? n : n === q(e.base_, t) ? (J(e), e.copy_[t] = oe(n, e)) : n;
  },
  has(e, t) {
    return t in b(e);
  },
  ownKeys(e) {
    return Reflect.ownKeys(b(e));
  },
  set(e, t, r) {
    const n = Ye(b(e), t);
    if (n != null && n.set)
      return n.set.call(e.draft_, r), !0;
    if (!e.modified_) {
      const i = q(b(e), t), o = i == null ? void 0 : i[m];
      if (o && o.base_ === r)
        return e.copy_[t] = r, e.assigned_[t] = !1, !0;
      if (St(r, i) && (r !== void 0 || $(e.base_, t))) return !0;
      J(e), ne(e);
    }
    return e.copy_[t] === r && // special case: handle new props with value 'undefined'
    (r !== void 0 || t in e.copy_) || // special case: NaN
    Number.isNaN(r) && Number.isNaN(e.copy_[t]) || (e.copy_[t] = r, e.assigned_[t] = !0), !0;
  },
  deleteProperty(e, t) {
    return q(e.base_, t) !== void 0 || t in e.base_ ? (e.assigned_[t] = !1, J(e), ne(e)) : delete e.assigned_[t], e.copy_ && delete e.copy_[t], !0;
  },
  // Note: We never coerce `desc.value` into an Immer draft, because we can't make
  // the same guarantee in ES5 mode.
  getOwnPropertyDescriptor(e, t) {
    const r = b(e), n = Reflect.getOwnPropertyDescriptor(r, t);
    return n && {
      writable: !0,
      configurable: e.type_ !== 1 || t !== "length",
      enumerable: n.enumerable,
      value: r[t]
    };
  },
  defineProperty() {
    y(11);
  },
  getPrototypeOf(e) {
    return C(e.base_);
  },
  setPrototypeOf() {
    y(12);
  }
}, I = {};
Y(se, (e, t) => {
  I[e] = function() {
    return arguments[0] = arguments[0][0], t.apply(this, arguments);
  };
});
I.deleteProperty = function(e, t) {
  return I.set.call(this, e, t, void 0);
};
I.set = function(e, t, r) {
  return se.set.call(this, e[0], t, r, e[0]);
};
function q(e, t) {
  const r = e[m];
  return (r ? b(r) : e)[t];
}
function Ot(e, t, r) {
  var i;
  const n = Ye(t, r);
  return n ? "value" in n ? n.value : (
    // This is a very special case, if the prop is a getter defined by the
    // prototype, we should invoke it with the draft as context!
    (i = n.get) == null ? void 0 : i.call(e.draft_)
  ) : void 0;
}
function Ye(e, t) {
  if (!(t in e)) return;
  let r = C(e);
  for (; r; ) {
    const n = Object.getOwnPropertyDescriptor(r, t);
    if (n) return n;
    r = C(r);
  }
}
function ne(e) {
  e.modified_ || (e.modified_ = !0, e.parent_ && ne(e.parent_));
}
function J(e) {
  e.copy_ || (e.copy_ = ee(e.base_, e.scope_.immer_.useStrictShallowCopy_));
}
var It = class {
  constructor(e) {
    this.autoFreeze_ = !0, this.useStrictShallowCopy_ = !1, this.produce = (t, r, n) => {
      if (typeof t == "function" && typeof r != "function") {
        const o = r;
        r = t;
        const s = this;
        return function(c = o, ...g) {
          return s.produce(c, (a) => r.call(this, a, ...g));
        };
      }
      typeof r != "function" && y(6), n !== void 0 && typeof n != "function" && y(7);
      let i;
      if (E(t)) {
        const o = ye(this), s = oe(t, void 0);
        let l = !0;
        try {
          i = r(s), l = !1;
        } finally {
          l ? te(o) : re(o);
        }
        return pe(o, n), ge(i, o);
      } else if (!t || typeof t != "object") {
        if (i = r(t), i === void 0 && (i = t), i === Ae && (i = void 0), this.autoFreeze_ && ie(i, !0), n) {
          const o = [], s = [];
          S("Patches").generateReplacementPatches_(t, i, o, s), n(o, s);
        }
        return i;
      } else y(1, t);
    }, this.produceWithPatches = (t, r) => {
      if (typeof t == "function")
        return (s, ...l) => this.produceWithPatches(s, (c) => t(c, ...l));
      let n, i;
      return [this.produce(t, r, (s, l) => {
        n = s, i = l;
      }), n, i];
    }, typeof (e == null ? void 0 : e.autoFreeze) == "boolean" && this.setAutoFreeze(e.autoFreeze), typeof (e == null ? void 0 : e.useStrictShallowCopy) == "boolean" && this.setUseStrictShallowCopy(e.useStrictShallowCopy);
  }
  createDraft(e) {
    E(e) || y(8), z(e) && (e = At(e));
    const t = ye(this), r = oe(e, void 0);
    return r[m].isManual_ = !0, re(t), r;
  }
  finishDraft(e, t) {
    const r = e && e[m];
    (!r || !r.isManual_) && y(9);
    const {
      scope_: n
    } = r;
    return pe(n, t), ge(void 0, n);
  }
  /**
   * Pass true to automatically freeze all copies created by Immer.
   *
   * By default, auto-freezing is enabled.
   */
  setAutoFreeze(e) {
    this.autoFreeze_ = e;
  }
  /**
   * Pass true to enable strict shallow copy.
   *
   * By default, immer does not copy the object descriptors such as getter, setter and non-enumrable properties.
   */
  setUseStrictShallowCopy(e) {
    this.useStrictShallowCopy_ = e;
  }
  applyPatches(e, t) {
    let r;
    for (r = t.length - 1; r >= 0; r--) {
      const i = t[r];
      if (i.path.length === 0 && i.op === "replace") {
        e = i.value;
        break;
      }
    }
    r > -1 && (t = t.slice(r + 1));
    const n = S("Patches").applyPatches_;
    return z(e) ? n(e, t) : this.produce(e, (i) => n(i, t));
  }
};
function oe(e, t) {
  const r = j(e) ? S("MapSet").proxyMap_(e, t) : H(e) ? S("MapSet").proxySet_(e, t) : Rt(e, t);
  return (t ? t.scope_ : Fe()).drafts_.push(r), r;
}
function At(e) {
  return z(e) || y(10, e), Me(e);
}
function Me(e) {
  if (!E(e) || K(e)) return e;
  const t = e[m];
  let r;
  if (t) {
    if (!t.modified_) return t.base_;
    t.finalized_ = !0, r = ee(e, t.scope_.immer_.useStrictShallowCopy_);
  } else
    r = ee(e, !0);
  return Y(r, (n, i) => {
    xe(r, n, Me(i));
  }), t && (t.finalized_ = !1), r;
}
var h = new It(), Dt = h.produce;
h.produceWithPatches.bind(h);
h.setAutoFreeze.bind(h);
h.setUseStrictShallowCopy.bind(h);
h.applyPatches.bind(h);
h.createDraft.bind(h);
h.finishDraft.bind(h);
var xt = {
  exports: {}
};
(function(e, t) {
  (function(r, n) {
    e.exports = n(Se);
  })(He, function(r) {
    function n(s) {
      return s && typeof s == "object" && "default" in s ? s : {
        default: s
      };
    }
    var i = n(r), o = {
      name: "zh-cn",
      weekdays: "星期日_星期一_星期二_星期三_星期四_星期五_星期六".split("_"),
      weekdaysShort: "周日_周一_周二_周三_周四_周五_周六".split("_"),
      weekdaysMin: "日_一_二_三_四_五_六".split("_"),
      months: "一月_二月_三月_四月_五月_六月_七月_八月_九月_十月_十一月_十二月".split("_"),
      monthsShort: "1月_2月_3月_4月_5月_6月_7月_8月_9月_10月_11月_12月".split("_"),
      ordinal: function(s, l) {
        return l === "W" ? s + "周" : s + "日";
      },
      weekStart: 1,
      yearStart: 4,
      formats: {
        LT: "HH:mm",
        LTS: "HH:mm:ss",
        L: "YYYY/MM/DD",
        LL: "YYYY年M月D日",
        LLL: "YYYY年M月D日Ah点mm分",
        LLLL: "YYYY年M月D日ddddAh点mm分",
        l: "YYYY/M/D",
        ll: "YYYY年M月D日",
        lll: "YYYY年M月D日 HH:mm",
        llll: "YYYY年M月D日dddd HH:mm"
      },
      relativeTime: {
        future: "%s内",
        past: "%s前",
        s: "几秒",
        m: "1 分钟",
        mm: "%d 分钟",
        h: "1 小时",
        hh: "%d 小时",
        d: "1 天",
        dd: "%d 天",
        M: "1 个月",
        MM: "%d 个月",
        y: "1 年",
        yy: "%d 年"
      },
      meridiem: function(s, l) {
        var c = 100 * s + l;
        return c < 600 ? "凌晨" : c < 900 ? "早上" : c < 1100 ? "上午" : c < 1300 ? "中午" : c < 1800 ? "下午" : "晚上";
      }
    };
    return i.default.locale(o, null, !0), o;
  });
})(xt);
const be = {
  ar_EG: () => import("./ar_EG-DikqxAFn.js").then((e) => e.a),
  az_AZ: () => import("./az_AZ--EGX7Z6W.js").then((e) => e.a),
  bg_BG: () => import("./bg_BG-CpgrFyWJ.js").then((e) => e.b),
  bn_BD: () => import("./bn_BD-_sr4b-e3.js").then((e) => e.b),
  by_BY: () => import("./by_BY-D6q4x54b.js").then((e) => e.b),
  ca_ES: () => import("./ca_ES-D8FBl2F7.js").then((e) => e.c),
  cs_CZ: () => import("./cs_CZ-DW7MGZSs.js").then((e) => e.c),
  da_DK: () => import("./da_DK-Ckj7-wi8.js").then((e) => e.d),
  de_DE: () => import("./de_DE-CgGDrzMw.js").then((e) => e.d),
  el_GR: () => import("./el_GR-BJtxwhBO.js").then((e) => e.e),
  en_GB: () => import("./en_GB-Q3Bwkchl.js").then((e) => e.e),
  en_US: () => import("./en_US-C4Z8x8G8.js").then((e) => e.e),
  es_ES: () => import("./es_ES-CRvpZTy3.js").then((e) => e.e),
  et_EE: () => import("./et_EE-B4z6vPsF.js").then((e) => e.e),
  eu_ES: () => import("./eu_ES-Datgf-aA.js").then((e) => e.e),
  fa_IR: () => import("./fa_IR-Cy-r4sAI.js").then((e) => e.f),
  fi_FI: () => import("./fi_FI-BDj2oOky.js").then((e) => e.f),
  fr_BE: () => import("./fr_BE-BHhkw4Vt.js").then((e) => e.f),
  fr_CA: () => import("./fr_CA-BRZlu8G_.js").then((e) => e.f),
  fr_FR: () => import("./fr_FR-BDl2zuJJ.js").then((e) => e.f),
  ga_IE: () => import("./ga_IE-DRR3nU9v.js").then((e) => e.g),
  gl_ES: () => import("./gl_ES-BZ0cZmH0.js").then((e) => e.g),
  he_IL: () => import("./he_IL-BfzIxsAI.js").then((e) => e.h),
  hi_IN: () => import("./hi_IN-aQwYy9WI.js").then((e) => e.h),
  hr_HR: () => import("./hr_HR-6H-tkRPD.js").then((e) => e.h),
  hu_HU: () => import("./hu_HU-DonOw886.js").then((e) => e.h),
  hy_AM: () => import("./hy_AM-B2MhPC10.js").then((e) => e.h),
  id_ID: () => import("./id_ID-MKs1GncM.js").then((e) => e.i),
  is_IS: () => import("./is_IS-D4tCOzj6.js").then((e) => e.i),
  it_IT: () => import("./it_IT-Y6j4ycof.js").then((e) => e.i),
  ja_JP: () => import("./ja_JP-CzIJGULe.js").then((e) => e.j),
  ka_GE: () => import("./ka_GE-CTogdzZ0.js").then((e) => e.k),
  kk_KZ: () => import("./kk_KZ-DOpoBw60.js").then((e) => e.k),
  km_KH: () => import("./km_KH-B68zoUzO.js").then((e) => e.k),
  kmr_IQ: () => import("./kmr_IQ-C-zM74Ho.js").then((e) => e.k),
  kn_IN: () => import("./kn_IN-DI3NRlm_.js").then((e) => e.k),
  ko_KR: () => import("./ko_KR-w924Es5f.js").then((e) => e.k),
  ku_IQ: () => import("./ku_IQ-CC5B-82g.js").then((e) => e.k),
  lt_LT: () => import("./lt_LT-Bym2s2e6.js").then((e) => e.l),
  lv_LV: () => import("./lv_LV-kyJ4VTnz.js").then((e) => e.l),
  mk_MK: () => import("./mk_MK-D7r7Ytlu.js").then((e) => e.m),
  ml_IN: () => import("./ml_IN-Yu01dqyH.js").then((e) => e.m),
  mn_MN: () => import("./mn_MN-BXrWD6X2.js").then((e) => e.m),
  ms_MY: () => import("./ms_MY-CzBCE5O9.js").then((e) => e.m),
  my_MM: () => import("./my_MM-CBKO_QV4.js").then((e) => e.m),
  nb_NO: () => import("./nb_NO-C9n0hyOj.js").then((e) => e.n),
  ne_NP: () => import("./ne_NP-oBBd-PeD.js").then((e) => e.n),
  nl_BE: () => import("./nl_BE-8xA9QDo-.js").then((e) => e.n),
  nl_NL: () => import("./nl_NL-CyVCU3fJ.js").then((e) => e.n),
  pl_PL: () => import("./pl_PL-B8sNAiY4.js").then((e) => e.p),
  pt_BR: () => import("./pt_BR-DJd-RLbR.js").then((e) => e.p),
  pt_PT: () => import("./pt_PT-BpGGlz1o.js").then((e) => e.p),
  ro_RO: () => import("./ro_RO-W82xvk29.js").then((e) => e.r),
  ru_RU: () => import("./ru_RU-CbN3qb5J.js").then((e) => e.r),
  si_LK: () => import("./si_LK-DXUXSq10.js").then((e) => e.s),
  sk_SK: () => import("./sk_SK-BjLRgmze.js").then((e) => e.s),
  sl_SI: () => import("./sl_SI-BJs5sVw6.js").then((e) => e.s),
  sr_RS: () => import("./sr_RS-CKdEHtPQ.js").then((e) => e.s),
  sv_SE: () => import("./sv_SE-CQRCHaEV.js").then((e) => e.s),
  ta_IN: () => import("./ta_IN-BDuQe0qK.js").then((e) => e.t),
  th_TH: () => import("./th_TH-DzG8FS_S.js").then((e) => e.t),
  tk_TK: () => import("./tk_TK-BieoG0dN.js").then((e) => e.t),
  tr_TR: () => import("./tr_TR-Bjbxef-w.js").then((e) => e.t),
  uk_UA: () => import("./uk_UA-DoWFAxq0.js").then((e) => e.u),
  ur_PK: () => import("./ur_PK-BJoFr92s.js").then((e) => e.u),
  uz_UZ: () => import("./uz_UZ-C_HCrzSJ.js").then((e) => e.u),
  vi_VN: () => import("./vi_VN-CGmPQrUa.js").then((e) => e.v),
  zh_CN: () => import("./zh_CN-DR-mcCeY.js").then((e) => e.z),
  zh_HK: () => import("./zh_HK-DULocUqX.js").then((e) => e.z),
  zh_TW: () => import("./zh_TW-MnXdVk7O.js").then((e) => e.z)
}, Ft = (e, t) => Dt(e, (r) => {
  Object.keys(t).forEach((n) => {
    const i = n.split(".");
    let o = r;
    for (let s = 0; s < i.length - 1; s++) {
      const l = i[s];
      o[l] || (o[l] = {}), o = o[l];
    }
    o[i[i.length - 1]] = /* @__PURE__ */ R.jsx(Ie, {
      slot: t[n],
      clone: !0
    });
  });
}), Mt = ht(({
  slots: e,
  themeMode: t,
  id: r,
  className: n,
  style: i,
  locale: o,
  getTargetContainer: s,
  getPopupContainer: l,
  renderEmpty: c,
  setSlotParams: g,
  children: a,
  ...p
}) => {
  var A;
  const [u, _] = Pe(), d = {
    dark: t === "dark",
    ...((A = p.theme) == null ? void 0 : A.algorithm) || {}
  }, v = Z(l), U = Z(s), B = Z(c);
  return Ee(() => {
    o && be[o] && be[o]().then((w) => {
      _(w.default), o === "zh_CN" && Se.locale("zh-cn");
    });
  }, [o]), /* @__PURE__ */ R.jsx("div", {
    id: r,
    className: n,
    style: i,
    children: /* @__PURE__ */ R.jsx(Ke, {
      hashPriority: "high",
      container: document.body,
      children: /* @__PURE__ */ R.jsx(Ue, {
        prefixCls: "ms-gr-ant",
        ...Ft(p, e),
        locale: u,
        getPopupContainer: v,
        getTargetContainer: U,
        renderEmpty: e.renderEmpty ? Pt({
          slots: e,
          setSlotParams: g,
          key: "renderEmpty"
        }) : B,
        theme: {
          cssVar: !0,
          ...p.theme,
          algorithm: Object.keys(d).map((w) => {
            switch (w) {
              case "dark":
                return d[w] ? G.darkAlgorithm : G.defaultAlgorithm;
              case "compact":
                return d[w] ? G.compactAlgorithm : null;
              default:
                return null;
            }
          }).filter(Boolean)
        },
        children: a
      })
    })
  });
});
export {
  Mt as ConfigProvider,
  Mt as default
};
