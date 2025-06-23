import streamlit as st
import random

# Page configuration
st.set_page_config(
    page_title="🌍 Travel Assistant India",
    page_icon="✈️",
    layout="centered"
)

# Custom CSS for colorful design and gradient background
st.markdown("""
<style>
    .main {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 20px;
    }
    
    .stApp {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    }
    
    .title-text {
        color: white;
        text-align: center;
        font-size: 3rem;
        font-weight: bold;
        margin-bottom: 2rem;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
    }
    
    .input-container {
        background: rgba(255, 255, 255, 0.9);
        padding: 2rem;
        border-radius: 15px;
        margin: 1rem 0;
        box-shadow: 0 8px 32px rgba(0,0,0,0.1);
    }
    
    .plan-container {
        background: rgba(255, 255, 255, 0.95);
        padding: 2rem;
        border-radius: 15px;
        margin: 1rem 0;
        box-shadow: 0 8px 32px rgba(0,0,0,0.1);
    }
    
    .day-header {
        background: linear-gradient(90deg, #FF6B6B, #4ECDC4);
        color: white;
        padding: 10px;
        border-radius: 8px;
        margin: 10px 0;
        font-weight: bold;
    }
    
    .cost-summary {
        background: linear-gradient(90deg, #11998e, #38ef7d);
        color: white;
        padding: 15px;
        border-radius: 10px;
        margin: 10px 0;
        font-weight: bold;
        font-size: 1.2rem;
    }
</style>
""", unsafe_allow_html=True)

# Title
st.markdown('<h1 class="title-text">🌍 Travel Assistant India ✈️</h1>', unsafe_allow_html=True)

# Input container
with st.container():
    st.markdown('<div class="input-container">', unsafe_allow_html=True)
    
    # Input fields with colorful labels
    st.markdown("### 👤 **Travel Details**")
    
    col1, col2 = st.columns(2)
    with col1:
        name = st.text_input("🎯 **Your Name**", placeholder="Enter your name")
        people = st.number_input("👥 **Number of People**", min_value=1, max_value=20, value=2)
    
    with col2:
        destination = st.selectbox(
            "🏖️ **Choose Destination**",
            ["Goa", "Kerala", "Rajasthan", "Kashmir", "Himachal Pradesh", "Tamil Nadu", "Karnataka"]
        )
        budget_type = st.selectbox(
            "💰 **Budget Type**",
            ["Budget", "Standard", "Luxury"]
        )
    
    st.markdown('</div>', unsafe_allow_html=True)

# Travel data
destinations_data = {
    "Goa": {"activities": ["Beach visits", "Water sports", "Casino", "Local markets", "Sunset cruise"], "daily_cost": {"Budget": 2500, "Standard": 4000, "Luxury": 7000}},
    "Kerala": {"activities": ["Backwater cruise", "Spice plantation", "Hill stations", "Ayurvedic spa", "Tea gardens"], "daily_cost": {"Budget": 2000, "Standard": 3500, "Luxury": 6000}},
    "Rajasthan": {"activities": ["Palace visits", "Desert safari", "Camel ride", "Local handicrafts", "Cultural shows"], "daily_cost": {"Budget": 2200, "Standard": 3800, "Luxury": 6500}},
    "Kashmir": {"activities": ["Dal Lake shikara", "Gulmarg skiing", "Pahalgam trekking", "Saffron fields", "Mughal gardens"], "daily_cost": {"Budget": 2800, "Standard": 4500, "Luxury": 8000}},
    "Himachal Pradesh": {"activities": ["Mountain trekking", "Paragliding", "Temple visits", "Apple orchards", "Adventure sports"], "daily_cost": {"Budget": 2300, "Standard": 3800, "Luxury": 6800}},
    "Tamil Nadu": {"activities": ["Temple tours", "Hill stations", "Beach visits", "Cultural sites", "Traditional dance"], "daily_cost": {"Budget": 1800, "Standard": 3200, "Luxury": 5500}},
    "Karnataka": {"activities": ["Palace tours", "Coffee plantations", "Wildlife safari", "Historical sites", "Gardens"], "daily_cost": {"Budget": 2000, "Standard": 3400, "Luxury": 5800}}
}

# Generate plan button
if st.button("🚀 **Generate Travel Plan**", type="primary"):
    if name and people and destination:
        st.markdown('<div class="plan-container">', unsafe_allow_html=True)
        
        # Welcome message
        st.markdown(f"### 🎉 Welcome {name}! Here's your 5-day {destination} travel plan for {people} people")
        
        # Get destination data
        dest_data = destinations_data[destination]
        daily_cost_per_person = dest_data["daily_cost"][budget_type]
        activities = dest_data["activities"]
        
        # Generate 5-day plan
        for day in range(1, 6):
            st.markdown(f'<div class="day-header">📅 Day {day}</div>', unsafe_allow_html=True)
            
            # Random activities for each day
            day_activities = random.sample(activities, min(2, len(activities)))
            
            st.markdown(f"**🌅 Morning:** {day_activities[0]}")
            if len(day_activities) > 1:
                st.markdown(f"**🌆 Evening:** {day_activities[1]}")
            
            # Meals
            st.markdown(f"**🍽️ Meals:** Breakfast, Lunch, Dinner")
            st.markdown(f"**🏨 Accommodation:** {budget_type} category hotel")
            st.markdown("---")
        
        # Cost calculation
        total_cost = daily_cost_per_person * 5 * people
        cost_breakdown = {
            "Accommodation": total_cost * 0.4,
            "Food": total_cost * 0.3,
            "Activities": total_cost * 0.2,
            "Transportation": total_cost * 0.1
        }
        
        # Cost summary
        st.markdown(f'<div class="cost-summary">💰 Total Cost: ₹{total_cost:,.0f} for {people} people</div>', unsafe_allow_html=True)
        
        # Cost breakdown
        st.markdown("### 📊 **Cost Breakdown:**")
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown(f"🏨 **Accommodation:** ₹{cost_breakdown['Accommodation']:,.0f}")
            st.markdown(f"🍽️ **Food:** ₹{cost_breakdown['Food']:,.0f}")
        
        with col2:
            st.markdown(f"🎯 **Activities:** ₹{cost_breakdown['Activities']:,.0f}")
            st.markdown(f"🚗 **Transportation:** ₹{cost_breakdown['Transportation']:,.0f}")
        
        # Additional info
        st.markdown("### 📝 **Important Notes:**")
        st.markdown("• Prices are approximate and may vary based on season")
        st.markdown("• Book accommodations in advance for better rates")
        st.markdown("• Carry valid ID for all activities")
        st.markdown("• Check weather conditions before travel")
        
        st.markdown('</div>', unsafe_allow_html=True)
        
        # Success message
        st.success("🎊 Your travel plan is ready! Have a wonderful trip!")
        
    else:
        st.error("⚠️ Please fill in all the required fields!")

# Footer
st.markdown("---")
st.markdown("### 🙏 **Happy Travels!** Made with ❤️ for Indian Travelers")