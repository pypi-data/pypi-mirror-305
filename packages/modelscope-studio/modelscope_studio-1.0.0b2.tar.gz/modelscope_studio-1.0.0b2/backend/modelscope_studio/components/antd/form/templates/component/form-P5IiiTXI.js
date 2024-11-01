import { g as $, w as b } from "./Index-glwwRWGp.js";
const h = window.ms_globals.React, Y = window.ms_globals.React.useMemo, Q = window.ms_globals.React.forwardRef, X = window.ms_globals.React.useRef, Z = window.ms_globals.React.useState, D = window.ms_globals.React.useEffect, R = window.ms_globals.ReactDOM.createPortal, x = window.ms_globals.antd.Form;
var M = {
  exports: {}
}, v = {};
/**
 * @license React
 * react-jsx-runtime.production.min.js
 *
 * Copyright (c) Facebook, Inc. and its affiliates.
 *
 * This source code is licensed under the MIT license found in the
 * LICENSE file in the root directory of this source tree.
 */
var ee = h, te = Symbol.for("react.element"), ne = Symbol.for("react.fragment"), re = Object.prototype.hasOwnProperty, oe = ee.__SECRET_INTERNALS_DO_NOT_USE_OR_YOU_WILL_BE_FIRED.ReactCurrentOwner, se = {
  key: !0,
  ref: !0,
  __self: !0,
  __source: !0
};
function W(t, n, o) {
  var s, r = {}, e = null, l = null;
  o !== void 0 && (e = "" + o), n.key !== void 0 && (e = "" + n.key), n.ref !== void 0 && (l = n.ref);
  for (s in n) re.call(n, s) && !se.hasOwnProperty(s) && (r[s] = n[s]);
  if (t && t.defaultProps) for (s in n = t.defaultProps, n) r[s] === void 0 && (r[s] = n[s]);
  return {
    $$typeof: te,
    type: t,
    key: e,
    ref: l,
    props: r,
    _owner: oe.current
  };
}
v.Fragment = ne;
v.jsx = W;
v.jsxs = W;
M.exports = v;
var z = M.exports;
const {
  SvelteComponent: le,
  assign: k,
  binding_callbacks: O,
  check_outros: ie,
  children: G,
  claim_element: U,
  claim_space: ce,
  component_subscribe: P,
  compute_slots: ae,
  create_slot: ue,
  detach: g,
  element: q,
  empty: F,
  exclude_internal_props: L,
  get_all_dirty_from_scope: de,
  get_slot_changes: fe,
  group_outros: _e,
  init: pe,
  insert_hydration: y,
  safe_not_equal: me,
  set_custom_element_data: H,
  space: he,
  transition_in: E,
  transition_out: S,
  update_slot_base: ge
} = window.__gradio__svelte__internal, {
  beforeUpdate: we,
  getContext: be,
  onDestroy: ye,
  setContext: Ee
} = window.__gradio__svelte__internal;
function T(t) {
  let n, o;
  const s = (
    /*#slots*/
    t[7].default
  ), r = ue(
    s,
    t,
    /*$$scope*/
    t[6],
    null
  );
  return {
    c() {
      n = q("svelte-slot"), r && r.c(), this.h();
    },
    l(e) {
      n = U(e, "SVELTE-SLOT", {
        class: !0
      });
      var l = G(n);
      r && r.l(l), l.forEach(g), this.h();
    },
    h() {
      H(n, "class", "svelte-1rt0kpf");
    },
    m(e, l) {
      y(e, n, l), r && r.m(n, null), t[9](n), o = !0;
    },
    p(e, l) {
      r && r.p && (!o || l & /*$$scope*/
      64) && ge(
        r,
        s,
        e,
        /*$$scope*/
        e[6],
        o ? fe(
          s,
          /*$$scope*/
          e[6],
          l,
          null
        ) : de(
          /*$$scope*/
          e[6]
        ),
        null
      );
    },
    i(e) {
      o || (E(r, e), o = !0);
    },
    o(e) {
      S(r, e), o = !1;
    },
    d(e) {
      e && g(n), r && r.d(e), t[9](null);
    }
  };
}
function ve(t) {
  let n, o, s, r, e = (
    /*$$slots*/
    t[4].default && T(t)
  );
  return {
    c() {
      n = q("react-portal-target"), o = he(), e && e.c(), s = F(), this.h();
    },
    l(l) {
      n = U(l, "REACT-PORTAL-TARGET", {
        class: !0
      }), G(n).forEach(g), o = ce(l), e && e.l(l), s = F(), this.h();
    },
    h() {
      H(n, "class", "svelte-1rt0kpf");
    },
    m(l, c) {
      y(l, n, c), t[8](n), y(l, o, c), e && e.m(l, c), y(l, s, c), r = !0;
    },
    p(l, [c]) {
      /*$$slots*/
      l[4].default ? e ? (e.p(l, c), c & /*$$slots*/
      16 && E(e, 1)) : (e = T(l), e.c(), E(e, 1), e.m(s.parentNode, s)) : e && (_e(), S(e, 1, 1, () => {
        e = null;
      }), ie());
    },
    i(l) {
      r || (E(e), r = !0);
    },
    o(l) {
      S(e), r = !1;
    },
    d(l) {
      l && (g(n), g(o), g(s)), t[8](null), e && e.d(l);
    }
  };
}
function N(t) {
  const {
    svelteInit: n,
    ...o
  } = t;
  return o;
}
function Ce(t, n, o) {
  let s, r, {
    $$slots: e = {},
    $$scope: l
  } = n;
  const c = ae(e);
  let {
    svelteInit: i
  } = n;
  const m = b(N(n)), d = b();
  P(t, d, (u) => o(0, s = u));
  const _ = b();
  P(t, _, (u) => o(1, r = u));
  const a = [], f = be("$$ms-gr-react-wrapper"), {
    slotKey: p,
    slotIndex: w,
    subSlotIndex: K
  } = $() || {}, B = i({
    parent: f,
    props: m,
    target: d,
    slot: _,
    slotKey: p,
    slotIndex: w,
    subSlotIndex: K,
    onDestroy(u) {
      a.push(u);
    }
  });
  Ee("$$ms-gr-react-wrapper", B), we(() => {
    m.set(N(n));
  }), ye(() => {
    a.forEach((u) => u());
  });
  function J(u) {
    O[u ? "unshift" : "push"](() => {
      s = u, d.set(s);
    });
  }
  function V(u) {
    O[u ? "unshift" : "push"](() => {
      r = u, _.set(r);
    });
  }
  return t.$$set = (u) => {
    o(17, n = k(k({}, n), L(u))), "svelteInit" in u && o(5, i = u.svelteInit), "$$scope" in u && o(6, l = u.$$scope);
  }, n = L(n), [s, r, d, _, c, i, l, e, J, V];
}
class Re extends le {
  constructor(n) {
    super(), pe(this, n, Ce, ve, me, {
      svelteInit: 5
    });
  }
}
const j = window.ms_globals.rerender, C = window.ms_globals.tree;
function Se(t) {
  function n(o) {
    const s = b(), r = new Re({
      ...o,
      props: {
        svelteInit(e) {
          window.ms_globals.autokey += 1;
          const l = {
            key: window.ms_globals.autokey,
            svelteInstance: s,
            reactComponent: t,
            props: e.props,
            slot: e.slot,
            target: e.target,
            slotIndex: e.slotIndex,
            subSlotIndex: e.subSlotIndex,
            slotKey: e.slotKey,
            nodes: []
          }, c = e.parent ?? C;
          return c.nodes = [...c.nodes, l], j({
            createPortal: R,
            node: C
          }), e.onDestroy(() => {
            c.nodes = c.nodes.filter((i) => i.svelteInstance !== s), j({
              createPortal: R,
              node: C
            });
          }), l;
        },
        ...o.props
      }
    });
    return s.set(r), r;
  }
  return new Promise((o) => {
    window.ms_globals.initializePromise.then(() => {
      o(n);
    });
  });
}
function Ie(t) {
  try {
    return typeof t == "string" ? new Function(`return (...args) => (${t})(...args)`)() : void 0;
  } catch {
    return;
  }
}
function A(t) {
  return Y(() => Ie(t), [t]);
}
const xe = ["animationIterationCount", "borderImageOutset", "borderImageSlice", "borderImageWidth", "boxFlex", "boxFlexGroup", "boxOrdinalGroup", "columnCount", "columns", "flex", "flexGrow", "flexPositive", "flexShrink", "flexNegative", "flexOrder", "gridArea", "gridColumn", "gridColumnEnd", "gridColumnStart", "gridRow", "gridRowEnd", "gridRowStart", "lineClamp", "lineHeight", "opacity", "order", "orphans", "tabSize", "widows", "zIndex", "zoom", "fontWeight", "letterSpacing", "lineHeight"];
function ke(t) {
  return t ? Object.keys(t).reduce((n, o) => {
    const s = t[o];
    return typeof s == "number" && !xe.includes(o) ? n[o] = s + "px" : n[o] = s, n;
  }, {}) : {};
}
function I(t) {
  const n = [], o = t.cloneNode(!1);
  if (t._reactElement)
    return n.push(R(h.cloneElement(t._reactElement, {
      ...t._reactElement.props,
      children: h.Children.toArray(t._reactElement.props.children).map((r) => {
        if (h.isValidElement(r) && r.props.__slot__) {
          const {
            portals: e,
            clonedElement: l
          } = I(r.props.el);
          return h.cloneElement(r, {
            ...r.props,
            el: l,
            children: [...h.Children.toArray(r.props.children), ...e]
          });
        }
        return null;
      })
    }), o)), {
      clonedElement: o,
      portals: n
    };
  Object.keys(t.getEventListeners()).forEach((r) => {
    t.getEventListeners(r).forEach(({
      listener: l,
      type: c,
      useCapture: i
    }) => {
      o.addEventListener(c, l, i);
    });
  });
  const s = Array.from(t.childNodes);
  for (let r = 0; r < s.length; r++) {
    const e = s[r];
    if (e.nodeType === 1) {
      const {
        clonedElement: l,
        portals: c
      } = I(e);
      n.push(...c), o.appendChild(l);
    } else e.nodeType === 3 && o.appendChild(e.cloneNode());
  }
  return {
    clonedElement: o,
    portals: n
  };
}
function Oe(t, n) {
  t && (typeof t == "function" ? t(n) : t.current = n);
}
const Pe = Q(({
  slot: t,
  clone: n,
  className: o,
  style: s
}, r) => {
  const e = X(), [l, c] = Z([]);
  return D(() => {
    var _;
    if (!e.current || !t)
      return;
    let i = t;
    function m() {
      let a = i;
      if (i.tagName.toLowerCase() === "svelte-slot" && i.children.length === 1 && i.children[0] && (a = i.children[0], a.tagName.toLowerCase() === "react-portal-target" && a.children[0] && (a = a.children[0])), Oe(r, a), o && a.classList.add(...o.split(" ")), s) {
        const f = ke(s);
        Object.keys(f).forEach((p) => {
          a.style[p] = f[p];
        });
      }
    }
    let d = null;
    if (n && window.MutationObserver) {
      let a = function() {
        var w;
        const {
          portals: f,
          clonedElement: p
        } = I(t);
        i = p, c(f), i.style.display = "contents", m(), (w = e.current) == null || w.appendChild(i);
      };
      a(), d = new window.MutationObserver(() => {
        var f, p;
        (f = e.current) != null && f.contains(i) && ((p = e.current) == null || p.removeChild(i)), a();
      }), d.observe(t, {
        attributes: !0,
        childList: !0,
        subtree: !0
      });
    } else
      i.style.display = "contents", m(), (_ = e.current) == null || _.appendChild(i);
    return () => {
      var a, f;
      i.style.display = "", (a = e.current) != null && a.contains(i) && ((f = e.current) == null || f.removeChild(i)), d == null || d.disconnect();
    };
  }, [t, n, o, s, r]), h.createElement("react-child", {
    ref: e,
    style: {
      display: "contents"
    }
  }, ...l);
});
function Fe(t, n) {
  return t ? /* @__PURE__ */ z.jsx(Pe, {
    slot: t,
    clone: n == null ? void 0 : n.clone
  }) : null;
}
function Le({
  key: t,
  setSlotParams: n,
  slots: o
}, s) {
  return (...r) => (n(t, r), Fe(o[t], {
    clone: !0,
    ...s
  }));
}
const Ne = Se(({
  value: t,
  onValueChange: n,
  requiredMark: o,
  onValuesChange: s,
  feedbackIcons: r,
  setSlotParams: e,
  slots: l,
  ...c
}) => {
  const [i] = x.useForm(), m = A(r), d = A(o);
  return D(() => {
    i.setFieldsValue(t);
  }, [i, t]), /* @__PURE__ */ z.jsx(x, {
    ...c,
    initialValues: t,
    form: i,
    requiredMark: l.requiredMark ? Le({
      key: "requiredMark",
      setSlotParams: e,
      slots: l
    }) : o === "optional" ? o : d || o,
    feedbackIcons: m,
    onValuesChange: (_, a) => {
      n(a), s == null || s(_, a);
    }
  });
});
export {
  Ne as Form,
  Ne as default
};
