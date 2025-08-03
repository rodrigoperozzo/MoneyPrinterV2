# MoneyPrinter V2 Configuration Guide

## 🎯 Quick Setup for YouTube Video Generation

### 1. Basic Configuration (Required)

**Firefox Profile Path**: 
- You need to create a Firefox profile that's logged into your YouTube account
- Path format: `/Users/yourusername/Library/Application Support/Firefox/Profiles/xxxxxxxx.default-release`

**Language**: 
- Set to your preferred language for content generation
- Options: English, Spanish, French, German, etc.

### 2. AI Model Settings (Optimized)

**LLM (Language Model)**: `gpt-4o-mini`
- Fast and reliable for content generation
- Alternative: `gpt-4o` for higher quality (slower)

**Image Model**: `sdxl-turbo`
- Fast AI image generation
- Alternative: `flux` for higher quality

**Threads**: `4`
- Number of parallel processes
- Increase if you have a powerful computer

### 3. Optional Settings

**AssemblyAI API Key**: 
- For automatic subtitle generation
- Get free key at: https://www.assemblyai.com/

**Email Settings**:
- For outreach functionality
- Configure if you plan to use email automation

## 🔧 Configuration Questions

Please answer these questions to customize your setup:

1. **What type of YouTube content do you want to create?**
   - Educational videos
   - Entertainment/Comedy
   - Product reviews
   - News/Current events
   - Other: _________

2. **What language should the content be in?**
   - English (default)
   - Spanish
   - French
   - German
   - Other: _________

3. **Do you have a Firefox profile set up for YouTube?**
   - Yes, path: _________
   - No, I need help setting this up

4. **Do you want to use AssemblyAI for automatic subtitles?**
   - Yes, I'll get an API key
   - No, I'll handle subtitles manually

5. **What's your computer's performance level?**
   - High-end (8+ cores, 16GB+ RAM) → Use 6-8 threads
   - Mid-range (4-6 cores, 8-16GB RAM) → Use 4 threads
   - Basic (2-4 cores, 4-8GB RAM) → Use 2 threads

## 📝 Next Steps

1. Answer the configuration questions above
2. Set up your Firefox profile
3. Update the config.json file with your preferences
4. Test the basic functionality
5. Start generating videos!

## 🚀 Recommended Settings for Different Use Cases

### For Educational Content:
```json
{
  "llm": "gpt-4o",
  "image_model": "flux",
  "script_sentence_length": 6
}
```

### For Entertainment Content:
```json
{
  "llm": "gpt-4o-mini",
  "image_model": "sdxl-turbo",
  "script_sentence_length": 3
}
```

### For Fast Production:
```json
{
  "llm": "gpt-4o-mini",
  "image_model": "sdxl-turbo",
  "threads": 6,
  "headless": true
}
``` 