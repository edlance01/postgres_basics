from configparser import ConfigParser
import psycopg2

def load_config(
    filename="/Users/edwardlance/semantic_search_vector_db/semantic_seach/ModuleY_PostGres/database.ini",
    section="postgresql",
):
    parser = ConfigParser()
    parser.read(filename)
    # get section, default to postgresql
    config = {}
   
    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            config[param[0]] = param[1]
    else:
        raise Exception(
            "Section {0} not found in the {1} file".format(section, filename)
        )
    return config


if __name__ == "__main__":
    config = load_config()
    print(config)
    print("finished")
