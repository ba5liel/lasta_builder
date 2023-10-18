import core

FOOTER = """<footer class="footer" data-track-source="Footer">
<div class="footer-content">
<div class="container">
<div class="footer-row">
<div class="footer-logo">
<span class="footer-logo-img-wrapper">
<!-- <img width="200" height="40" class="lazy" src="data:image/svg+xml;base64,CiAgICAgICAgICAgIDxzdmcgeG1sbnM9J2h0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnJyB2aWV3Qm94PScwIDAgMjAwIDQwJz4KICAgICAgICAgICAgICAgIDxyZWN0IHdpZHRoPScyMDAnIGhlaWdodD0nNDAnIGZpbGw9JyNmMmYyZjInLz4KICAgICAgICAgICAgPC9zdmc+CiAgICAgICAg" data-src="/bundles/app/img/logo-footer.svg" alt="Lasta Digital footer icon"> -->
<img alt="Lasta Digital footer icon" class="lazy" data-src="" height="40" src="https://lasta.digital/logos/logos-for-slider-with-content/lasta-logo-long-white-transparent.png" width="200"/>
</span>
<div class="footer-socials">
<div class="footer-socials-links">
<a aria-label="Linkedin" class="footer-socials-links-linkedin js-track-click" data-track-text="Linkedin" href="https://www.linkedin.com/company/lastaDigital/" rel="noopener" target="_blank"></a>
<a aria-label="Twitter" class="footer-socials-links-twitter js-track-click" data-track-text="Twitter" href="https://twitter.com/LastaDigital" rel="noopener" target="_blank"></a>
<a aria-label="Facebook" class="footer-socials-links-facebook js-track-click" data-track-text="Facebook" href="https://www.facebook.com/lasta.digital/" rel="noopener" target="_blank"></a>
<a aria-label="Dribble" class="footer-socials-links-dribble js-track-click" data-track-text="Dribble" href="https://dribbble.com/lasta.digital" rel="noopener" target="_blank"></a>
</div>
</div>
</div>
<div class="footer-contacts addresses-count-1">
<div class="footer-contacts-rows">
<div class="footer-contacts-row">
<div class="footer-contacts-links">
<div class="footer-contacts-links-item">
<i class="icon-s-map-marker"></i>
<a class="footer-contacts-links-item-address-location js-track-click" href="https://goo.gl/maps/aGbrBRbct4eivFyV8" rel="noopener" target="_blank">
Alexandria, Virginia USA 
Addis Ababa Ethiopia
</a>
</div>
<div class="footer-contacts-links-item">
<i class="icon-s-envelope"></i>
<a class="footer-contacts-links-item-email js-track-click" dir="ltr" href="mailto:contact@lasta.digital" itemprop="email">
contact@lasta.digital
</a>
</div>
<div class="footer-contacts-links-item">
<i class="icon-s-phone"></i>
<div class="footer-contacts-links-item-phones">
<a class="footer-contacts-links-item-phone js-track-click" dir="ltr" href="tel:+1 571 365 1523" itemprop="telephone">
+1 571 365 1523
</a>
<a class="footer-contacts-links-item-phone js-track-click" dir="ltr" href="tel:+251 961 186 323" itemprop="telephone">
+251 961 186 323
</a>
</div>
</div>
<div class="footer-contacts-links-item footer-contacts-call">
<button class="footer-contacts-call-btn js-track-click" type="button">
Request a call
</button>
<div class="footer-contacts-call-tooltip">
<div class="footer-contacts-call-tooltip-content">
<p class="footer-contacts-call-tooltip-title">
Request a call
</p>
<button aria-label="Close request a call tooltip" class="footer-contacts-call-tooltip-close" type="button">
<i class="icon-s-close"></i>
</button>
<form action="https://www.scnsoft.com/form/footer-call-form" class="footer-contacts-call-tooltip-form" data-track-source="Footer: Request a call Form" enctype="multipart/form-data" method="post" name="Request a call Form">
<input autocomplete="nope" class="hp-field" name="hon_pot_fd" placeholder="Your hon pot fd" type="text"/>
<input name="piwikVisitorId" type="hidden">
<div class="form-element-wrapper form-input-wrapper">
<input autocomplete="tel" class="form-input js-track-change" data-custom-phone="" dir="ltr" id="input_phone_29" maxlength="70" name="phone" placeholder="Phone number" required="" type="tel"/>
<label class="form-element-label" for="input_phone_29">Phone number</label>
</div>
<button class="footer-contacts-call-tooltip-submit js-track-click" type="submit">
Send
</button>
<div class="footer-contacts-call-tooltip-submit-success">
<i class="icon-s-checkmark"></i>
</div>
</input></form>
</div>
</div>
<div class="footer-contacts-call-tooltip-ledge"></div> </div>
</div>
</div>
</div>
</div>
</div>
<div class="footer-row">
<div class="footer-links">
<div class="footer-links-item">
<a class="footer-links-item-a js-track-click" href="#">
About Lasta Digital
</a>
</div>

<div class="footer-links-item">
<a class="footer-links-item-a js-track-click" href="#">
Privacy Policy
</a>
</div>
<div class="footer-links-item">
<a class="footer-links-item-a js-track-click" href="#">
Terms of Use
</a>
</div>
</div>
</div>
<div class="footer-row">
<div class="footer-copyright">
<div class="footer-copyright-text">
<p class="footer-copyright-text-corporation">© 2023 Lasta Digital USA Corporation.</p>
<p>All rights reserved.</p>
</div>
</div>
</div>
</div>
<div class="footer-scripts">
<div class="pimcore_area_html-code pimcore_area_content">
<div class="" data-track-source="Editable: Html Code">
<div class="html-code-editable-wrapper">
</div>
</div>
</div>
</div></div></footer>"""

if __name__ == "__main__":
    core.start('footer', 'footer', FOOTER)
