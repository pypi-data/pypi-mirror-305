const dom = {
get: function(id) { return document.getElementById(id) },
elt(tag,style,attrs,html) { const e = document.createElement(tag); e.style.cssText = style; if (attrs) { for (const k in attrs) { e.setAttribute(k, attrs[k]);}}; if (html) e.innerHTML=html; return e; },
elt_p(parent,tag,style,attrs,html) { const e = this.elt(tag,style,attrs,html); if (parent) parent.appendChild(e); return e; },
div(style,attrs,html) { return this.elt('div',style,attrs,html); },
div_p(parent,style,attrs,html) { return this.elt_p(parent,'div',style,attrs,html); },
tree(parent, data, out) {
    if (!data) return;
    const e = this.elt_p(parent, data.tag, data.style, data.attrs, data.html);
    if (data.out) out[data.out] = e;
    if (data.children) {
        for (const i in data.children) { this.tree(e, data.children[i], out) }
    }
},
tree_o(parent, data) { const out={} ; this.tree(parent, data, out); return out; },
getRadio(form,name) { return document.forms[form].elements[name].value },
}