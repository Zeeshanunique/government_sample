import { create } from 'zustand';

type Language = 'en' | 'hi';

interface LanguageStore {
  language: Language;
  setLanguage: (lang: Language) => void;
}

export const useLanguageStore = create<LanguageStore>((set) => ({
  language: 'en',
  setLanguage: (lang) => set({ language: lang }),
}));

export const translations = {
  en: {
    nav: {
      home: 'Home',
      services: 'Services',
      schemes: 'Schemes',
      documents: 'Documents',
      contact: 'Contact',
    },
    hero: {
      welcome: 'Welcome to Digital India Portal',
      subtitle: 'Empowering citizens through digital transformation',
      cta: 'Explore Services',
    },
    services: {
      title: 'Our Services',
      certificates: {
        title: 'Certificates',
        description: 'Apply for birth, death, income, and residence certificates online',
      },
      payments: {
        title: 'Online Payments',
        description: 'Pay utility bills, taxes, and other government fees securely',
      },
      registration: {
        title: 'Registration',
        description: 'Register for various government schemes and services',
      },
      grievances: {
        title: 'Grievance Redressal',
        description: 'Submit and track your grievances online',
      },
    },
    schemes: {
      title: 'Popular Schemes',
      digital_india: {
        title: 'Digital India',
        description: 'Transforming India into a digitally empowered society and knowledge economy',
      },
      make_india: {
        title: 'Make in India',
        description: 'Encouraging companies to manufacture their products in India',
      },
      skill_india: {
        title: 'Skill India',
        description: 'Training over 40 crore people in different skills by 2022',
      },
    },
    documents: {
      title: 'Important Documents',
      searchPlaceholder: 'Search for documents...',
      list: [
        {
          title: 'Aadhaar Card Guidelines',
          description: 'Official guidelines for Aadhaar card application and usage',
        },
        {
          title: 'PAN Card Application',
          description: 'Documents and procedures for PAN card application',
        },
        {
          title: 'Voter ID Registration',
          description: 'Process and requirements for voter registration',
        },
        {
          title: 'Passport Application Guide',
          description: 'Step-by-step guide for passport application',
        },
      ],
    },
    updates: {
      title: 'Latest Updates',
      viewAll: 'View All Updates',
    },
    footer: {
      rights: 'All Rights Reserved',
      ministry: 'Ministry of Electronics & Information Technology',
      quickLinks: 'Quick Links',
      helpfulResources: 'Helpful Resources',
      socialMedia: 'Connect With Us',
    },
  },
  hi: {
    nav: {
      home: 'होम',
      services: 'सेवाएं',
      schemes: 'योजनाएं',
      documents: 'दस्तावेज़',
      contact: 'संपर्क',
    },
    hero: {
      welcome: 'डिजिटल इंडिया पोर्टल में आपका स्वागत है',
      subtitle: 'डिजिटल परिवर्तन के माध्यम से नागरिकों का सशक्तिकरण',
      cta: 'सेवाएं देखें',
    },
    services: {
      title: 'हमारी सेवाएं',
      certificates: {
        title: 'प्रमाणपत्र',
        description: 'जन्म, मृत्यु, आय और निवास प्रमाण पत्र के लिए ऑनलाइन आवेदन करें',
      },
      payments: {
        title: 'ऑनलाइन भुगतान',
        description: 'उपयोगिता बिल, कर और अन्य सरकारी शुल्क सुरक्षित रूप से भुगतान करें',
      },
      registration: {
        title: 'पंजीकरण',
        description: 'विभिन्न सरकारी योजनाओं और सेवाओं के लिए पंजीकरण करें',
      },
      grievances: {
        title: 'शिकायत निवारण',
        description: 'अपनी शिकायतें ऑनलाइन दर्ज करें और ट्रैक करें',
      },
    },
    schemes: {
      title: 'लोकप्रिय योजनाएं',
      digital_india: {
        title: 'डिजिटल इंडिया',
        description: 'भारत को डिजिटल रूप से सशक्त समाज और ज्ञान अर्थव्यवस्था में बदलना',
      },
      make_india: {
        title: 'मेक इन इंडिया',
        description: 'कंपनियों को भारत में अपने उत्पादों का निर्माण करने के लिए प्रोत्साहित करना',
      },
      skill_india: {
        title: 'स्किल इंडिया',
        description: '2022 तक विभिन्न कौशलों में 40 करोड़ से अधिक लोगों को प्रशिक्षित करना',
      },
    },
    documents: {
      title: 'महत्वपूर्ण दस्तावेज़',
      searchPlaceholder: 'दस्तावेज़ खोजें...',
      list: [
        {
          title: 'आधार कार्ड दिशानिर्देश',
          description: 'आधार कार्ड आवेदन और उपयोग के लिए आधिकारिक दिशानिर्देश',
        },
        {
          title: 'पैन कार्ड आवेदन',
          description: 'पैन कार्ड आवेदन के लिए दस्तावेज और प्रक्रियाएं',
        },
        {
          title: 'वोटर आईडी पंजीकरण',
          description: 'मतदाता पंजीकरण की प्रक्रिया और आवश्यकताएं',
        },
        {
          title: 'पासपोर्ट आवेदन गाइड',
          description: 'पासपोर्ट आवेदन के लिए चरण-दर-चरण गाइड',
        },
      ],
    },
    updates: {
      title: 'नवीनतम अपडेट',
      viewAll: 'सभी अपडेट देखें',
    },
    footer: {
      rights: 'सर्वाधिकार सुरक्षित',
      ministry: 'इलेक्ट्रॉनिक्स और सूचना प्रौद्योगिकी मंत्रालय',
      quickLinks: 'त्वरित लिंक',
      helpfulResources: 'सहायक संसाधन',
      socialMedia: 'हमसे जुड़ें',
    },
  },
};