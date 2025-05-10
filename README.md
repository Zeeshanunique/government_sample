# Government Sample Website

A comprehensive, modern, and accessible government website template built with Next.js and shadcn/ui components. This project serves as a reference implementation for government entities looking to modernize their digital presence while adhering to accessibility standards and providing a superior user experience.

## 🚀 Project Overview

This project demonstrates a modern approach to building government websites with a focus on:

- **User-Centric Design**: Prioritizing the citizen's needs with intuitive navigation and clear information architecture
- **Accessibility**: Ensuring the website is usable by people of all abilities in accordance with WCAG guidelines
- **Multilingual Support**: Built-in language switching capabilities to serve diverse populations
- **Responsive Design**: Optimized experience across all device types from mobile to desktop
- **Performance**: Fast loading times and optimized rendering for a smooth user experience
- **Dark/Light Mode**: Respect for user preferences with automatic and manual theme switching
- **Document Translation**: English to Hindi translation service for government documents

## 🌐 Document Translation Service

The project includes a powerful English-Hindi translation service specifically designed for government documents. This feature leverages a custom machine learning model trained on government terminology to provide accurate translations.

### Translation Features

- **Specialized for Government Documents**: Specifically trained on bureaucratic language and formal tone
- **Preserves Technical Terms**: Accurately translates specialized government terminology
- **User-friendly Interface**: Simple input/output design for ease of use
- **Customizable Model**: Trainable with domain-specific translation pairs
- **Self-hosted Solution**: No dependency on external APIs or services

### How To Use The Translation Service

1. **Start the Translation Server**:
   ```bash
   cd python-api
   pip install -r requirements.txt
   uvicorn main:app --reload
   ```

2. **Launch the Translation Interface**:
   ```bash
   cd python-api
   streamlit run app.py
   ```

3. **Translate Documents**:
   - Enter English text in the input field
   - Click "Translate" to get Hindi translation
   - Copy the translated text for use in documents

### Training The Translation Model

The translation system uses a custom model that can be trained with domain-specific terminology:

1. **Prepare Training Data**:
   - Create a CSV file with "english,hindi" columns
   - Add translation pairs relevant to your government domain
   - Alternatively, use the provided sample data in `govt_training_data.csv`

2. **Train the Model**:
   ```bash
   cd python-api
   python train_model.py
   ```

3. **Test Your Translation Quality**:
   - After training, the model will automatically test with some example phrases
   - Check translation quality and add more training data as needed

### Translation API Endpoints

For developers integrating the translation service:

- **POST /translate**: Translate English text to Hindi
  ```json
  {"text": "Your English text here", "preserve_formatting": true}
  ```

- **POST /train/add-data**: Add new training data pairs
  ```json
  {"training_pairs": [{"english": "English text", "hindi": "Hindi translation"}]}
  ```

- **GET /health**: Check API status and model information

## 🛠️ Technology Stack

### Core Technologies
- **Next.js 13.5**: Utilizing the App Router for improved routing and server components
- **TypeScript**: Full type safety throughout the application for more reliable code
- **React 18**: Leveraging the latest React features including concurrent rendering
- **Tailwind CSS**: Utility-first CSS framework for highly customizable and maintainable styling
- **FastAPI**: Backend API framework for the translation service
- **Streamlit**: User interface for the translation service
- **Custom ML Translation Model**: Lightweight machine learning model for government document translation

### UI Components and Styling
- **shadcn/ui**: High-quality, accessible, and customizable UI components
- **Radix UI**: Unstyled, accessible components as the foundation for shadcn/ui
- **Lucide Icons**: Consistent and beautiful SVG icons
- **Tailwind Merge**: Smart utility for merging Tailwind CSS classes
- **Class Variance Authority**: For creating variant components with type safety

### Form Handling and Validation
- **React Hook Form**: Efficient form management with minimal re-renders
- **Zod**: TypeScript-first schema validation with static type inference

### State Management
- **Zustand**: Lightweight state management solution with a simple API

### UI Enhancement
- **Next Themes**: Easy theme switching between light and dark modes
- **Tailwind Animate**: Tailwind plugin for animations
- **Sonner**: Toast notifications with minimal design
- **React Day Picker**: Flexible date picker component
- **Embla Carousel**: Extensible carousel component
- **cmdk**: Command menu component for keyboard-first interfaces
- **Vaul**: Drawer component for mobile interfaces

### Data Visualization
- **Recharts**: Composable charting library built on React components

### Development Tools
- **ESLint**: Linting to catch problems early
- **PostCSS**: For transforming CSS with JavaScript plugins
- **Autoprefixer**: Automatic vendor prefix handling

## 📋 Features

- **Modern Dashboard Layout**: Clean, intuitive dashboard for administrative functions
- **Service Catalog**: Organized presentation of government services
- **Interactive Forms**: User-friendly forms with validation for government applications and requests
- **News and Announcements Section**: Timely updates with filtering capabilities
- **Search Functionality**: Comprehensive site search for quick information access
- **User Authentication**: Secure login for accessing personalized services
- **Accessible UI Components**: All components meet WCAG accessibility standards
- **Responsive Navigation**: Adaptive navigation patterns for all screen sizes
- **Performance Optimization**: Optimized assets and code splitting for fast page loads
- **SEO Best Practices**: Built-in SEO optimization for better visibility
- **Analytics Integration**: Ready for integration with government-approved analytics tools
- **Content Management**: Structured for easy content updates and maintenance

## 🚦 Getting Started

### Prerequisites
- Node.js 18.x or later
- npm or yarn package manager
- Python 3.8+ (for translation service)

### Installation

Clone the repository:
```bash
git clone https://github.com/Zeeshanunique/government_sample.git
cd government_sample
```

Install the frontend dependencies:
```bash
npm install
# or
yarn install
# or
pnpm install
```

Install the translation service dependencies:
```bash
cd python-api
pip install -r requirements.txt
```

Run the development server:
```bash
npm run dev
# or
yarn dev
# or
pnpm dev
```

Start the translation service:
```bash
cd python-api
uvicorn main:app --reload
```

Launch the translation interface:
```bash
cd python-api
streamlit run app.py
```

Open [http://localhost:3000](http://localhost:3000) for the main website and [http://localhost:8501](http://localhost:8501) for the translation interface.

## 🌐 Deployment

This project is configured for seamless deployment on Vercel. The live demo is available at:
[https://government-sample-enmkzqms5-zeeshanuniques-projects.vercel.app](https://government-sample-enmkzqms5-zeeshanuniques-projects.vercel.app)

### Deployment Options
- **Vercel**: One-click deployment with GitHub integration
- **Netlify**: Alternative deployment with similar capabilities
- **Docker**: Container configuration available for deployment in government infrastructure
- **Cloud Providers**: Compatible with AWS, Azure, and Google Cloud Platform

## 🔒 Security Considerations

This template includes:
- CSRF protection
- XSS prevention measures
- Input sanitization
- Security headers configuration
- Rate limiting setup
- Secure cookie handling

## 🌱 Future Roadmap

- Integration with common government payment gateways
- Enhanced accessibility features
- Digital identity verification
- Document management system
- Citizen feedback modules
- API for external service integration
- Expanded language support for translation service
- Enhanced translation model with transformer architecture
- Integration of translation service into the main website interface

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgments

- The shadcn/ui team for their excellent component library
- Next.js team for the robust framework
- Government digital service standards from around the world that inspired this template
- The open source NLP community for translation tools and resources