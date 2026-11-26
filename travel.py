from dotenv import load_dotenv
from crewai import Agent, Task, Crew

load_dotenv()  # expects OPENAI_API_KEY (or your provider's key) in .env


def build_crew() -> Crew:
    planner = Agent(
        role="Travel Planner",
        goal="Create practical, well-organized trip plans for {city}",
        backstory=(
            "You are a seasoned travel planner with extensive knowledge "
            "of cities around the world."
        ),
        verbose=True,
    )

    task = Task(
        description=(
            "Plan a {days}-day trip to {city}. Cover the top attractions, "
            "where to eat, how to get around, and a day-by-day schedule."
        ),
        expected_output=(
            "A detailed day-by-day travel itinerary for {city}, including "
            "recommended attractions, restaurants, transportation options, "
            "daily activities, and estimated costs."
        ),
        agent=planner,
    )

    return Crew(agents=[planner], tasks=[task], verbose=True)


def main() -> None:
    city = input("Which city? ").strip()
    if not city:
        print("Please enter a city name.")
        return

    days = input("How many days? [3] ").strip() or "3"
    if not days.isdigit() or int(days) < 1:
        print("Please enter a positive whole number of days.")
        return

    crew = build_crew()
    result = crew.kickoff(inputs={"city": city, "days": days})
    print("\n=== Your Itinerary ===\n")
    print(result.raw)


if __name__ == "__main__":
    main()