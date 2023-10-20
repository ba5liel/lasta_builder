import core

# BASE_URL="."
BASE_URL="http://localhost/lasta.digital/lasta.digital"
# BASE_URL="https://lasta.digital"

HEADER = f""" <header class="header header-transparent" data-track-source="Header">
        <div class="container header-container" data-nosnippet>
            <!--[if IE]><!-- zone: header --><!-- [endif] -->
<div class="header-row">
<div class="header-logo ">
<div class="header-logo-svg-wrapper">
    <div class="p-1">
    <a href="{BASE_URL}">
        <img style="width: 180px" src="https://lasta.digital/logos/logos-for-slider-with-content/lasta-logo-long-transparent.png">
    </a>
    </div>
</div>
</div>
<nav class="header-menu" data-track-source="Header menu" itemscope itemtype="https://schema.org/SiteNavigationElement" role="menu">
<div class="
                 header-menu-item
                                  has-sub-menu                                                                ">
<p class="header-menu-item-label js-track-click" data-track-element="item">
About
</p>
<div class="header-sub-menu d-none">
<div class="container header-sub-menu-container">

    <div class="header-sub-menu-intro-column col-3 ">
<p class="header-sub-menu-intro-column-title">
Our Company
</p>
<p class="header-sub-menu-intro-column-text">
Established in 2018, Lasta Digital is a transformative force in the software development industry, offering high-quality, affordable solutions through Agile methodology, clear communication, comprehensive analysis, and a commitment to innovation, all aimed at unlocking opportunities for diverse businesses worldwide. 
</p>
</div>
<div class="header-sub-menu-columns columns-5">
<div class="header-sub-menu-column">
<p class="header-sub-menu-title"></p>
<div class="header-sub-menu-link ">
<a href="{BASE_URL}/about/company.html" class="js-track-click" itemprop="url">
<span itemprop="name">About Company</span>
</a>
</div>

<div class="header-sub-menu-link ">
<a href="{BASE_URL}/case-studies.html" class="js-track-click" itemprop="url">
<span itemprop="name">Portfolio</span>
</a>
</div>

</div>
<div class="header-sub-menu-close-btn js-track-click" data-track-element="button" data-track-text="Close"></div>
</div>

    </div>
</div>
</div>
<div class="
                 header-menu-item
                                  has-sub-menu                                                                ">
<p class="header-menu-item-label js-track-click" data-track-element="item">
Approach
</p>
<div class="header-sub-menu d-none">
<div class="container header-sub-menu-container">
<div class="header-sub-menu-intro-column col-3 ">
<p class="header-sub-menu-intro-column-title">
Our Agile Approach
</p>
<p class="header-sub-menu-intro-column-text">
At Lasta Digital, our methodology is deeply rooted in Agile principles, ensuring adaptability, continuous improvement, and customer satisfaction. We embrace an iterative approach, allowing for flexibility and responsiveness to changes, fostering a collaborative environment where communication and feedback are paramount. 
</p>
</div>
<div class="header-sub-menu-columns columns-5">
<div class="header-sub-menu-column">

<div class="header-sub-menu-column">
<p class="header-sub-menu-title"></p>

<div class="header-sub-menu-link ">
<a href="{BASE_URL}/how-we-work/development-process.html" class="js-track-click" itemprop="url">
<span itemprop="name">Development Process</span>
</a>
</div>
<div class="header-sub-menu-link ">
<a href="{BASE_URL}/about/ux.html" class="js-track-click" itemprop="url">
<span itemprop="name">Our Approach to UX Design</span>
</a>
</div>
<div class="header-sub-menu-link ">
<a href="{BASE_URL}/about/ui.html" class="js-track-click" itemprop="url">
<span itemprop="name">Our Approach to UI Design</span>
</a>
</div>
<div class="header-sub-menu-link ">
<a href="{BASE_URL}/about/security-management.html" class="js-track-click" itemprop="url">
<span itemprop="name">Security Management </span>
</a>
</div>
<div class="header-sub-menu-link ">
<a href="{BASE_URL}/about/quality-management.html" class="js-track-click" itemprop="url">
<span itemprop="name">Quality Management</span>
</a>
</div>

<div class="header-sub-menu-link ">
<a href="{BASE_URL}/about/estimate.html" class="js-track-click" itemprop="url">
<span itemprop="name">Our Estimation Practices</span>
</a>
</div>

</div>

</div>
<div class="header-sub-menu-close-btn js-track-click" data-track-element="button" data-track-text="Close"></div>
</div>

    </div>
</div>
</div>
<div class="
                 header-menu-item
                                  has-sub-menu                                                                ">
<p class="header-menu-item-label js-track-click" data-track-element="item">
Services
</p>
<div class="header-sub-menu d-none">
<div class="container header-sub-menu-container">
<div class="header-sub-menu-intro-column col-3 ">
<p class="header-sub-menu-intro-column-title">
Services
</p>
<p class="header-sub-menu-intro-column-text">
Our service portfolio covers an entire software development life cycle and meets varied business needs.
</p>
</div>
<div class="header-sub-menu-columns columns-2">
<div class="header-sub-menu-column">
<div class="header-sub-menu-link ">
<a href="{BASE_URL}/services/software-development.html" class="js-track-click" itemprop="url">
<span itemprop="name">Software Development</span>
</a>
</div>
<div class="header-sub-menu-link ">
<a href="{BASE_URL}/services/web-development.html" class="js-track-click" itemprop="url">
<span itemprop="name">Web Development</span>
</a>
</div>
<div class="header-sub-menu-link ">
<a href="{BASE_URL}/services/mobile-app-development.html" class="js-track-click" itemprop="url">
<span itemprop="name">Mobile App Development</span>
</a>
</div>
<div class="header-sub-menu-link ">
<a href="{BASE_URL}/software-testing.html" class="js-track-click" itemprop="url">
<span itemprop="name">Testing and QA</span>
</a>
</div>
<div class="header-sub-menu-link ">
<a href="{BASE_URL}/services/application.html" class="js-track-click" itemprop="url">
<span itemprop="name">Application Services</span>
</a>
</div>
<div class="header-sub-menu-link ">
<a href="{BASE_URL}/services/web-design.html" class="js-track-click" itemprop="url">
<span itemprop="name">UI/UX Design</span>
</a>
</div>
<div class="header-sub-menu-link ">
<a href="{BASE_URL}/services/it-infrastructure.html" class="js-track-click" itemprop="url">
<span itemprop="name">Infrastructure Services</span>
</a>
</div>
</div>
<div class="header-sub-menu-column">
<div class="header-sub-menu-link ">
<a href="{BASE_URL}/services/digital-transformation.html" class="js-track-click" itemprop="url">
<span itemprop="name">Digital Transformation</span>
</a>
</div>
<div class="header-sub-menu-link ">
<a href="{BASE_URL}/services/managed-it.html" class="js-track-click" itemprop="url">
<span itemprop="name">Managed IT Services</span>
</a>
</div>
<div class="header-sub-menu-link ">
<a href="{BASE_URL}/services/it-outsourcing.html" class="js-track-click" itemprop="url">
<span itemprop="name">IT Outsourcing</span>
</a>
</div>
<div class="header-sub-menu-link ">
<a href="{BASE_URL}/services/it-consulting.html" class="js-track-click" itemprop="url">
<span itemprop="name">IT Consulting</span>
</a>
</div>
<div class="header-sub-menu-link ">
<a href="{BASE_URL}/it-support.html" class="js-track-click" itemprop="url">
<span itemprop="name">IT Support</span>
</a>
</div>
<div class="header-sub-menu-link ">
<a href="{BASE_URL}/services/analytics.html" class="js-track-click" itemprop="url">
<span itemprop="name">Data Analytics</span>
</a>
</div>
<div class="header-sub-menu-link ">
<a href="{BASE_URL}/services/security.html" class="js-track-click" itemprop="url">
<span itemprop="name">Cybersecurity</span>
</a>
</div>
</div>
</div>
<div class="header-sub-menu-close-btn js-track-click" data-track-element="button" data-track-text="Close"></div>
</div>

    </div>
</div>

<div class="
                 header-menu-item
                                                                                                  ">
<a href="{BASE_URL}/case-studies.html" class="header-menu-item-label js-track-click" itemprop="url" data-track-element="item">
<span itemprop="name">Portfolio</span>
</a>
</div>
<div class="
                 header-menu-item
                                                                                                  ">
<a href="{BASE_URL}/pricing.html" class="header-menu-item-label js-track-click" itemprop="url" data-track-element="item">
<span itemprop="name">Pricing</span>
</a>
</div>
<div class="
                 header-menu-item
                                                                                                  ">
<a href="https://school.lasta.digital" class="header-menu-item-label js-track-click" itemprop="url" data-track-element="item">
<span itemprop="name">Lasta School</span>
</a>
</div>
<div class="header-menu-page-shadow d-none"></div>
</nav>
<a href="tel:+1 571 365 1523" class="header-phone" aria-label="Call Lasta Digital">
<i class="icon-s-phone-bordered"></i>
</a>

<div class="header-yellow-buttons" data-track-source="Header menu">
<div class="header-yellow-button">
<a href="{BASE_URL}/about/company/contact-us-discuss-your-needs.html" class="header-yellow-button-label js-track-click" data-track-element="item">
Inquire Now
</a>
</div>
</div>
<button class="header-burger-btn js-track-click" aria-label="Open mobile menu" data-track-source="Header mobile menu" data-track-text="Open mobile menu"></button>
</div>
<!--[if IE]><!-- ~zone: header --><!-- [endif] -->
</div>
<!--[if IE]><!-- zone: header_mobile --><!-- [endif] -->
<div class="header-menu-mobile d-none" data-nosnippet data-track-source="Header mobile menu">
<button class="header-menu-mobile-close-btn js-track-click" aria-label="Close mobile menu" data-track-text="Close mobile menu">
<i class="icon-s-close"></i>
</button>
<div class="header-menu-mobile-items" itemscope itemtype="https://schema.org/SiteNavigationElement" role="menu">
<div class="
                     header-menu-mobile-item
                                                               has-sub-menu                     js-track-click
                 " data-track-element="item" data-track-text="About" data-track-event="Open/close sub menu">
<p class="header-menu-mobile-item-label">About</p>
<div class="header-sub-menu-mobile">
<div class="header-sub-menu-mobile-item">
<p class="header-sub-menu-mobile-title"></p>
</div>
<div class="header-sub-menu-mobile-item">
<a href="{BASE_URL}/about/company.html" class="header-sub-menu-mobile-link js-track-click " itemprop="url">
<span itemprop="name">About Company</span>
</a>
</div>
    
<div class="header-sub-menu-mobile-item">
<a href="{BASE_URL}/case-studies.html" class="header-sub-menu-mobile-link js-track-click " itemprop="url">
<span itemprop="name">Portfolio</span>
</a>
</div>
 
</div>
</div>
   <div class="
                     header-menu-mobile-item
                                                               has-sub-menu                     js-track-click
                 " data-track-element="item" data-track-text="Approach" data-track-event="Open/close sub menu">
<p class="header-menu-mobile-item-label">Approach</p>
<div class="header-sub-menu-mobile">
<div class="header-sub-menu-mobile-item">
<p class="header-sub-menu-mobile-title"></p>
</div>

<div class="header-sub-menu-mobile-item">
<a href="{BASE_URL}/how-we-work/development-process.html" class="header-sub-menu-mobile-link js-track-click " itemprop="url">
<span itemprop="name">Development Process</span>
</a>
</div>
<div class="header-sub-menu-mobile-item">
<a href="{BASE_URL}/about/ux.html" class="header-sub-menu-mobile-link js-track-click " itemprop="url">
<span itemprop="name">Our Approach to UX Design</span>
</a>
</div>
<div class="header-sub-menu-mobile-item">
<a href="{BASE_URL}/about/ui.html" class="header-sub-menu-mobile-link js-track-click " itemprop="url">
<span itemprop="name">Our Approach to UI Design</span>
</a>
</div>
<div class="header-sub-menu-mobile-item">
<a href="{BASE_URL}/about/security-management.html" class="header-sub-menu-mobile-link js-track-click " itemprop="url">
<span itemprop="name">Security Management </span>
</a>
</div>
<div class="header-sub-menu-mobile-item">
<a href="{BASE_URL}/about/quality-management.html" class="header-sub-menu-mobile-link js-track-click " itemprop="url">
<span itemprop="name">Quality Management</span>
</a>
</div>

<div class="header-sub-menu-mobile-item">
<a href="{BASE_URL}/about/estimate.html" class="header-sub-menu-mobile-link js-track-click " itemprop="url">
<span itemprop="name">Our Estimation Practices</span>
</a>
</div>

</div>
</div>
<div class="
                     header-menu-mobile-item
                                                               has-sub-menu                     js-track-click
                 " data-track-element="item" data-track-text="Services" data-track-event="Open/close sub menu">
<p class="header-menu-mobile-item-label">Services</p>
<div class="header-sub-menu-mobile">
<div class="header-sub-menu-mobile-item">
<a href="{BASE_URL}/services/software-development.html" class="header-sub-menu-mobile-link js-track-click " itemprop="url">
<span itemprop="name">Software Development</span>
</a>
</div>
<div class="header-sub-menu-mobile-item">
<a href="{BASE_URL}/services/web-development.html" class="header-sub-menu-mobile-link js-track-click " itemprop="url">
<span itemprop="name">Web Development</span>
</a>
</div>
<div class="header-sub-menu-mobile-item">
<a href="{BASE_URL}/services/mobile-app-development.html" class="header-sub-menu-mobile-link js-track-click " itemprop="url">
<span itemprop="name">Mobile App Development</span>
</a>
</div>
<div class="header-sub-menu-mobile-item">
<a href="{BASE_URL}/software-testing.html" class="header-sub-menu-mobile-link js-track-click " itemprop="url">
<span itemprop="name">Testing and QA</span>
</a>
</div>

<div class="header-sub-menu-mobile-item">
<a href="{BASE_URL}/services/web-design.html" class="header-sub-menu-mobile-link js-track-click " itemprop="url">
<span itemprop="name">UI/UX Design</span>
</a>
</div>

<div class="header-sub-menu-mobile-item">
<a href="{BASE_URL}/services/it-outsourcing.html" class="header-sub-menu-mobile-link js-track-click " itemprop="url">
<span itemprop="name">IT Outsourcing</span>
</a>
</div>

<div class="header-sub-menu-mobile-item">
<a href="{BASE_URL}/it-support.html" class="header-sub-menu-mobile-link js-track-click " itemprop="url">
<span itemprop="name">IT Support</span>
</a>
</div>
    <div class="header-sub-menu-mobile-item">
<a href="https://school.lasta.digital" class="header-sub-menu-mobile-link js-track-click " itemprop="url">
<span itemprop="name">Lasta School</span>
</a>
</div>

</div>
</div>

<div class="
                     header-menu-mobile-item
                                                                                    js-track-click
                 " data-track-element="item" data-track-text="Portfolio">
<a href="{BASE_URL}/case-studies.html" class="header-menu-mobile-item-label " itemprop="url">
<span itemprop="name">Portfolio</span>
</a>
</div>
<div class="
                     header-menu-mobile-item
                                                                                    js-track-click
                 " data-track-element="item" data-track-text="Lasta School">
<a href="https://school.lasta.digital" target="_blank" class="header-menu-mobile-item-label " itemprop="url">
<span itemprop="name">Lasta School</span>
</a>
</div>
<div class="
                     header-menu-mobile-item
                                                                                    js-trackclick
                 " data-track-element="item" data-track-text="Pricing">
<a href="{BASE_URL}/pricing.html" class="header-menu-mobile-item-label " itemprop="url">
<span itemprop="name">Pricing</span>
</a>
</div>

<div class="
                     header-menu-mobile-item
                     header-yellow-button                                                               js-track-click
                 " data-track-element="item" data-track-text="Inquire Now">
<a href="{BASE_URL}/about/company/contact-us-discuss-your-needs.html" class="header-menu-mobile-item-label header-yellow-button-label" itemprop="url">
<span itemprop="name">Inquire Now</span>
</a>
</div>
<div class="header-menu-mobile-contacts">
<a href="tel:+1 214 306 68 37" class="header-menu-mobile-phone">
<i class="icon-s-phone-bordered"></i>
<span class="header-menu-mobile-phone-text" dir="ltr">+1 571 365 1523</span>
</a>
<a href="mailto:contact@lasta.digital" class="header-menu-mobile-email">
<i class="icon-s-envelope"></i>
<span class="header-menu-mobile-email-text" dir="ltr">contact@lasta.digital</span>
</a>
</div>
  </div>
</div>
<div class="header-menu-mobile-shadow d-none js-track-click" data-track-source="Header mobile menu" data-track-element="button" data-track-text="Close mobile menu"></div>
<!--[if IE]><!-- ~zone: header_mobile --><!-- [endif] -->
</header>"""

HEADER_SERVICE_OUT = f""" <header class="header header-transparent" data-track-source="Header">
        <div class="container header-container" data-nosnippet>
            <!--[if IE]><!-- zone: header --><!-- [endif] -->
<div class="header-row">
<div class="header-logo ">
<div class="header-logo-svg-wrapper">
    <div class="p-1">
    <a href="{BASE_URL}">
        <img style="width: 180px" src="https://lasta.digital/logos/logos-for-slider-with-content/lasta-logo-long-transparent.png">
    </a>
    </div>
</div>
</div>
<nav class="header-menu" data-track-source="Header menu" itemscope itemtype="https://schema.org/SiteNavigationElement" role="menu">
<div class="
                 header-menu-item
                                  has-sub-menu                                                                ">
<p class="header-menu-item-label js-track-click" data-track-element="item">
About
</p>
<div class="header-sub-menu d-none">
<div class="container header-sub-menu-container">

    <div class="header-sub-menu-intro-column col-3 ">
<p class="header-sub-menu-intro-column-title">
Our Company
</p>
<p class="header-sub-menu-intro-column-text">
Established in 2018, Lasta Digital is a transformative force in the software development industry, offering high-quality, affordable solutions through Agile methodology, clear communication, comprehensive analysis, and a commitment to innovation, all aimed at unlocking opportunities for diverse businesses worldwide. 
</p>
</div>
<div class="header-sub-menu-columns columns-5">
<div class="header-sub-menu-column">
<p class="header-sub-menu-title"></p>
<div class="header-sub-menu-link ">
<a href="{BASE_URL}/about/company.html" class="js-track-click" itemprop="url">
<span itemprop="name">About Company</span>
</a>
</div>

<div class="header-sub-menu-link ">
<a href="{BASE_URL}/case-studies.html" class="js-track-click" itemprop="url">
<span itemprop="name">Portfolio</span>
</a>
</div>

</div>
<div class="header-sub-menu-close-btn js-track-click" data-track-element="button" data-track-text="Close"></div>
</div>

    </div>
</div>
</div>
<div class="
                 header-menu-item
                                  has-sub-menu                                                                ">
<p class="header-menu-item-label js-track-click" data-track-element="item">
Approach
</p>
<div class="header-sub-menu d-none">
<div class="container header-sub-menu-container">
<div class="header-sub-menu-intro-column col-3 ">
<p class="header-sub-menu-intro-column-title">
Our Agile Approach
</p>
<p class="header-sub-menu-intro-column-text">
At Lasta Digital, our methodology is deeply rooted in Agile principles, ensuring adaptability, continuous improvement, and customer satisfaction. We embrace an iterative approach, allowing for flexibility and responsiveness to changes, fostering a collaborative environment where communication and feedback are paramount. 
</p>
</div>
<div class="header-sub-menu-columns columns-5">
<div class="header-sub-menu-column">

<div class="header-sub-menu-column">
<p class="header-sub-menu-title"></p>

<div class="header-sub-menu-link ">
<a href="{BASE_URL}/how-we-work/development-process.html" class="js-track-click" itemprop="url">
<span itemprop="name">Development Process</span>
</a>
</div>
<div class="header-sub-menu-link ">
<a href="{BASE_URL}/about/ux.html" class="js-track-click" itemprop="url">
<span itemprop="name">Our Approach to UX Design</span>
</a>
</div>
<div class="header-sub-menu-link ">
<a href="{BASE_URL}/about/ui.html" class="js-track-click" itemprop="url">
<span itemprop="name">Our Approach to UI Design</span>
</a>
</div>
<div class="header-sub-menu-link ">
<a href="{BASE_URL}/about/security-management.html" class="js-track-click" itemprop="url">
<span itemprop="name">Security Management </span>
</a>
</div>
<div class="header-sub-menu-link ">
<a href="{BASE_URL}/about/quality-management.html" class="js-track-click" itemprop="url">
<span itemprop="name">Quality Management</span>
</a>
</div>

<div class="header-sub-menu-link ">
<a href="{BASE_URL}/about/estimate.html" class="js-track-click" itemprop="url">
<span itemprop="name">Our Estimation Practices</span>
</a>
</div>

</div>

</div>
<div class="header-sub-menu-close-btn js-track-click" data-track-element="button" data-track-text="Close"></div>
</div>

    </div>
</div>
</div>
<div class="
                 header-menu-item
                                  has-sub-menu                                                                ">
<p class="header-menu-item-label js-track-click" data-track-element="item">
Services
</p>
<div class="header-sub-menu d-none">
<div class="container header-sub-menu-container">
<div class="header-sub-menu-intro-column col-3 ">
<p class="header-sub-menu-intro-column-title">
Services
</p>
<p class="header-sub-menu-intro-column-text">
Our service portfolio covers an entire software development life cycle and meets varied business needs.
</p>
</div>
<div class="header-sub-menu-columns columns-2">
<div class="header-sub-menu-column">
<div class="header-sub-menu-link ">
<a href="javascript:void(0)" class="js-track-click" itemprop="url">
<span itemprop="name">Software Development</span>
</a>
</div>
<div class="header-sub-menu-link ">
<a href="javascript:void(0)" class="js-track-click" itemprop="url">
<span itemprop="name">Web Development</span>
</a>
</div>
<div class="header-sub-menu-link ">
<a href="javascript:void(0)" class="js-track-click" itemprop="url">
<span itemprop="name">Mobile App Development</span>
</a>
</div>
<div class="header-sub-menu-link ">
<a href="javascript:void(0)" class="js-track-click" itemprop="url">
<span itemprop="name">Testing and QA</span>
</a>
</div>
<div class="header-sub-menu-link ">
<a href="javascript:void(0)" class="js-track-click" itemprop="url">
<span itemprop="name">Application Services</span>
</a>
</div>
<div class="header-sub-menu-link ">
<a href="javascript:void(0)" class="js-track-click" itemprop="url">
<span itemprop="name">UI/UX Design</span>
</a>
</div>
<div class="header-sub-menu-link ">
<a href="javascript:void(0)" class="js-track-click" itemprop="url">
<span itemprop="name">Infrastructure Services</span>
</a>
</div>
</div>
<div class="header-sub-menu-column">
<div class="header-sub-menu-link ">
<a href="javascript:void(0)" class="js-track-click" itemprop="url">
<span itemprop="name">Digital Transformation</span>
</a>
</div>
<div class="header-sub-menu-link ">
<a href="javascript:void(0)" class="js-track-click" itemprop="url">
<span itemprop="name">Managed IT Services</span>
</a>
</div>
<div class="header-sub-menu-link ">
<a href="javascript:void(0)" class="js-track-click" itemprop="url">
<span itemprop="name">IT Outsourcing</span>
</a>
</div>
<div class="header-sub-menu-link ">
<a href="javascript:void(0)" class="js-track-click" itemprop="url">
<span itemprop="name">IT Consulting</span>
</a>
</div>
<div class="header-sub-menu-link ">
<a href="javascript:void(0)" class="js-track-click" itemprop="url">
<span itemprop="name">IT Support</span>
</a>
</div>
<div class="header-sub-menu-link ">
<a href="javascript:void(0)" class="js-track-click" itemprop="url">
<span itemprop="name">Data Analytics</span>
</a>
</div>
<div class="header-sub-menu-link ">
<a href="javascript:void(0)" class="js-track-click" itemprop="url">
<span itemprop="name">Cybersecurity</span>
</a>
</div>
</div>
</div>
<div class="header-sub-menu-close-btn js-track-click" data-track-element="button" data-track-text="Close"></div>
</div>

    </div>
</div>

<div class="
                 header-menu-item
                                                                                                  ">
<a href="{BASE_URL}/case-studies.html" class="header-menu-item-label js-track-click" itemprop="url" data-track-element="item">
<span itemprop="name">Portfolio</span>
</a>
</div>
<div class="
                 header-menu-item
                                                                                                  ">
<a href="{BASE_URL}/pricing.html" class="header-menu-item-label js-track-click" itemprop="url" data-track-element="item">
<span itemprop="name">Pricing</span>
</a>
</div>
<div class="
                 header-menu-item
                                                                                                  ">
<a href="https://school.lasta.digital" class="header-menu-item-label js-track-click" itemprop="url" data-track-element="item">
<span itemprop="name">Lasta School</span>
</a>
</div>
<div class="header-menu-page-shadow d-none"></div>
</nav>
<a href="tel:+1 571 365 1523" class="header-phone" aria-label="Call Lasta Digital">
<i class="icon-s-phone-bordered"></i>
</a>

<div class="header-yellow-buttons" data-track-source="Header menu">
<div class="header-yellow-button">
<a href="{BASE_URL}/about/company/contact-us-discuss-your-needs.html" class="header-yellow-button-label js-track-click" data-track-element="item">
Inquire Now
</a>
</div>
</div>
<button class="header-burger-btn js-track-click" aria-label="Open mobile menu" data-track-source="Header mobile menu" data-track-text="Open mobile menu"></button>
</div>
<!--[if IE]><!-- ~zone: header --><!-- [endif] -->
</div>
<!--[if IE]><!-- zone: header_mobile --><!-- [endif] -->
<div class="header-menu-mobile d-none" data-nosnippet data-track-source="Header mobile menu">
<button class="header-menu-mobile-close-btn js-track-click" aria-label="Close mobile menu" data-track-text="Close mobile menu">
<i class="icon-s-close"></i>
</button>
<div class="header-menu-mobile-items" itemscope itemtype="https://schema.org/SiteNavigationElement" role="menu">
<div class="
                     header-menu-mobile-item
                                                               has-sub-menu                     js-track-click
                 " data-track-element="item" data-track-text="About" data-track-event="Open/close sub menu">
<p class="header-menu-mobile-item-label">About</p>
<div class="header-sub-menu-mobile">
<div class="header-sub-menu-mobile-item">
<p class="header-sub-menu-mobile-title"></p>
</div>
<div class="header-sub-menu-mobile-item">
<a href="{BASE_URL}/about/company.html" class="header-sub-menu-mobile-link js-track-click " itemprop="url">
<span itemprop="name">About Company</span>
</a>
</div>
    
<div class="header-sub-menu-mobile-item">
<a href="{BASE_URL}/case-studies.html" class="header-sub-menu-mobile-link js-track-click " itemprop="url">
<span itemprop="name">Portfolio</span>
</a>
</div>
 
</div>
</div>
   <div class="
                     header-menu-mobile-item
                                                               has-sub-menu                     js-track-click
                 " data-track-element="item" data-track-text="Approach" data-track-event="Open/close sub menu">
<p class="header-menu-mobile-item-label">Approach</p>
<div class="header-sub-menu-mobile">
<div class="header-sub-menu-mobile-item">
<p class="header-sub-menu-mobile-title"></p>
</div>

<div class="header-sub-menu-mobile-item">
<a href="{BASE_URL}/how-we-work/development-process.html" class="header-sub-menu-mobile-link js-track-click " itemprop="url">
<span itemprop="name">Development Process</span>
</a>
</div>
<div class="header-sub-menu-mobile-item">
<a href="{BASE_URL}/about/ux.html" class="header-sub-menu-mobile-link js-track-click " itemprop="url">
<span itemprop="name">Our Approach to UX Design</span>
</a>
</div>
<div class="header-sub-menu-mobile-item">
<a href="{BASE_URL}/about/ui.html" class="header-sub-menu-mobile-link js-track-click " itemprop="url">
<span itemprop="name">Our Approach to UI Design</span>
</a>
</div>
<div class="header-sub-menu-mobile-item">
<a href="{BASE_URL}/about/security-management.html" class="header-sub-menu-mobile-link js-track-click " itemprop="url">
<span itemprop="name">Security Management </span>
</a>
</div>
<div class="header-sub-menu-mobile-item">
<a href="{BASE_URL}/about/quality-management.html" class="header-sub-menu-mobile-link js-track-click " itemprop="url">
<span itemprop="name">Quality Management</span>
</a>
</div>

<div class="header-sub-menu-mobile-item">
<a href="{BASE_URL}/about/estimate.html" class="header-sub-menu-mobile-link js-track-click " itemprop="url">
<span itemprop="name">Our Estimation Practices</span>
</a>
</div>

</div>
</div>
<div class="
                     header-menu-mobile-item
                                                               has-sub-menu                     js-track-click
                 " data-track-element="item" data-track-text="Services" data-track-event="Open/close sub menu">
<p class="header-menu-mobile-item-label">Services</p>
<div class="header-sub-menu-mobile">
<div class="header-sub-menu-mobile-item">
<a href="{BASE_URL}/services/software-development.html" class="header-sub-menu-mobile-link js-track-click " itemprop="url">
<span itemprop="name">Software Development</span>
</a>
</div>
<div class="header-sub-menu-mobile-item">
<a href="{BASE_URL}/services/web-development.html" class="header-sub-menu-mobile-link js-track-click " itemprop="url">
<span itemprop="name">Web Development</span>
</a>
</div>
<div class="header-sub-menu-mobile-item">
<a href="{BASE_URL}/services/mobile-app-development.html" class="header-sub-menu-mobile-link js-track-click " itemprop="url">
<span itemprop="name">Mobile App Development</span>
</a>
</div>
<div class="header-sub-menu-mobile-item">
<a href="{BASE_URL}/software-testing.html" class="header-sub-menu-mobile-link js-track-click " itemprop="url">
<span itemprop="name">Testing and QA</span>
</a>
</div>

<div class="header-sub-menu-mobile-item">
<a href="{BASE_URL}/services/web-design.html" class="header-sub-menu-mobile-link js-track-click " itemprop="url">
<span itemprop="name">UI/UX Design</span>
</a>
</div>

<div class="header-sub-menu-mobile-item">
<a href="{BASE_URL}/services/it-outsourcing.html" class="header-sub-menu-mobile-link js-track-click " itemprop="url">
<span itemprop="name">IT Outsourcing</span>
</a>
</div>

<div class="header-sub-menu-mobile-item">
<a href="{BASE_URL}/it-support.html" class="header-sub-menu-mobile-link js-track-click " itemprop="url">
<span itemprop="name">IT Support</span>
</a>
</div>
    <div class="header-sub-menu-mobile-item">
<a href="https://school.lasta.digital" class="header-sub-menu-mobile-link js-track-click " itemprop="url">
<span itemprop="name">Lasta School</span>
</a>
</div>

</div>
</div>

<div class="
                     header-menu-mobile-item
                                                                                    js-track-click
                 " data-track-element="item" data-track-text="Portfolio">
<a href="{BASE_URL}/case-studies.html" class="header-menu-mobile-item-label " itemprop="url">
<span itemprop="name">Portfolio</span>
</a>
</div>
<div class="
                     header-menu-mobile-item
                                                                                    js-track-click
                 " data-track-element="item" data-track-text="Lasta School">
<a href="https://school.lasta.digital" target="_blank" class="header-menu-mobile-item-label " itemprop="url">
<span itemprop="name">Lasta School</span>
</a>
</div>
<div class="
                     header-menu-mobile-item
                                                                                    js-trackclick
                 " data-track-element="item" data-track-text="Pricing">
<a href="{BASE_URL}/pricing.html" class="header-menu-mobile-item-label " itemprop="url">
<span itemprop="name">Pricing</span>
</a>
</div>

<div class="
                     header-menu-mobile-item
                     header-yellow-button                                                               js-track-click
                 " data-track-element="item" data-track-text="Inquire Now">
<a href="{BASE_URL}/about/company/contact-us-discuss-your-needs.html" class="header-menu-mobile-item-label header-yellow-button-label" itemprop="url">
<span itemprop="name">Inquire Now</span>
</a>
</div>
<div class="header-menu-mobile-contacts">
<a href="tel:+1 214 306 68 37" class="header-menu-mobile-phone">
<i class="icon-s-phone-bordered"></i>
<span class="header-menu-mobile-phone-text" dir="ltr">+1 571 365 1523</span>
</a>
<a href="mailto:contact@lasta.digital" class="header-menu-mobile-email">
<i class="icon-s-envelope"></i>
<span class="header-menu-mobile-email-text" dir="ltr">contact@lasta.digital</span>
</a>
</div>
  </div>
</div>
<div class="header-menu-mobile-shadow d-none js-track-click" data-track-source="Header mobile menu" data-track-element="button" data-track-text="Close mobile menu"></div>
<!--[if IE]><!-- ~zone: header_mobile --><!-- [endif] -->
</header>"""

if __name__ == "__main__":
    core.start('header', 'header', HEADER_SERVICE_OUT)
