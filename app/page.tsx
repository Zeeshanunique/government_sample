'use client';

import { Card } from "@/components/ui/card";
import { Button } from "@/components/ui/button";
import { LanguageSwitcher } from "@/components/language-switcher";
import { translations, useLanguageStore } from "@/lib/i18n";
import { GovtLogo } from "@/components/govt-logo";
import { 
  Building2, 
  FileText, 
  IndianRupee, 
  UserCheck, 
  MessageSquare,
  ChevronRight,
  Facebook,
  Twitter,
  Youtube,
  Instagram,
  FileIcon,
  Download,
  Search
} from "lucide-react";
import { useRef, useEffect } from 'react';

function ServiceCard({ icon, title, description, onClick }: { 
  icon: React.ReactNode; 
  title: string;
  description: string;
  onClick: () => void;
}) {
  return (
    <Card className="p-6 text-center hover:shadow-lg transition-shadow cursor-pointer" onClick={onClick}>
      <div className="inline-block p-3 bg-blue-100 rounded-full mb-4">
        {icon}
      </div>
      <h3 className="font-semibold text-lg mb-2">{title}</h3>
      <p className="text-gray-600">{description}</p>
    </Card>
  );
}

function SchemeCard({ title, description, onClick }: {
  title: string;
  description: string;
  onClick: () => void;
}) {
  return (
    <Card className="p-6 hover:shadow-lg transition-shadow cursor-pointer" onClick={onClick}>
      <h3 className="font-semibold text-lg mb-2">{title}</h3>
      <p className="text-gray-600">{description}</p>
      <Button variant="link" className="mt-4 p-0">
        Learn More →
      </Button>
    </Card>
  );
}

function DocumentCard({ icon, title, description }: {
  icon: React.ReactNode;
  title: string;
  description: string;
}) {
  return (
    <Card className="p-6 hover:shadow-lg transition-shadow">
      <div className="flex items-start">
        <div className="p-3 bg-blue-100 rounded-full">
          {icon}
        </div>
        <div className="ml-4">
          <h3 className="font-semibold text-lg mb-2">{title}</h3>
          <p className="text-gray-600 mb-4">{description}</p>
          <Button variant="outline" size="sm" className="flex items-center gap-2">
            <Download className="h-4 w-4" />
            Download
          </Button>
        </div>
      </div>
    </Card>
  );
}

function UpdateCard({ date, title, description }: { 
  date: string; 
  title: string; 
  description: string;
}) {
  return (
    <Card className="p-6">
      <time className="text-sm text-gray-500">{date}</time>
      <h3 className="font-semibold text-lg mt-2">{title}</h3>
      <p className="text-gray-600 mt-2">{description}</p>
    </Card>
  );
}

export default function Home() {
  const { language } = useLanguageStore();
  const t = translations[language];
  
  const servicesRef = useRef<HTMLDivElement>(null);
  const schemesRef = useRef<HTMLDivElement>(null);
  const documentsRef = useRef<HTMLDivElement>(null);

  const scrollToSection = (sectionRef: React.RefObject<HTMLDivElement>) => {
    sectionRef.current?.scrollIntoView({ behavior: 'smooth' });
  };

  const handleServiceClick = (service: string) => {
    console.log(`Navigating to ${service} service`);
  };

  const handleSchemeClick = (scheme: string) => {
    console.log(`Navigating to ${scheme} scheme details`);
  };

  return (
    <div className="min-h-screen bg-gray-50">
      <header className="bg-white border-b sticky top-0 z-50">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="flex justify-between items-center h-16">
            <div className="flex items-center cursor-pointer">
              <GovtLogo className="h-12 w-auto" />
              <span className="ml-3 text-xl font-semibold">Digital India</span>
            </div>
            <LanguageSwitcher />
          </div>
        </div>
      </header>

      <nav className="bg-blue-700 text-white sticky top-16 z-40">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="flex space-x-8 h-12 items-center">
            <button
              className="hover:text-blue-200 transition-colors"
              onClick={() => window.scrollTo({ top: 0, behavior: 'smooth' })}
            >
              {t.nav.home}
            </button>
            <button
              className="hover:text-blue-200 transition-colors"
              onClick={() => scrollToSection(servicesRef)}
            >
              {t.nav.services}
            </button>
            <button
              className="hover:text-blue-200 transition-colors"
              onClick={() => scrollToSection(schemesRef)}
            >
              {t.nav.schemes}
            </button>
            <button
              className="hover:text-blue-200 transition-colors"
              onClick={() => scrollToSection(documentsRef)}
            >
              {t.nav.documents}
            </button>
            <button className="hover:text-blue-200 transition-colors">
              {t.nav.contact}
            </button>
          </div>
        </div>
      </nav>

      <div className="bg-[url('https://images.unsplash.com/photo-1598633689984-a477bec32705?auto=format&fit=crop&q=80')] bg-cover bg-center">
        <div className="bg-black/50 py-24">
          <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 text-center text-white">
            <h1 className="text-4xl font-bold mb-4">{t.hero.welcome}</h1>
            <p className="text-xl mb-8">{t.hero.subtitle}</p>
            <Button 
              size="lg" 
              className="bg-blue-600 hover:bg-blue-700"
              onClick={() => scrollToSection(servicesRef)}
            >
              {t.hero.cta}
            </Button>
          </div>
        </div>
      </div>

      <div ref={servicesRef} className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-16">
        <h2 className="text-3xl font-bold text-center mb-12">{t.services.title}</h2>
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-8">
          <ServiceCard 
            icon={<FileText />} 
            title={t.services.certificates.title}
            description={t.services.certificates.description}
            onClick={() => handleServiceClick('certificates')}
          />
          <ServiceCard 
            icon={<IndianRupee />} 
            title={t.services.payments.title}
            description={t.services.payments.description}
            onClick={() => handleServiceClick('payments')}
          />
          <ServiceCard 
            icon={<UserCheck />} 
            title={t.services.registration.title}
            description={t.services.registration.description}
            onClick={() => handleServiceClick('registration')}
          />
          <ServiceCard 
            icon={<MessageSquare />} 
            title={t.services.grievances.title}
            description={t.services.grievances.description}
            onClick={() => handleServiceClick('grievances')}
          />
        </div>
      </div>

      <div ref={schemesRef} className="bg-blue-50 py-16">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <h2 className="text-3xl font-bold text-center mb-12">{t.schemes.title}</h2>
          <div className="grid grid-cols-1 md:grid-cols-3 gap-8">
            <SchemeCard
              title={t.schemes.digital_india.title}
              description={t.schemes.digital_india.description}
              onClick={() => handleSchemeClick('digital_india')}
            />
            <SchemeCard
              title={t.schemes.make_india.title}
              description={t.schemes.make_india.description}
              onClick={() => handleSchemeClick('make_india')}
            />
            <SchemeCard
              title={t.schemes.skill_india.title}
              description={t.schemes.skill_india.description}
              onClick={() => handleSchemeClick('skill_india')}
            />
          </div>
        </div>
      </div>

      <div ref={documentsRef} className="bg-white py-16">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <h2 className="text-3xl font-bold text-center mb-12">{t.documents.title}</h2>
          <div className="mb-8">
            <div className="max-w-md mx-auto">
              <div className="relative">
                <Search className="absolute left-3 top-1/2 transform -translate-y-1/2 text-gray-400" />
                <input
                  type="text"
                  placeholder={t.documents.searchPlaceholder}
                  className="w-full pl-10 pr-4 py-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500"
                />
              </div>
            </div>
          </div>
          <div className="grid grid-cols-1 gap-6">
            {t.documents.list.map((doc, index) => (
              <DocumentCard
                key={index}
                icon={<FileIcon />}
                title={doc.title}
                description={doc.description}
              />
            ))}
          </div>
        </div>
      </div>

      <div className="bg-gray-50 py-16">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="flex justify-between items-center mb-8">
            <h2 className="text-3xl font-bold">{t.updates.title}</h2>
            <Button variant="outline" className="flex items-center gap-2">
              {t.updates.viewAll}
              <ChevronRight className="h-4 w-4" />
            </Button>
          </div>
          <div className="grid grid-cols-1 md:grid-cols-3 gap-8">
            <UpdateCard
              date="2024-03-20"
              title="COVID-19 Vaccination Drive"
              description="Phase 4 of vaccination drive starts next week"
            />
            <UpdateCard
              date="2024-03-19"
              title="Digital Literacy Program"
              description="New centers opened in rural areas"
            />
            <UpdateCard
              date="2024-03-18"
              title="G20 Summit Preparations"
              description="India to host upcoming G20 summit"
            />
          </div>
        </div>
      </div>

      <footer className="bg-gray-900 text-white py-12">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="grid grid-cols-1 md:grid-cols-4 gap-8">
            <div>
              <GovtLogo className="h-12 w-auto mb-4" />
              <p className="text-gray-400">{t.footer.ministry}</p>
            </div>
            <div>
              <h3 className="font-semibold mb-4">{t.footer.quickLinks}</h3>
              <ul className="space-y-2 text-gray-400">
                <li>{t.services.certificates.title}</li>
                <li>{t.services.payments.title}</li>
                <li>{t.services.registration.title}</li>
              </ul>
            </div>
            <div>
              <h3 className="font-semibold mb-4">{t.footer.helpfulResources}</h3>
              <ul className="space-y-2 text-gray-400">
                <li>{t.schemes.digital_india.title}</li>
                <li>{t.schemes.make_india.title}</li>
                <li>{t.schemes.skill_india.title}</li>
              </ul>
            </div>
            <div>
              <h3 className="font-semibold mb-4">{t.footer.socialMedia}</h3>
              <div className="flex space-x-4">
                <Facebook className="h-6 w-6 text-gray-400 hover:text-white cursor-pointer" />
                <Twitter className="h-6 w-6 text-gray-400 hover:text-white cursor-pointer" />
                <Youtube className="h-6 w-6 text-gray-400 hover:text-white cursor-pointer" />
                <Instagram className="h-6 w-6 text-gray-400 hover:text-white cursor-pointer" />
              </div>
            </div>
          </div>
          <div className="mt-8 pt-8 border-t border-gray-800 text-center text-gray-400">
            © 2024 {t.footer.rights}
          </div>
        </div>
      </footer>
    </div>
  );
}